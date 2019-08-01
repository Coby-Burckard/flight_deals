from django.urls import path
from . import views

urlpatterns = [
    path('skymiles_tracker/deals/', views.get_deals),
    path('skymiles_tracker/get_history/<str:departure_airport>/<str:arrival_airport>/', views.get_history),
]