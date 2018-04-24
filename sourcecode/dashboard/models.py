from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MemberCard(models.Model):
    quota = models.IntegerField(default=0)
    related_user = models.ForeignKey(User, on_delete=models.CASCADE)
