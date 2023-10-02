from django.urls import path
from base.views import *

urlpatterns = [

    path('', DockerImageLV.as_view(), name="main")
]
