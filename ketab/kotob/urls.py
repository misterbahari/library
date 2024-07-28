from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_token

app_name = 'kotob'
urlpatterns = [
    path('', views.Home.as_view(), name='kotob'),
    path('api-token-auth/', auth_token.obtain_auth_token),
]