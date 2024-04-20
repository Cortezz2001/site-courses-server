
from django.urls import path
from courses_backend.auth_system.views import UserRegistration

urlpatterns = [
    path('authorization', UserRegistration)
]
