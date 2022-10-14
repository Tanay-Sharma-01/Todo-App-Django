from email.mime import base
from wsgiref.simple_server import demo_app
from django.urls import path , include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"player" , PlayerViewSet)
router.register(r"addplayer" , AddPlayerViewSet , basename="adding_player")

urlpatterns = router.urls
