from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event

def homepage(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})


def event_detail(request, id):
    event = Event.objects.get(id=id)
    return render(request, 'event_detail.html', {'event': event})


@login_required(login_url="/register/")
def create_event(request):
    if request.method == "POST":
        Event.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            date=request.POST["date"],
            start_time=request.POST["start_time"],
            end_time=request.POST["end_time"],
            location=request.POST["location"],
            organizer=request.user
        )
        return redirect("/")
    return render(request, "event_create.html")


