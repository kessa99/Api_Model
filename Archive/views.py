from rest_framework import viewsets
from .models import Archive
from .serializers import ArchiveSerialisers

# Create your views here.

class ArchiveViewSet(viewsets.ModelViewSet):
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerialisers