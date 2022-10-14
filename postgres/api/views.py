from colors.get_colors import color
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view , authentication_classes , permission_classes
from .models import Player
from rest_framework.authentication import SessionAuthentication , BasicAuthentication , TokenAuthentication
from .serializer import PlayerSerializer
from rest_framework.permissions import IsAuthenticated
import re
from rest_framework.viewsets import ModelViewSet

def get_data(request):
    data = {
        "Name": request.POST.get("Name"),
        "Age" : request.POST.get("Age"),
        "Sport": request.POST.get("Sport"),
        "Team": request.POST.get("Team")
    }
    return data;

def regex(pattern):

    regex = r"(\w)+@(\w)+.([a-zA-Z]{2,5})"
    ans = re.match(regex , pattern)
    print(color.GREEN , ans)
    print(color.YELLOW) # ans will be none if provided pattern is wrong.
        

@api_view(["GET"])
@authentication_classes([TokenAuthentication , SessionAuthentication])
@permission_classes([IsAuthenticated])
def show_data(request):

    get_data = Player.objects.all();
    serialized = PlayerSerializer(get_data , many=True)
    return JsonResponse(serialized.data , safe=False)

@api_view(["POST"])
def add_player(request):
    if(request.method == "POST"):
    
        data = get_data(request)
        
        serialized = PlayerSerializer(data = data);
        if(serialized.is_valid()):
            serialized.save();
        else:
            return HttpResponse("PLAYER ALREADY EXIXTS")
        
        return Response(serialized.data)

# @api_view(["PUT"])
# @authentication_classes([TokenAuthentication , SessionAuthentication])
# @permission_classes([IsAuthenticated])
# def update_player(request):

#     data = get_data(request)
#     try:
#         player = Player.objects.get(Name = request.POST.get("user"))
#     except:
#         return Response("Invalid Request Data")
#     else:
#         serialized = PlayerSerializer(data = data)

#         print(color.BLUE , data)

#         if(serialized.is_valid()):
            
#             player.Name = data["Name"]
#             player.Age = data["Age"]
            
#             player.Sport = data["Sport"]
#             player.Team = data["Team"]
            
#             player.save();
#         else:
#             return Response("Updated User creadentials already found ...")

#     print(color.GREEN , data)
#     return Response(data)


# @api_view(["DELETE"])
# @authentication_classes([TokenAuthentication , SessionAuthentication])
# @permission_classes([IsAuthenticated])
# def delete_player(request):
#     user = request.POST.get("user")
#     try:
#         player = Player.objects.get(Name = user)
#     except:
#         return Response("Invalid Data")
#     else:
#         player.delete();
#         return Response("{} is deleted".format(user))

class PlayerViewSet(ModelViewSet):
    model = Player
    serializer_class = PlayerSerializer
    http_method_names = ["get"]
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication , TokenAuthentication]
    queryset = Player.objects.all() 

class AddPlayerViewSet(ModelViewSet):
    model = Player
    http_method_names = ["get" ,"post"]
    serializer_class = PlayerSerializer

    

    
