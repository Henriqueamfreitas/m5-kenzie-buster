from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from users.serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomJWTSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from movies.permissions import IsSuperuserOrReadOnly
from .models import User
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from .permissions import IsAdminUserOrSelf


# Create your views here.
class UserView(APIView):
	def post(self, request: Request) -> Response:
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer

class UserDetailView(APIView):
	authentication_classes = [JWTAuthentication]
	permission_classes = [IsAdminUser]
	def get(self, request: Request, user_id: int) -> Response:
		print(request.user.id)
		try:
			found_user = User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return Response({'message': 'User not found'}, status.HTTP_404_NOT_FOUND)
		
		serializer = UserSerializer(found_user)
		return Response(serializer.data)
        
	def patch(self, request: Request, user_id: int) -> Response:
		try:
			found_user = User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return Response({'message': 'User not found'}, status.HTTP_404_NOT_FOUND)
		
		serializer = UserSerializer(found_user, data=request.data, partial=True)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
