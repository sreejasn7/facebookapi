# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .serializers import UserSerializer, FacebookLabelSerializer
from .models import MessengerUser , FacebookLabel
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser , MultiPartParser , JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from rest_framework.response import Response
import json


def index(request):
    """
    :description: Index Page
    :url: /
    :param: request
    :return: Http Response
    """
    return HttpResponse("Hello There !!!. You are running your application.")


class UserList(generics.ListAPIView):
    """
    :description: List total users.
    :url:ps_id_list/
    """
    queryset = MessengerUser.objects.all()
    serializer_class = UserSerializer


class FileUploadCSV(APIView):
    """
    :description: FileUploadCSV to upload CSV files using django rest framework
    :url: upload_csv/
    """
    parser_classes = (MultiPartParser,)

    def put(self, request, format='None'):
        """
        :param: request
        :return: Response 200, 400
        :curl call sample : curl -X PUT -H "Content-Disposition: attachment; filename=psids.csv;" -F "files=@psids.csv;type=text/csv" \
         http://127.0.0.1:8000/upload_csv/
        """
        try:
            key_list = request.FILES.keys()
            file_obj = request.FILES[key_list[0]]
            for psid in file_obj:
                obj, created = MessengerUser.objects.get_or_create(ps_id=psid)
                obj.save()
            return Response({"message": "Success"}, status=200)
        except Exception as e:
            return Response({"error": e}, status=400)


class FileUploadJson(APIView):
    """
    :description: FileUploadJson to upload JSON files using django rest framework
    :url: upload_json/
    """
    parser_classes = (JSONParser,)

    def put(self, request, format='None'):
        """
        :param: request
        :return: Response 200, 400
        :curl call sample :curl -X PUT  -H "Content-Type: application/json" -d @psid.json http://127.0.0.1:8000/upload_json/
        """
        try:
            key_list = json.loads(request.body.decode(encoding='UTF-8'))
            for psid in key_list.itervalues():
                obj, created = MessengerUser.objects.get_or_create(ps_id=psid)
                obj.save()
            return Response({"message": "Success"}, status=200)
        except Exception as e:
            return Response({"error": e}, status=400)


class PsidPageMap(generics.ListAPIView):
    """
    :description: If the page .
    :url: /
    """
    serializer_class = FacebookLabelSerializer
    queryset = FacebookLabel.objects.all()

    def post(self, request):
        if request.method == 'POST':
            print(self.request.POST["owner"])
            queryset = FacebookLabel.objects.filter(owner__pk=self.request.POST["owner"],
                                                page__pk=self.request.POST['page'])
            queryset_js = FacebookLabelSerializer(queryset, many=True)
            if queryset_js.data:
                return Response({"status": True, 'result':queryset_js.data})
            else:
                return Response({"status": False,'result':None})

