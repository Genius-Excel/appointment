from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('api/create-appointment/', views.CreateClientAppointment.as_view(), name='create-appointment'),
    path('api/craden-moore-client/', views.CreateCradenMooreClient.as_view(), name='craden-moore-client'),
    path('api/enish-create-booking/', views.CreateEnishBooking.as_view(), name='enish-creating-booking'),

    # STRIPE PATHS
    path('create-checkout-session/<int:amount>/', views.create_checkout_session, name='create_checkout_session'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('payment-cancelled/', views.payment_cancelled, name='payment_cancelled'),
    path('confirm-payment/<str:stripe_session_id>/', views.confirm_payment, name='confirm-payment'),

    # Laundry Clinic PATHS
    path('send-customer-apology', views.CreateLaundryClinicEmailApology.as_view(), name='send-customer-apology'),


]