from json.encoder import JSONEncoder
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .models import Profile
from .serializers import ProfileSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def register(request):
    serializer=ProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def login(request):
    email1=request.GET['email']
    password1=request.GET['password']
    profiles=Profile.objects.filter(email=email1).filter(password=password1) 
    serializer1=ProfileSerializer(profiles,many=True)
    return Response(serializer1.data,status=status.HTTP_201_CREATED)
    # return Response(status=status.HTTP_400_BAD_REQUEST)



