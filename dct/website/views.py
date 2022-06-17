from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>page is working just fine</h1>')

def sermons(request):
    return render(request, 'website/index.html')