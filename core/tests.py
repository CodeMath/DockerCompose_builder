import pytest
from django.shortcuts import get_object_or_404
from builder.models import *
from builder.factories import *


@pytest.mark.django_db
def test_get_docker_image_code():
    _docker = BaseDockerImageFactory()
    assert get_object_or_404(BaseDockerImage, name__iexact=_docker.name)
    assert {'code': _docker.command_code, 'name': _docker.name}



