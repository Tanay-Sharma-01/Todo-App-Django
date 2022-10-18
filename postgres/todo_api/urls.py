from email.mime import base
from django.urls import path , include
from requests import delete
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register("show" , TodoViewSet , basename="show-todo")
router.register("create" , CreateTodoViewSet , basename="create-todo")
router.register("create-user-token" , CreateUserTokenViewSet , basename="create-user-token" )
router.register("delete-todo" , DeleteTodoViewSet , basename="delete-todo")
router.register("update-todo" , UpdateTodoViewSet , basename="update-todo");
urlpatterns = router.urls
# urlpatterns += [
#     path("delete-todo/<int:pk>/" , delete_todo , name="delete-todo")
# ]

