from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.utils import timezone

# Create your views here.
def home(request):
    return HttpResponse('<h1>page is working just fine</h1>')

def departments(request):
    return render()

def HomeMinistries(request):
    return render()

def about(request):
    return render()

def sermons(request):
    date_today = datetime.datetime.now().date()
    return render(request, 'website/index.html', {"date_today" : date_today})
