from django.db import models
from django.contrib.auth.models import User



class Project(models.Model):
    """Project model, used for store all project reference"""

    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    
    date_created = models.DateTimeField(auto_now_add=True)
    
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'



class Card(models.Model):
    """Card model, used for store all card reference"""

    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
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

    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    # Relationship
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Card Item'
        verbose_name_plural = 'Card Items'



class CardItemComment(models.Model):
    """CardItem model, used for store all card item reference"""

    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    # Relationship
    card_item = models.ForeignKey(CardItem, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.body[:20]

    class Meta:
        verbose_name = 'Card Item Comment'
        verbose_name_plural = 'Card Item Comments'