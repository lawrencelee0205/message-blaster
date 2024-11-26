from django.urls import path
from django.urls import include, path
from .views import request_phone_number, verify_code, send_message


urlpatterns = [
    path('request-phone/', request_phone_number, name='request_phone'),
    path('verify-code/', verify_code, name='verify_code'),
    path('send-message/', send_message, name='send_message'),
]
