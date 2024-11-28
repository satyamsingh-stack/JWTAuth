from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class Operation1(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if(serializer.is_valid()):
            email=serializer.validated_data['email']
            if(User.objects.filter(email=email).exists()):
                return Response("Already Existed",status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class Operation2(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        try:
            user = User.objects.get(username=username)
            if(user.check_password(password)):
                refresh=RefreshToken.for_user(user)
                return Response({
                    "refresh":str(refresh),
                    "access": str(refresh.access_token)
                },status=status.HTTP_200_OK)
            return Response("invalid password",status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response([],status=status.HTTP_404_NOT_FOUND)

class Operation3(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        serializer=BlogSerializer(data=request.data)
        if(serializer.is_valid()):
            id=request.data.get('author')
            try:
                author=User.objects.get(id=id)
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            except Blog.DoesNotExist:
                return Response("Invalid Author",status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        item=Blog.objects.all()
        serializer=BlogSerializer(item,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)