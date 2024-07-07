from django.urls import path
from . import views

app_name = 'kotob'
urlpatterns = [
    path('', views.Home.as_view(), name='kotob'),
]