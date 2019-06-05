# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .serializers import UserSerializer
from .models import MessengerUser
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser


# Create your views here.

from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from rest_framework.response import Response



def index(request):
    return HttpResponse("Hello There !!!. You are running your application.")

class UserList(generics.ListAPIView):
    queryset = MessengerUser.objects.all()
    serializer_class = UserSerializer

class FileUploadView(generics.CreateAPIView):
    parser_classes = (FileUploadParser,)

    def put(self, request, filename, format=None):
        file_obj = request.FILES['file']
        print file_obj
        return Response(status=204)