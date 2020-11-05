from django.db import models
from django.contrib.auth.models import User

PROJECT_COLORS = [
    ('default', 'Default'),
    ('black', "Black"),
    ('green', "Green"),
    ('orange', "Orange"),
    ('blue', "Blue"),
    ('violet', "Violet"),
    ('red', "Red"),
    ('yellow', "Yellow")
]

class Project(models.Model):
    """Project model, used for store all project reference"""

    title = models.CharField(max_length=100, blank=False, null=False, verbose_name="Project title")
    description = models.TextField(max_length=500, blank=True, null=True, verbose_name="Short description")
    working = models.BooleanField(default=True, verbose_name="Currently working")
    color = models.CharField(max_length=15, choices=PROJECT_COLORS, default='default', verbose_name="Project UI color")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    
    # Relationship
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'



class Card(models.Model):
    """Card model, used for store all card reference"""

    title = models.CharField(max_length=100, blank=False, null=False, verbose_name="Card title")
    description = models.TextField(max_length=500, blank=True, null=True, verbose_name="Short description")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    
    # Relationship
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'



class CardItem(models.Model):
    """CardItem model, used for store all card item reference"""

    title = models.CharField(max_length=100, blank=False, null=False, verbose_name="Item title")
    description = models.TextField(blank=True, null=True, verbose_name="Short description")
    working = models.BooleanField(default=True, verbose_name="Currently working")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    
    # Relationship
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Created by")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Card Item'
        verbose_name_plural = 'Card Items'



class CardItemComment(models.Model):
    """CardItem model, used for store all card item reference"""

    body = models.TextField(verbose_name="Comment text")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    
    # Relationship
    card_item = models.ForeignKey(CardItem, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.body[:20]

    class Meta:
        verbose_name = 'Card Item Comment'
        verbose_name_plural = 'Card Item Comments'