from django.shortcuts import render
from .models import Jobs

def home(request):
    jobs = Jobs.objects
    return render(request, 'jobs/index.html', {'jobs':jobs})