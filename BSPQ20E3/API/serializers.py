from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
	'''Serializes user objects

	:param req: User object queryset
	:type amount: User object

	:returns: Users list
	:rtype: Json
	'''
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'last_login')