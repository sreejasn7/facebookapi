from django.conf.urls import url
from .views import UserList , FileUploadCSV , FileUploadJson, PsidPageMap
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ps_id_list/', UserList.as_view(), name='psid'),
    url(r'^upload_csv/', FileUploadCSV.as_view(), name='upload_csv'),
    url(r'^upload_json/', FileUploadJson.as_view(), name='upload_json'),
    url(r'^psid_page_map/', PsidPageMap.as_view(), name='psid_page_map'),

]
