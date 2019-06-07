from django.conf.urls import url
from .views import UserList , FileUploadCSV , FileUploadJSON, PSIDPageMap, UserListPagination
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^PSID_list/', UserList.as_view(), name='psid'),
    url(r'^upload_csv/', FileUploadCSV.as_view(), name='upload_csv'),
    url(r'^upload_json/', FileUploadJSON.as_view(), name='upload_json'),
    url(r'^PSID_page_map/', PSIDPageMap.as_view(), name='psid_page_map'),
    url(r'^PSID_list_pages/', UserListPagination.as_view(), name='psid_page_map'),

]
