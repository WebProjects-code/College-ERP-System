from rest_framework import viewsets
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    @action(detail=False, methods=["post"])
    def mark_read(self, request):
        ids = request.data.get("ids", [])
        Notification.objects.filter(id__in=ids).update(read=True)
        return Response({"updated": len(ids)})
