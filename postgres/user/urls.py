from django.urls import path , include
from .views import *
from rest_framework.authtoken import views

urlpatterns = [
    path("" , HomeView.as_view() , name="asdasd"),
    path("<int:page>/" , HomeView.as_view() , name="asdasd"),
    path("signup/" , SignupView.as_view()),
    path("login/" , LoginView.as_view()),
    path("profile/" , ProfileView.as_view()),
    path("auth/" , include("rest_framework.urls") , name = "rest"),
    path("authenticate_login_request/" , AuthenticateLoginRequestView.as_view()),
    path("invalid-details/<int:val>/" , InvalidUserView.as_view() , name="invalid_user"),
    path("create_user/" , CreateUserView.as_view() , name="create_user"),
    path("add-todo/" , AddTodoView.as_view() , name="add-todo"),
    path("todo-auth/" , TodoAuthView.as_view() , name="todo-auth"),
    path("update-todo/<int:pk>/" , UpdateTodoView.as_view() , name="updateTodo"),
    path("auth-gettoken/" , views.obtain_auth_token , name="get-token"),
    # path("" , home , name = "home"),
    # path("<int:page>/" , home , name = "home"),
    # path("signup/" , signup , name = "signup"),
    # path("login/" , login , name="login"),
    # path("authenticate_login_request/" , authenticate_login_request , name = "auth_login_request"),
    # path("profile/"  , profile , name="profile"),
    # path("invalid-details/<int:val>/" , invalid_user , name="invalid_user"),
    # path("create_user/" , create_user , name="create_user"),
    # path("add-todo/" , add_Todo , name="add-todo"),
    # path("todo-auth/" , todo_auth , name="todo-auth"),
    # path("update-todo/<int:pk>/" , updateTodo , name="updateTodo")
]
