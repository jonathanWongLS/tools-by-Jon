from django.shortcuts import render
from django.http import HttpResponse
from .models import StartTimeRange, EndTimeRange

# Create your views here.
def index(request):
    start_time_ranges = StartTimeRange.objects.all()
    end_time_ranges = EndTimeRange.objects.all()
    context = {'start_time_ranges': start_time_ranges, 'end_time_ranges': end_time_ranges}
    return render(request, 'finder.html', context)
