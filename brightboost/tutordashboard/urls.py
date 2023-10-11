import debug_toolbar
from django.urls import include, path
from . import views

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path('dashboard', views.tutordashboard, name='tutordashboard'),
]
