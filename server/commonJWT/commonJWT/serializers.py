from rest_framework import serializers
from django.contrib.auth.models import User

# allows us to map JSON objects from APIs to entries in our DB
class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields= ['id', 'username', 'password', 'email']