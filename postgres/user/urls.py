from django.urls import path , include
from .views import *
from rest_framework.authtoken import views

urlpatterns = [
    path("" , home , name = "home"),
    path("signup/" , signup , name = "signup"),
    path("login/" , login , name="login"),
    path("auth/" , include("rest_framework.urls") , name = "rest"),
    path("authenticate_login_request/" , authenticate_login_request , name = "auth_login_request"),
    path("profile/"  , profile , name="profile"),
    path("invalid-details/<int:val>/" , invalid_user , name="invalid_user"),
    path("create_user/" , create_user , name="create_user"),
    path("auth-gettoken/" , views.obtain_auth_token , name="get-token"),
    path("add-todo/" , add_Todo , name="add-todo"),
    path("todo-auth/" , todo_auth , name="todo-auth")
]