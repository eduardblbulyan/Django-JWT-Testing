from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

@api_view(["POST"])
def login(request):
    return Response({})

@api_view(["POST"])
def signup(request):
    serializers = UserSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data["password"]) # hashed password
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializers.data})
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def test_token(request):
    return Response({})