from rest_framework import serializers
from core_app.models import Project, Card, CardItem
from user.serializers import UserAccountSerializer


class CardItemSerializer(serializers.ModelSerializer):
    created_by = UserAccountSerializer(read_only=True)

    class Meta:
        model = CardItem
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):

    carditem_set = CardItemSerializer(many=True, read_only=True)
    created_by = UserAccountSerializer(read_only=True)

    class Meta:
        model = Card
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        # fields = '__all__'
        exclude = ['users']


class ProjectRetriveSerializer(serializers.ModelSerializer):
    """Serializer for project retrieve when modelviewser called"""

    # include card set and users to it
    card_set = CardSerializer(many=True, read_only=True)
    users = UserAccountSerializer(many=True, read_only=True)


    class Meta:
        model = Project
        fields = '__all__'
