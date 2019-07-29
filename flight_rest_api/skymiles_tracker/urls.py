from django.urls import path
from . import views

urlpatterns = [
    path('skymiles_tracker/deals/', views.get_deals),
]