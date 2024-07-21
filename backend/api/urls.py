from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
	path("auth/", obtain_auth_token, name="generate token for a user"),
	path("", views.json_get)
]
