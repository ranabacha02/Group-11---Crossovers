from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect
from .filters import ShopFilter
from .models import ShopItem
import calendar
from calendar import HTMLCalendar
from datetime import datetime 
from .forms import EventForm

# Create your views here.
def HomePage(request):
    return HttpResponse('HomePage')

def shop(request):
    return HttpResponse('shop')

def ticket(request):
    return HttpResponse('ticket')

def shop_list(request):
    f = ShopFilter(request.GET, queryset=ShopItem.objects.all())
    return render(request, 'shop/filter.html', {'filter': f})

def schedule(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    # Convert month from name to number
    month = month.title()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # Create calendar
    cal = HTMLCalendar().formatmonth(year, month_number)

    # Get current year
    now = datetime.now() 
    current_year = now.year

    # Get current time
    time = now.strftime('%I:%M %p')

    return render(request, 'schedule/schedule.html', {
        'year': year,
        'month': month,
        'cal': cal,
        'current_year': current_year,
        'time': time,
    })

def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'schedule/add_event.html', {'form':form, 'submitted':submitted})

def edit_event(request, event_id):
    event = Event.objects.get(pk=venue_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list_events')

    return render(request, 'events/edit_event.html',
        {'event': event,
        'form':form})
