from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),


    path('airport-info/', views.airport, name="airport-info"),
    path('airport-search/', views.airportSerch, name="airport-search"),
    # path('email_autocomplete/', views.email_autocomplete, name='email_autocomplete')
    path('airport-arrivals-info/', views.airportArrivalsInfo, name="airport-arrivals-info"),
    path('airport-departures-info/', views.airportDeparturesInfo, name="airport-departures-info"),
    path('arrivals-info-full-screen/', views.airportArrivalsInfoFullScreen, name="arrivals-info-full-screen"),
    path('departures-info-full-screen/', views.airportDeparturesInfoFullScreen, name="departures-info-full-screen"),
    path('flight-stats/', views.flightStats, name="flight-stats"),
    path('pilot-info/', views.pilotInfo, name="pilot-info"),
    path('passenger_inf_a/<str:flight>/', views.passenger_inf_a, name="passenger_inf_a"),
    path('passenger_inf_d/<str:flight>/', views.passenger_inf_d, name="passenger_inf_d"),

    path('control-panel/', views.contorlPanel, name="control-panel"),

    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('generate-code-and-print/', views.generateCodeAndPrint, name="generate-code-and-print")
]
