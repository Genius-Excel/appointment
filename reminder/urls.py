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
    path('api/send-customer-apology', views.CreateLaundryClinicEmailApology.as_view(), name='send-customer-apology'),
    path('api/laundry-clinic-voice-call', views.CreateLaundryClinicVoiceCall.as_view(), name='laundry-clinic-voice-call'),
    path('api/create-english-customer-query', views.CreateEnglishSpeakingCustomersQuery.as_view(), name='english-customers'),
    path('api/create-spanish-customer-query', views.CreateSpanishSpeakingCustomersQuery.as_view(), name='spanish-customers'),
    path('api/update-spanish-customer-query/<int:spreadsheet_row>', views.UpdateSpanishSpeakingcustomersQuery.as_view(), name='update-spanish-customers'),
    
    path('login-user/', views.login_user, name='login-user'),
    path('logout-user/', views.logout_user, name='logout-user'),
    path('list-english-customers/', views.list_english_customers, name='list-english-customers'),
    path('list-spanish-customers/', views.list_spanish_customers, name='list-spanish-customers'),
    path('laundry-index', views.laundry_clinic_dashboard_test, name='laundry-index'),
    path('laundry-clinic-ai-calls/', views.get_all_laundry_clinic_calls, name='laundry-clinic-calls'),
    path('laundry-clinic-ai-call/detail/<int:id>/', views.get_laundry_clinic_ai_call_detail, name='ai-call-detail'),
    path('detail/<str:type>/<int:id>', views.get_detail_laundry_clinic_record, name='record-detail'),
    path('update-record-status/<str:type>/<int:id>/<str:action_type>/', views.update_query_status, name='update-record-status'),


    # Ceracerni
    path('send-email-ceracerni', views.CreateCeraniEmail.as_view(), name='send-email-ceracerni'),


    



]