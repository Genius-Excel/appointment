from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('api/create-appointment/', views.CreateClientAppointment.as_view(), name='create-appointment'),
]