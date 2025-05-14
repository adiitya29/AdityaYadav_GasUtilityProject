from django.urls import path
from . import views
from .views import account_info_view

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('submitted/', views.request_submitted, name='request_submitted'),
    path('track/', views.track_request, name='track_request'),
    path('account/', account_info_view, name='account_info'),
    path('admin-report/', views.admin_report_view, name='admin_report'),
]