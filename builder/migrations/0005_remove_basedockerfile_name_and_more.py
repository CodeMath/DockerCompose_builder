# Generated by Django 4.2.5 on 2023-10-02 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0004_basedockerfile_dockerfile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basedockerfile',
            name='name',
        ),
        migrations.AddField(
            model_name='basedockerimage',
            name='dockerfile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='builder.basedockerfile', verbose_name='도커파일'),
        ),
    ]
