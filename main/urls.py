from django.urls import path, include
from . import views
from rest_framework import routers
from .api_views import AppointmentViewSet

router = routers.DefaultRouter()
router.register(r'appointments', AppointmentViewSet, basename='appointments')

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('skills-education/', views.skills_education, name='skills_education'),
    path('contact/', views.contact, name='contact'),
    path('scheduler/', views.scheduler, name='scheduler'),
    path('appointment-success/', views.appointment_success, name='appointment_success'),
    path('appointments/json/', views.appointment_events, name='appointment_events'),


]
