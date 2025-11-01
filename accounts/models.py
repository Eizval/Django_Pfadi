from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    is_approve = models.BooleanField(default=False)
    role = models.ForeignKey('Role', on_delete=models.PROTECT, null=True, blank=True)

class Role(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name