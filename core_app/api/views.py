from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from core_app.models import Card, Project, CardItem
from .serializers import ProjectSerializer, CardSerializer, CardItemSerializer, ProjectRetriveSerializer
from .permissions import IsOwnProject



class ProjectViewSet(ModelViewSet):
    """Viewset for project"""

    queryset = Project.objects.order_by('-date_created').all() 
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsOwnProject]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProjectRetriveSerializer
        return self.serializer_class

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


class ProjectCardListAPIView(ListAPIView):
    """List all cards for a single project"""

    queryset = Project.objects.all()
    serializer_class = CardSerializer

    def get_queryset(self):
        queryset = self.queryset
        try:
            cards = queryset.get(id=self.kwargs.get('project_id')).card_set.all()
        except Project.DoesNotExist:
            return []
        return cards