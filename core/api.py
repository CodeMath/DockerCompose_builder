from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotAllowed
from django.http import JsonResponse

from builder.models import BaseDockerImage, DockerComposeImage
import json

from django.http import FileResponse, HttpResponse
import uuid
from io import StringIO, BytesIO
import time
import zipfile


def get_docker_image_code(request):
    """
    get docker image command code
    """
    if request.method == "POST":
        json_load = json.load(request)
        try:
            app = get_object_or_404(BaseDockerImage, name__iexact=json_load["name"])
            return JsonResponse({'code': app.command_code, 'name': app.name})
        except Exception as e:
            print(e)
            return JsonResponse({'msg': "Does not exist."}, status=404)

    else:
        return HttpResponseNotAllowed(['POST'])


def convert_to_docker_compose_file(request):
    """
    convert from docker compose code to docker-compose.yml file
    """
    if request.method == "POST":
        json_load = json.load(request)
        raw_yaml = json_load["code"].replace("\t", "    ")

        rdk = f"""{raw_yaml}
        """
        uid = str(uuid.uuid4().hex) + f"{time.time()}".replace('.', '')

        dci = DockerComposeImage.objects.create(
            name=uid,
            compose_code=rdk,
            description=",".join(json_load["used"])
        )
        dk_file = []

        for i in json_load["used"]:
            try:
                dk = BaseDockerImage.objects.get(name__iexact=i)
                dci.apps.add(dk)
                if dk.dockerfile:
                    dk_file.append(dk)
            except:
                pass

        dci.save()


        # write file in memoryq
        f = StringIO(rdk)

        # exist dockerfile?
        if dk_file:

            # make zip
            zip_buffer = BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w') as zips:
                for dk in dk_file:
                    zips.writestr(
                        f"{dk.name}/{dk.dockerfile.dockerfile_name}", StringIO(f"{dk.dockerfile.dockerfile}").getvalue()
                    )
                zips.writestr("docker-compose.yml", f.getvalue())
                zips.close()

            response = HttpResponse(zip_buffer.getvalue(), content_type="application/zip")
            response['Content-Disposition'] = 'attachment; filename=docker-compose.zip'
            response.headers['Content-Type'] = 'application/zip'


        else:
            response = HttpResponse(f.getvalue(), content_type="application/yaml")
            response['Content-Disposition'] = 'attachment; filename=docker-compose.yml'
            response.headers['Content-Type'] = 'application/yaml'

        return response

    else:
        return HttpResponseNotAllowed(['POST'])
