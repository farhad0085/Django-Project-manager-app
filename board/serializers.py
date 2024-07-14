from rest_framework import serializers
from board.models import Board, Card, CardItem
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


class BoardSerializer(serializers.ModelSerializer):

    card_set = CardSerializer(many=True, read_only=True)
    users = UserAccountSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = '__all__'
