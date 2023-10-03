import pytest
from builder.factories import *
import json
from django.urls import reverse


@pytest.mark.django_db
def test_added_apps_without_dockerfile_200(client):
    _docker_compose = DockerComposeImageFactory()

    res = client.post(
        reverse('convert_to_docker_compose_file'),
        json.dumps({
            'code': _docker_compose.compose_code,
            'used': _docker_compose.description
        }),
        content_type="application/json"
    )
    assert res.status_code == 200
    assert res['content-type'] == "application/yaml"


@pytest.fixture
def test_generate_docker_image():
    return WithDockerfileFactory()

@pytest.mark.django_db
def test_added_apps_with_dockerfile_200(client, test_generate_docker_image: factory.django.DjangoModelFactory):

    assert test_generate_docker_image.dockerfile.dockerfile_name == "Dockerfile"

    _docker_compose = DockerComposeImageWithAppsFactory.create(
        apps=(test_generate_docker_image, )
    )

    assert _docker_compose.apps.first().dockerfile.dockerfile_name == "Dockerfile"


    res = client.post(
        reverse('convert_to_docker_compose_file'),
        json.dumps({
            'code': _docker_compose.compose_code,
            'used': [test_generate_docker_image.name]
        }),
        content_type="application/json"
    )

    assert DockerComposeImage.objects.last().apps.all().count() == 1
    assert res.status_code == 200
    assert res['content-type'] == "application/zip"
