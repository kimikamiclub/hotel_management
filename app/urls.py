from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home_page, name='home'),
    path('contact/', views.contact, name='contact'),
    path('rooms/', views.rooms_list, name='rooms'),
    path('reservations/', views.reservations_list, name="reservations"),
    path('reservations/view', views.view_reservations, name="view_reservations"),
    path('reservations/create', views.make_reservation, name= "make_reservation")
]
