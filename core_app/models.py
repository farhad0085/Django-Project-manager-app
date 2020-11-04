from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    """Project model, used for store all project reference"""

    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        pass

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'