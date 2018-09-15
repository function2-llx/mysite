from django.urls import path
from . import views
from django.http import HttpResponseRedirect

urlpatterns = [
	path('', lambda request: HttpResponseRedirect('0')),
	path('<int:pagenum>/', views.displayList)
]