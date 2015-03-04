from django.shortcuts import render
from .models import MicroService

def index(request):

    context = {"services": MicroService.objects.all()}
    return render(request, 'api/index.html', context)

