from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Client(models.Model):
    clientName = models.OneToOneField(User,on_delete=models.CASCADE,related_name='Name_of_Client')
    createdAt = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.clientName.username

