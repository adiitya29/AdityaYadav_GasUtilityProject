from django.shortcuts import render, redirect
from .forms import ServiceRequestForm,TrackRequestForm
from django.http import HttpResponse
from .models import ServiceRequest

from django.db.models import Count, Q


def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('request_submitted')
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/submit_request.html', {'form': form})


def request_submitted(request):
    return HttpResponse("your service request has been submitted successfully")


def track_request(request):
    requests = None
    if request.method == 'POST':
        form = TrackRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['customer_email']
            requests = ServiceRequest.objects.filter(customer_email=email)
    else:
        form = TrackRequestForm()
    
    return render(request, 'service_requests/track_request.html', {
        'form': form,
        'requests': requests
    })

def account_info_view(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        requests = ServiceRequest.objects.filter(customer_email=email)
        
        if requests.exists():
            name = requests.first().customer_name
            total = requests.count()
            pending = requests.filter(status='Pending').count()
            resolved = requests.filter(status='Resolved').count()
            
            context.update({
                'name': name,
                'email': email,
                'requests': requests,
                'total': total,
                'pending': pending,
                'resolved': resolved,
            })
        else:
            context['error'] = "No requests found for this email."
    return render(request, 'account_info.html', context)

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_report_view(request):
    total = ServiceRequest.objects.count()
    pending = ServiceRequest.objects.filter(status='Pending').count()
    resolved = ServiceRequest.objects.filter(status='Resolved').count()

    return render(request, 'admin_report.html', {
        'total': total,
        'pending': pending,
        'resolved': resolved
    })
