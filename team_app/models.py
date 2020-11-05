from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    """Team model store team data"""

    name = models.CharField(max_length=50)
    member = models.ManyToManyField(User)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
