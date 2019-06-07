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
from .pagination import LargeUserSetPagination
from .logics import batch_mechanism_curl


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
    :url: PSID_list/
    """
    queryset = MessengerUser.objects.all()
    serializer_class = UserSerializer


class FileUploadCSV(APIView):
    """
    :description: FileUploadCSV to upload CSV files
    :url: upload_csv/
    :sample tests: curl -X PUT -H "Content-Disposition: attachment; filename=psids.csv;" -F "files=@psids.csv;type=text/csv" \
         http://127.0.0.1:8000/upload_csv/
    """
    parser_classes = (MultiPartParser,)

    def put(self, request, format='None'):
        """
        :param: request
        :return: Response 200, 400
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


class FileUploadJSON(APIView):
    """
    :description: FileUploadJson to upload JSON files using django rest framework
    :url: upload_json/
    :sample tests: curl -X PUT  -H "Content-Type: application/json" -d @psid.json http://127.0.0.1:8000/upload_json/
    """
    parser_classes = (JSONParser,)

    def put(self, request, format='None'):
        """
        :param: request
        :return: Response 200, 400
        """
        try:
            key_list = json.loads(request.body.decode(encoding='UTF-8'))
            for psid in key_list.itervalues():
                obj, created = MessengerUser.objects.get_or_create(ps_id=psid)
                obj.save()
            return Response({"message": "Success"}, status=200)
        except Exception as e:
            return Response({"error": e}, status=400)


class PSIDPageMap(generics.ListAPIView):
    """
    :description: Check if user and page mapping exists
    :url: PSID_page_map/
    """
    serializer_class = FacebookLabelSerializer
    queryset = {}

    def post(self, request):
        """
        :param request:owner, page
        :return: Response gives {status=True} & {owner : val , page : val } if {owner with page} exits.
        """
        if request.method == 'POST':
            queryset_result = FacebookLabel.objects.filter(owner__pk=self.request.POST["owner"],\
                                                    page__pk=self.request.POST['page'])
            queryset_js = FacebookLabelSerializer(queryset_result, many=True)
            if queryset_js.data:
                return Response({"status": True, 'result': queryset_js.data}, status=200)
            else:
                return Response({"status": False, 'result': None}, status=200)


class UserListPagination(generics.ListAPIView):
    """
    :description: List total users in pagination , Use this paginated users to send bulk requests.
    :url: PSID_list_pages/
    """
    queryset = MessengerUser.objects.all()
    serializer_class = UserSerializer
    pagination_class = LargeUserSetPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            print("response from page >", serializer.data)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
