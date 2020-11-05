from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core_app.models import Card, Project, CardItem
from .serializers import ProjectSerializer, CardSerializer, CardItemSerializer
from .permissions import IsOwnProject



class ProjectViewSet(ModelViewSet):
    """Viewset for project"""

    queryset = Project.objects.order_by('-date_created').all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsOwnProject]

    class Meta:
        model = Project


class CardViewSet(ModelViewSet):
    """Viewset for card"""

    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]

    class Meta:
        model = Card


class CardItemViewSet(ModelViewSet):
    """Viewset for card item"""

    queryset = CardItem.objects.all()
    serializer_class = CardItemSerializer
    permission_classes = [IsAuthenticated]

    class Meta:
        model = CardItem