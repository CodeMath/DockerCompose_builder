import factory
from builder_docker.models import *


class BaseDockerFileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BaseDockerFile

    dockerfile_name = "Dockerfile"
    dockerfile = """FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "manage.py", "runserver" ]
    """


class BaseDockerImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BaseDockerImage

    name = factory.sequence(lambda n: "#%s apps" %n)
    command_code = """apps:
		build:
			context: .
			dockerfile: Dockerfile
		command:
			- ["python", "manage.py", "runserver"]
		ports:
			- "8000:8000"
		expose:
			- "8000"
		restart: always
        """
    main_services_name = "web"
    sub_services_name = "Dockerfile"


class WithDockerfileFactory(BaseDockerImageFactory):
    dockerfile = factory.SubFactory(BaseDockerFileFactory)


class DockerComposeImageFactory(factory.django.DjangoModelFactory):
    """
    add apps without Dockerfile
    """
    class Meta:
        model = DockerComposeImage
    compose_code = """version: "3.7"
services:
	nginx:
		image: nginx
		volumes:
			- ./nginx.conf:/etc/nginx/nginx.conf
	postgres:
		image: postgres
	    restart: always
    	ports:
    		- "5432:5432"
		env_file: 
    		- .env
		volumes:
        	- ./postgres/data:/var/lib/postgresql/data
    """
    description = "nginx,postgres"

class DockerComposeImageWithAppsFactory(DockerComposeImageFactory):
    """
    add apps with Dockerfile
    """
    class Meta:
        model = DockerComposeImage
        skip_postgeneration_save = True

    compose_code = """version: "3.7"
services:
	nginx:
		image: nginx
		volumes:
			- ./nginx.conf:/etc/nginx/nginx.conf

	apps:
		build:
			context: .
			dockerfile: Dockerfile.django
		command:
			- ["python", "manage.py", "runserver"]
		ports:
			- "8000:8000"
		expose:
			- "8000"
		restart: always

	postgres:
		image: postgres
	    restart: always
    	ports:
    		- "5432:5432"
		env_file: 
    		- .env
		volumes:
        	- ./postgres/data:/var/lib/postgresql/data
    """
    description = "nginx,apps,postgres"

    @factory.post_generation
    def apps(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for app in extracted:
                self.apps.add(app)