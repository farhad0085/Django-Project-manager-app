from django.db import models
from user.models import UserAccount


class Team(models.Model):
    """Team model store team data"""

    name = models.CharField(max_length=50)
    member = models.ManyToManyField(UserAccount)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
