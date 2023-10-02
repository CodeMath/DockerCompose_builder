from django.urls import path
from core.api import *

urlpatterns = [
    path('code/get', get_docker_image_code, name="get_docker_image_code"),
    path('code/download', convert_to_docker_compose_file, name="convert_to_docker_compose_file")
]
