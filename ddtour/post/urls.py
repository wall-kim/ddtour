from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'mobile/', views.post_list_mobile, name='post_list_mobile'),
]