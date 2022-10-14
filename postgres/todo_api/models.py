from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 400)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User , on_delete = models.CASCADE)

    def __str__(self):
        return self.title;
