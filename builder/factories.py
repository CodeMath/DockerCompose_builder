import factory
from builder.models import *


class BaseDockerFileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BaseDockerFile

    dockerfile_name = "Dockerfile.example_app"
    dockerfile = """FROM:python:3.9-alpine
    pip install -r requirements.txt
    """

class BaseDockerImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BaseDockerImage

    name = "example_app"
    main_services_name = "web"
    sub_services_name = "admin"
    command_code = """example_app:
        image: example_app:latest
    """
    dockerfile = factory.SubFactory(BaseDockerFileFactory)


