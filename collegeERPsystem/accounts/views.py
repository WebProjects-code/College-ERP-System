from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from .permissions import IsAdmin, IsSelfOrAdmin
from rest_framework.decorators import action
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ["create","list","destroy"]:
            permission_classes = [IsAdmin]
        elif self.action in ["retrieve","partial_update","update"]:
            permission_classes = [IsSelfOrAdmin]
        else:
            permission_classes = [IsAdmin]
        return [p() for p in permission_classes]

    @action(detail=False, methods=["get"], url_path="me")
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
