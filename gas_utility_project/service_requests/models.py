from django.db import models

class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ('installation', 'New Installation'),
        ('repair', 'Repair'),
        ('maintenance', 'Maintenance'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]

    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES)
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.customer_name} - {self.request_type} - {self.status}"