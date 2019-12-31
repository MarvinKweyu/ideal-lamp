from django.shortcuts import render
from django.http import HttpResponse
from .models import Solo
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'solos': Solo.objects.filter(instrument=request.GET.get('instrument', None) ) }
    return render(request,'solos/index.html', context)