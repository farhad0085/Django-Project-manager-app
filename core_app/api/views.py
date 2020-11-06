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

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(users=self.request.user)
        return query_set


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
