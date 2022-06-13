from django.db import models
from django.contrib.auth import settings


# Create your models here.

class group(models.Model):
    group_id = models.BigAutoField(primary_key=True)  # 自增主键
    icon_id = models.IntegerField(null=True)
    owner = models.CharField(max_length=30, null=False)
    name = models.CharField(max_length=30, null=False, unique=True)
    introduction = models.CharField(max_length=100)


class user_user(models.Model):
    user_name = models.CharField(max_length=30, null=False)
    friend_name = models.CharField(max_length=30, null=False)
    relationship = models.CharField(max_length=32)
    latest_messages = models.CharField(max_length=100)

    class Meta:
        unique_together = (("user_name", "friend_name"),)


