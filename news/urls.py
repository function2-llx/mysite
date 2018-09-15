from . import views
from django.urls import path

urlpatterns = [
	path('<int:newsId>/', views.displayNews),
]