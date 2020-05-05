from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

#https://www.django-rest-framework.org/api-guide/permissions/
@permission_classes([IsAdminUser])
class UserViewSet(viewsets.ModelViewSet):
	""" API endpoint that allows users to be viewed or edited."""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer