from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from team_app.models import Team
from .serializers import TeamSerializer

class TeamViewSet(ModelViewSet):
    """View set for teams"""

    queryset = Team.objects.order_by('-date_created').all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]

    class Meta:
        model = Team