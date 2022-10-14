from email.policy import default
from django.db import models

class Player(models.Model):

    Name = models.CharField(max_length = 50)
    Team = models.CharField(max_length = 50)
    Age = models.IntegerField()
    Sport = models.CharField(max_length = 50)

    def __str__(self):
        return self.Name

    class Meta:
        unique_together = ["Name" , "Team" , "Age" , "Sport"]

# Creating two models first one is Player and second is Family which will simply hold the family details of the player

class Family(models.Model):
    
    Members = models.IntegerField()
    Location = models.CharField(max_length = 100)
    Married = models.BooleanField(default = False)
    Player = models.OneToOneField(Player , on_delete = models.CASCADE)

    def __str__(self):
        return self.Player.Name;

