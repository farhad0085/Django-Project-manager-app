from rest_framework import serializers
from core_app.models import Project, Card, CardItem


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'

    
class CardItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CardItem
        fields = '__all__'