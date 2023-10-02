from django.shortcuts import render
from builder.models import BaseDockerImage
from django.views.generic import ListView


class DockerImageLV(ListView):
    template_name = 'main.html'
    context_object_name = 'docker_image'

    def get_queryset(self):
        return BaseDockerImage.objects.all()

