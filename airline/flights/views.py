from django.shortcuts import render, redirect
from .models import Airport, Flight, Passenger

# Create your views here.

def index(request):
    flights = Flight.objects.all()
    return render(request, "flights/index.html", {
        "flights": flights
    })

def flight(request, id):
    f = Flight.objects.get(id=id)
    return render(request, "flights/flight.html", {
        "flight": f
    })

def add(request):
    airports = Airport.objects.all()

    if request.method == "POST":
        origin = Airport.objects.get(id=request.POST['origin'])
        destination = Airport.objects.get(id=request.POST['destination'])
        duration = request.POST['duration']
        seats = request.POST['seats']

        f = Flight(origin=origin, destination=destination, duration=duration, seats=seats)
        f.save()
        return redirect('index')
    return render(request, "flights/add.html", {
        "airports": airports
    })

def book(request, id):
    flight = Flight.objects.get(id=id)

    if flight.seats <= 0:
        return redirect('flight', id=flight.id)

    if request.method == "POST":
        fullname = request.POST["fullname"]
        email = request.POST["email"]
        passenger = Passenger(fullname=fullname, email=email)
        passenger.save()
        flight.seats -= 1
        flight.save()
        passenger.flights.add(flight)
        return redirect('flight', id=flight.id)

    return render(request, "flights/book.html", {
        "flight": flight
    })

def remove(request, flight_id, pass_id):
    flight = Flight.objects.get(id=flight_id)
    flight.seats += 1
    flight.save()
    passenger = Passenger.objects.get(id=pass_id)
    passenger.delete()
    
    return redirect('flight', id=flight_id)