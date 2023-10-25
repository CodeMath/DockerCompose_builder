from django.contrib import admin
from builder.models import *

@admin.register(BaseDockerImage)
class BaseDockerImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'main_services_name', 'sub_services_name']

@admin.register(BaseDockerFile)
class BaseDockerFileAdmin(admin.ModelAdmin):
    list_display = ["name", "dockerfile_name"]

@admin.register(DockerComposeImage)
class DockerComposeImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']