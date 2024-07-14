from django.db import models
from common.models import TrackingModel
from user.models import UserAccount


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


class Board(TrackingModel):
    """Project model, used for store all project reference"""

    title = models.CharField(max_length=100, blank=False, null=False, verbose_name="Project title")
    description = models.TextField(max_length=500, blank=True, null=True, verbose_name="Short description")
    working = models.BooleanField(default=True, verbose_name="Currently working")
    color = models.CharField(max_length=15, choices=PROJECT_COLORS, default='default', verbose_name="Project UI color")
    
    # Relationship
    users = models.ManyToManyField(UserAccount)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class Card(TrackingModel):
    """Card model, used for store all card reference"""

    title = models.CharField(max_length=100, blank=False, null=False, verbose_name="Card title")
    description = models.TextField(max_length=500, blank=True, null=True, verbose_name="Short description")
    color = models.CharField(max_length=15, choices=PROJECT_COLORS, default='default', verbose_name="Card color")
    
    # Relationship
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'



class CardItem(TrackingModel):
    """CardItem model, used for store all card item reference"""

    title = models.CharField(max_length=100, blank=False, null=False, verbose_name="Item title")
    description = models.TextField(blank=True, null=True, verbose_name="Short description")
    working = models.BooleanField(default=True, verbose_name="Currently working")
    
    # Relationship
    card = models.ForeignKey(Card, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(UserAccount, on_delete=models.CASCADE, verbose_name="Created by", null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Card Item'
        verbose_name_plural = 'Card Items'


class CardItemComment(TrackingModel):
    """CardItem model, used for store all card item reference"""

    body = models.TextField(verbose_name="Comment text")
    
    # Relationship
    card_item = models.ForeignKey(CardItem, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.body[:20]

    class Meta:
        verbose_name = 'Card Item Comment'
        verbose_name_plural = 'Card Item Comments'
