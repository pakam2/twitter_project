from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ModelBasicInfo(models.Model):
    edited_at = models.DateTimeField(auto_now=True)
    created_at =  models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

class Tweet(ModelBasicInfo):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
