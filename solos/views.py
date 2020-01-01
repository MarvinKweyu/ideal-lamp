from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Solo

# Create your views here.
def index(request):
    context = {'solos': []}

    if request.GET.keys():
        solos_queryset = Solo.objects.all()

        if request.GET.get('instrument', None):
            solos_queryset = solos_queryset.filter(instrument=request.GET.get('instrument', None))


        if request.GET.get('artist', None):
            solos_queryset = solos_queryset.filter(artist=request.GET.get('artist', None))

        
        context['solos'] = solos_queryset
        
    return render(request,'solos/index.html', context)

# class ListSearchResult(ListView):
#     model = Solo
#     context_object_name = 'solos'
#     template_name = 'solos/index.html'

#     def get_queryset(self):
#         pass

class SoloDetailView(DetailView):
    pass