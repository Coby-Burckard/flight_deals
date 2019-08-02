from django.urls import path
from . import views

urlpatterns = [
    path('skymiles_tracker/deals/', views.get_deals),
    path('skymiles_tracker/get_history/<int:deal_id>/', views.get_history),
]