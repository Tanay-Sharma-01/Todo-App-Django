from django.db import models
from django.contrib.auth.models import User

class TOKENS(models.Model):
    token = models.CharField(max_length = 200)
    user = models.OneToOneField(User , on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username
