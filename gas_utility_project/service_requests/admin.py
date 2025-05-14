from django.contrib import admin
from .models import ServiceRequest


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'request_type', 'status', 'submitted_at', 'resolved_at')
    list_filter = ('status', 'request_type')
    search_fields = ('customer_name', 'customer_email', 'details')
