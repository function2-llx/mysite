from . import views
from django.urls import path

urlpatterns = [
	path('', views.home),
	path('searchAction', views.display)
]