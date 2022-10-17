from pydoc import describe
from threading import activeCount
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from colors.get_colors import color
from django.contrib.auth.models import User
from django.contrib.auth import login as LOGIN
from django.contrib.auth.hashers import make_password  
from credentials import Data as DATA
import requests
from todo_api.models import Todo
import requests
import datetime
import ast

month = {
    1 : "Jan.",
    2 : "Feb.",
    3 : "Mar.",
    4 : "Apr.",
    5 : "May.",
    6 : "Jun.",
    7 : "Jul.",
    8 : "Aug.",
    9 : "Sep.",
    10 : "Oct.",
    11 : "Nov.",
    12 : "Dec.",
}


def get_token(user):
    DATA.TOKEN = user.tokens.token
    return DATA.TOKEN

def home(request):
    # Use request.user.is_authenticated , this will return true if the user is already logged in otherwise false

    isLoggedIn = request.user.is_authenticated;
    user = request.user

    data = []

    if(isLoggedIn):
        get_token(user);
        
        data = requests.get("http://localhost:8000/api/v1/show/" , headers={
            "Authorization" : "TOKEN {}".format(DATA.TOKEN)
        })
        data = ast.literal_eval(data.content.decode("utf-8"))

    return render(request , "user/home.html" , {
        "user" : request.user,
        "isAuth" : isLoggedIn,
        "data" : data
    })

def signup(request):  
    if(request.user.is_authenticated):
        return HttpResponseRedirect("/")
    # print(color.GREEN , request.user)
    return render(request , "user/signup.html")

def login(request):    

    if(request.user.is_authenticated):
        return HttpResponseRedirect("/")
    return render(request , "user/login.html");

def profile(request):
    if(not request.user.is_authenticated):
        return HttpResponseRedirect("/")
    return render(request , "user/Profile.html" , {
        "user": request.user
    })

def authenticate_login_request(request):

    pas = request.POST.get("password")
    use = request.POST.get("username")
    user = authenticate(username = use, password = pas);
    
    if user is not None:

        # print(color.GREEN , "user is authenticated" , user)
        account = User.objects.get(username = use);
        LOGIN(request , account)
        return HttpResponseRedirect("/");

    else:
        # print(color.RED , "user is not authenticated");
        return HttpResponseRedirect("/invalid-details/1/")
    
def invalid_user(request , val):
    # print(color.GREEN , request.user)
    if(request.user.is_authenticated):
        return HttpResponseRedirect("/")
            
    return render(request , "user/invalid.html" , {
        "val" : val
    })

def create_user(request):

    username = request.POST.get("username");
    password = request.POST.get("password");

     
    response = requests.post("http://localhost:8000/api/v1/create-user-token/" , data={
        "username" : username,
        "password" : password
    })

    print(color.CYAN , response)
    data = ast.literal_eval(response.content.decode("utf-8"))
    print(color.YELLOW , data , type(data))

    keys = data.keys();

    if("user" in keys):
        account = User.objects.get(pk = data["user"])
        LOGIN(request , account)
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/invalid-details/0/")



def add_Todo(request):
    if(not request.user.is_authenticated):
        return HttpResponseRedirect("/")
    return render(request , "user/add-todo.html")

def todo_auth(request):
    user = request.user;
    
    title = request.POST.get("title")
    description = request.POST.get("description")
    start_date = request.POST.get("start-date")
    end_date = request.POST.get("end-date")

    # print( color.GREEN , start_date , end_date)

    new_todo = user.todo_set.create(title = title , description=description , start_date=start_date , end_data=end_date);
    new_todo.save()
    # print(new_todo)

    return HttpResponseRedirect("/")

def updateTodo(request , pk):

    user = request.user;
    if(not user.is_authenticated):
        return HttpResponseRedirect("/")
    
    try:
        todo = user.todo_set.get(pk = pk)
    except:
        return HttpResponseRedirect("/")
    else:

        title = todo.title
        description = todo.description
        start_date = todo.start_date
        end_date = todo.end_date



    new_date1 = str(start_date)
    new_date2 = str(end_date)
    
    # print(color.CYAN , new_date1 , new_date2)
    # print(new_date4)

    context = {
        "title" : title,
        "description" : description,
        "start_date": new_date1,
        "end_date": new_date2,
        "pk": pk
    }
    return render(request , "user/update-todo.html" , context);
