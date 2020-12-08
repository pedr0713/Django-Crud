from django.urls import path
from .views import home

urlpatterns = [
    path('', home),#direciona para a funcao home do views
	
]