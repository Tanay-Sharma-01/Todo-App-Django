from colors.get_colors import color
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Todo 
from rest_framework.response import Response
from .serializer import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from user.models import TOKENS
import requests
import ast
from credentials import Data as DATA
from rest_framework.decorators import api_view , authentication_classes , permission_classes
from django.contrib.auth.hashers import make_password
import json
from django.http import HttpResponse, HttpResponseRedirect

class TodoViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication , 
    TokenAuthentication]

    http_method_names = ["get"]
    serializer_class = TodoDataSerializer

    def list(self , request):

        print(color.CYAN , self.queryset)

        user = request.user
        get_data = user.todo_set.all()

        new_data = []
        # print(color.RED , get_data.values())
        for x in get_data:
            obj = {
                "pk": x.pk,
                "title": x.title,
                "description": x.description,
                "start_date" : x.start_date,
                "end_date": x.end_date
            }
            new_data.append(obj)            
        # print(color.GREEN , new_data)

        return Response(new_data)
    

class CreateTodoViewSet(viewsets.ModelViewSet):
    
    authentication_classes = [SessionAuthentication , TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    http_method_names = ["post"]
    
    serializer_class = TodoDataSerializer

    def create(self , request):
        
        post_data = request.data;
        post_data = post_data.dict()

        post_data["user"] = self.request.user.pk;

        serialized = TodoDataSerializer(data = post_data)
        if(serialized.is_valid()):
            serialized.save();

        return HttpResponseRedirect("/")

class CreateUserTokenViewSet(viewsets.ModelViewSet):
    
    http_method_names = ["post"]
    serializer_class = UserSerializer

    def create(self, request):
        
        data = request.data.dict();
        
        save_password = data["password"];
        hashed_password = make_password(save_password)
        data["password"] = hashed_password

        serialized = UserSerializer(data = data);
        
        new_user = ...
        
        if(serialized.is_valid(raise_exception=True)):
            new_user = User(username = data["username"] , password=data["password"])
            new_user.save()
        
        data["password"] = save_password
        
        response = requests.post("http://localhost:8000/auth-gettoken/" , data=data)

        data = ast.literal_eval(response.content.decode("utf-8"))
        
        token = data["token"]
        
        data = {
            "token" : token,
            "user" : new_user.pk
        }
        token_serialized = TokenSerializer(data = data)
        if(token_serialized.is_valid()):
            token_serialized.save();

        return Response(token_serialized.data);
        

class DeleteTodoViewSet(viewsets.ModelViewSet):

    http_method_names = ["get"]
    queryset = Todo.objects.all()

    def retrieve(self, request, *args, **kwargs):
    
        user = request.user;
        if(not user.is_authenticated):
            return HttpResponse("Not Authenticated")

        try:
            todo = user.todo_set.get(pk = kwargs["pk"]);
        except:
            return HttpResponseRedirect("/")

        todo.delete();
        return HttpResponseRedirect("/")
    # Now i need to delete a particular todo.

class UpdateTodoViewSet(viewsets.ModelViewSet):

    serializer_class = TodoDataSerializer
    http_method_names = ["post"]

    def create(self, request):

        data = request.data.dict();

        todo = request.user.todo_set.get(pk = data["pk"])
        data["user"] = todo.user.pk

        serialized = TodoDataSerializer(data = data);

        if(serialized.is_valid()):
            todo.title = data["title"]
            todo.description = data["description"]
            todo.start_date = data["start_date"]
            todo.end_date = data["end_date"]
            todo.save();
        
        return HttpResponseRedirect("/")

        


# @api_view(["get"])
# def delete_todo(request , pk):

#     user = request.user;
#     if(not user.is_authenticated):  
#         return HttpResponse("Not Authenticated")

#     try:
#         todo = user.todo_set.get(pk = pk);
#     except:
#         return HttpResponseRedirect("/")

#     todo.delete();
#     return HttpResponseRedirect("/")

