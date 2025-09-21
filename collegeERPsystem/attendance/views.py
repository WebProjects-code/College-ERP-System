from rest_framework import viewsets
from .models import Session, Record
from .serializers import *

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
