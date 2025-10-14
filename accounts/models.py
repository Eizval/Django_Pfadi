from django.db import models

# Create your models here.
class User(models.Model):
    is_approve = models.BooleanField(default=False)
    role = models.ForeignKey('Role', on_delete=models.PROTECT)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()

class Role(models.Model):
    name = models.CharField(max_length=20)
