from django.urls import path
from . import views
from django.conf.urls import url

app_name = "basic_app"
urlpatterns = [
    path('', views.index, name='index'),
    url('other/', views.other, name='other'),
    url('relative/', views.relative, name='relative'),
]
