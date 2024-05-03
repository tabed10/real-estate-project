from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request=request, template_name='pages/index.html')

def about(request):
    return render(request=request, template_name='pages/about.html')
