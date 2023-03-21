from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def algorithm():
    return ['9:00 AM - 10:00 AM', '10:00 AM - 11:00 AM', '11:00 AM - 12:00 PM']

def index(request):
    timeframes = algorithm()
    context = {'values': timeframes}
    return render(request, 'finder.html', context)
