from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from board.models import Board, Card, CardItem
from .serializers import BoardSerializer, CardSerializer, CardItemSerializer
from .permissions import IsOwnProject


class BoardViewSet(ModelViewSet):
    """Viewset for project"""

    queryset = Board.objects.order_by('-created_at').all() 
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated, IsOwnProject]

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(users=self.request.user)
        return query_set

    def perform_create(self, serializer):
        project = serializer.save()
        project.users.add(self.request.user)
        project.save()


class CardViewSet(ModelViewSet):
    """Viewset for card"""

    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]


class CardItemViewSet(ModelViewSet):
    """Viewset for card item"""

    queryset = CardItem.objects.all()
    serializer_class = CardItemSerializer
    permission_classes = [IsAuthenticated]

