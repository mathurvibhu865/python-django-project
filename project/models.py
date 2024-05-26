from django.db import models

# Create your models here.
from account.models import Client
from django.contrib.auth.models import User
class Project(models.Model):
    projectName = models.CharField(max_length=30)
    clientId = models.ForeignKey(Client,on_delete=models.CASCADE)
    user = models.ManyToManyField(User,related_name='Name_of_User')
    createdAt = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Created_by_User')
    def __str__(self) -> str:
        return self.projectName