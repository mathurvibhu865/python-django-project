from rest_framework import generics
from account.models import Client
from project.models import Project
from .serializers import ClientSerializer,ProjectSerializer

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)


class ClientDetails(generics.RetrieveDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)


class ProjectDetails(generics.RetrieveDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    