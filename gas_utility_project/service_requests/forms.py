from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['customer_name', 'customer_email', 'request_type', 'description', 'attachment']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }



class TrackRequestForm(forms.Form):
    customer_email = forms.EmailField(label="Enter your email")