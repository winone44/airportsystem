from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Airport, Passengers, PlaneFlights, User, Pilot
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# from .models import model

# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exits')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            user.is_online = True
            user.save()
            if user.is_staff is True:
                return redirect('control-panel')
            else:
                return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exist')

    return render(request, 'base/login.html')


def logoutUser(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def home(request):
    return render(request, 'base/home.html')


@login_required(login_url='login')
def airportSerch(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    airport_request = Airport.objects.filter(name__icontains=q)[0:10]
    return render(request, 'base/airport_search.html', {'airport_request': airport_request})


@login_required(login_url='login')
def airport(request):
    id_airport = request.GET.get("id")
    if id_airport == None:
        return redirect('airport-search')
    airport_data = Airport.objects.get(id=id_airport)
    context = {'airport_data': airport_data}
    return render(request, 'base/airport_info.html', context)


# def email_autocomplete(request):
#     if request.GET.get('q'):
#         q = request.GET['q']
#         data = model.objects.using('legacy').filter(email__startswith=q).values_list('email', flat=True)
#         json = list(data)
#         return JsonResponse(json, safe=False)
#     else:
#         HttpResponse("No cookies")

@staff_member_required
def flightStats(request):
    fly_id = request.GET.get("flyId")
    if fly_id is None:
        return redirect(request.META['HTTP_REFERER'])
    pilots = Pilot.objects.filter(planeflights__flight=fly_id)
    flights = PlaneFlights.objects.filter(flight=fly_id)
    context = {'pilots': pilots, 'flights': flights}
    return render(request, 'base/flight_stats.html', context)


@login_required(login_url='login')
def airportArrivalsInfo(request):
    flights = PlaneFlights.objects.filter(to_airport__name__startswith='Rzeszów-Jasionka Airport')
    context = {'flights': flights}
    return render(request, 'base/airport_arrivals_info.html', context)


@login_required(login_url='login')
def airportDeparturesInfo(request):
    flights = PlaneFlights.objects.filter(from_airport__name__startswith='Rzeszów-Jasionka Airport')
    context = {'flights': flights}
    return render(request, 'base/airport_departures_info.html', context)


@login_required(login_url='login')
def passenger_inf_a(request, flight):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    passenger_data = Passengers.objects.filter(
        (
                Q(first_name__icontains=q) |
                Q(last_name__icontains=q)
        ) &
        Q(flight__flight__startswith=flight)
    )[0:10]
    context = {'passenger_data': passenger_data, 'flight': flight}
    return render(request, 'base/passenger_info_a.html', context)

    # q = request.GET.get('q') if request.GET.get('q') != None else ''
    # airport_request = Airport.objects.filter(name__icontains=q)[0:10]
    # return render(request, 'base/airport_search.html', {'airport_request': airport_request})


@login_required(login_url='login')
def passenger_inf_d(request, flight):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    passenger_data = Passengers.objects.filter(
        (
                Q(first_name__icontains=q) |
                Q(last_name__icontains=q)
        ) &
        Q(flight__flight__startswith=flight)
    )[0:10]
    context = {'passenger_data': passenger_data}
    return render(request, 'base/passenger_info_d.html', context)


@login_required(login_url='login')
def generateCodeAndPrint(request):
    id_passenger = request.GET.get("id")
    if id_passenger == None:
        return redirect(request.META['HTTP_REFERER'])
    passenger = Passengers.objects.get(id=id_passenger)
    if passenger.baggage_number != None:
        return redirect(request.META['HTTP_REFERER'])
    phone_number_without = passenger.phone_number.lstrip('+')
    phone_number_without = phone_number_without.lstrip(' ')
    passenger.baggage_number = ''.join(['ID', str(passenger.id), 'TEL', phone_number_without])
    passenger.save()
    context = {'passenger': passenger, 'phone_number_without': phone_number_without}
    return render(request, 'base/generate_code_and_print.html', context)


def airportArrivalsInfoFullScreen(request):
    flights = PlaneFlights.objects.filter(to_airport__name__startswith='Rzeszów-Jasionka Airport')
    context = {'flights': flights}
    return render(request, 'base/boardarrivals.html', context)


def airportDeparturesInfoFullScreen(request):
    flights = PlaneFlights.objects.filter(from_airport__name__startswith='Rzeszów-Jasionka Airport')
    context = {'flights': flights}
    return render(request, 'base/boarddepartures.html', context)


@staff_member_required
def contorlPanel(request):
    return render(request, 'base/controlpanel.html')

@staff_member_required
def pilotInfo(request):
    get_pilot_id = request.GET.get("pilotId")
    if get_pilot_id is None:
        return redirect(request.META['HTTP_REFERER'])
    pilots = Pilot.objects.filter(id=get_pilot_id)
    context = {'pilots': pilots}
    return render(request, 'base/pilot-info.html', context)

