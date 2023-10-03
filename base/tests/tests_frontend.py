import pytest
from django.urls import reverse
from builder.factories import *

from builder.models import BaseDockerImage



@pytest.fixture(scope="function")
def create_obj(db) -> BaseDockerImage:
    _docker = WithDockerfileFactory()
    return BaseDockerImage.objects.create(
        name="django",
        main_services_name="web",
        sub_services_name="Dockerfile",
        command_code=_docker.command_code,
        dockerfile=_docker.dockerfile
    )


@pytest.mark.django_db
def test_main_get_list_docker_images_200(client, create_obj):

    res = client.get(
        reverse('main')
    )

    assert res.status_code == 200
    assert res.context_data["docker_image"][0].name == "#0 apps"
    assert res.context_data["docker_image"][1].name == "django"
    assert res.context_data["docker_image"].count() == 2