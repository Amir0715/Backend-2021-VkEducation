from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from user.models import User
from user.serializers import UserSerializer

from user.decorators import login_required


class UserViewSet(viewsets.ViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request):
        return Response(self.serializer_class(self.queryset, many=True).data)

    @login_required
    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        return Response(self.serializer_class(user).data)

    @login_required
    @action(detail=False)
    def me(self, request):
        return Response(self.serializer_class(request.user).data)

