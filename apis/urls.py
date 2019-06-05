from django.conf.urls import url
from .views import UserList , FileUploadView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^psid/', UserList.as_view() , name='psid'),
    url(r'^upload/', FileUploadView.as_view() , name='upload_file'),

]