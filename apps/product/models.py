from datetime import datetime

from django.db import models
from apps.user.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f'{self.name}'
