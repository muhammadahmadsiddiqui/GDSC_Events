from django.shortcuts import render, redirect
from .models import Event, Registration
from .forms import RegistrationForm

def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

def home(request):
    return render(request, 'base.html', {})



def register(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = event
            registration.save()
            return redirect('events')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'event': event, 'form': form})
