# Generated by Django 4.2.5 on 2023-10-02 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseDockerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='이미지 이름')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='image')),
                ('main_services_name', models.CharField(max_length=200, verbose_name='서비스 구분')),
                ('sub_services_name', models.CharField(help_text='admin', max_length=200, verbose_name='부 서비스 구분')),
                ('command_code', models.TextField(blank=True, null=True, verbose_name='커멘드 명령어')),
                ('runner_code', models.TextField(blank=True, null=True, verbose_name='도커 run 명령어')),
            ],
        ),
        migrations.CreateModel(
            name='DockerComposeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='프로젝트 이름')),
                ('compose_code', models.TextField(blank=True, null=True, verbose_name='compose code')),
                ('description', models.TextField(blank=True, null=True, verbose_name='설명')),
                ('apps', models.ManyToManyField(blank=True, null=True, to='builder.basedockerimage', verbose_name='이미지')),
            ],
        ),
    ]
