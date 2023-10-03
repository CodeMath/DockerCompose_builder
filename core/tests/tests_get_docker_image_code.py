import pytest
from builder.factories import BaseDockerImageFactory
import json
from django.urls import reverse


@pytest.mark.django_db
def test_get_docker_image_200(client):
    _docker = BaseDockerImageFactory()

    res = client.post(
        reverse('get_docker_image_code'),
        json.dumps({
            'name': _docker.name
        }),
        content_type="application/json"
    )
    assert res.status_code == 200

@pytest.mark.django_db
def test_none_docker_image_404(client):
    res = client.post(
        reverse('get_docker_image_code'),
        json.dumps({
            'name': "404notfound"
        }),
        content_type="application/json"
    )

    assert res.status_code == 404


@pytest.mark.django_db
def test_not_allowed_method_405(client):
    _docker = BaseDockerImageFactory()
    res = client.get(
        reverse('get_docker_image_code')
    )
    assert res.status_code == 405