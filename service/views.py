from django.shortcuts import render

# Create your views here.
# service/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Or any template you wish to render
from django.shortcuts import render
from django.views.generic import TemplateView

# service/views.py
from django.views.generic import TemplateView

class HostelMapView(TemplateView):
    template_name = 'hostel_map.html'