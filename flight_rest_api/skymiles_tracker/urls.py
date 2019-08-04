from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('skymiles_tracker/deals/', views.get_deals, name='active_deals'),
    path('skymiles_tracker/get_history/<int:deal_id>/', views.get_history, name='deal_history'),
    path('skymiles_tracker/', views.api_root, name='api_root'),
]

urlpatterns = format_suffix_patterns(urlpatterns)