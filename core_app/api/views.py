from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from core_app.models import Project
from .serializers import ProjectSerializer
from .permissions import IsOwnProject



class ProjectListCreateAPIView(ListCreateAPIView):
    """List all project for an user"""

    queryset = Project.objects.order_by('-date_created').all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

class ProjectRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """List all project for an user"""

    queryset = Project.objects.order_by('-date_created').all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsOwnProject]