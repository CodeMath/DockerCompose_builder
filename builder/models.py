from django.db import models

class BaseDockerFile(models.Model):
    dockerfile_name = models.CharField(verbose_name="도커파일 이름", default='Dockerfile.', max_length=200, null=True, blank=True)
    dockerfile = models.TextField(verbose_name="커멘드 명령어", null=True, blank=True)

    def __str__(self):
        if self.dockerfile_name:
            return self.dockerfile_name
        else:
            return "None name"

class BaseDockerImage(models.Model):
    name = models.CharField(verbose_name="이미지 이름", max_length=200)
    image = models.ImageField(verbose_name="image", null=True, blank=True)
    main_services_name = models.CharField(verbose_name="서비스 구분", max_length=200, null=True, blank=True)
    sub_services_name = models.CharField(verbose_name="부 서비스 구분", max_length=200, help_text="admin", null=True, blank=True)
    command_code = models.TextField(verbose_name="커멘드 명령어", null=True, blank=True)
    runner_code = models.TextField(verbose_name="도커 run 명령어", null=True, blank=True)
    dockerfile = models.ForeignKey(BaseDockerFile, verbose_name="도커파일", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name



import uuid
class DockerComposeImage(models.Model):
    name = models.CharField(
        default='',
        verbose_name="구분값",
        max_length=60
    )
    apps = models.ManyToManyField(BaseDockerImage, verbose_name="이미지", null=True, blank=True)
    compose_code = models.TextField(verbose_name="compose code", null=True, blank=True)
    description = models.TextField(verbose_name="설명", null=True, blank=True)

    def __str__(self):
        return self.name