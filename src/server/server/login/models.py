from django.db import models
from django.contrib.auth import settings
# Create your models here.

class group(models.Model):
    group_id = models.BigAutoField(primary_key=True) #自增主键
    icon_id = models.IntegerField(null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, to_field="username", on_delete=models.CASCADE,null=False)
    name = models.CharField(max_length=30,null=False)
    introduction = models.CharField(max_length=100)








