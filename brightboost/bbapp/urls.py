import debug_toolbar
from django.urls import include, path
from . import views

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path('', views.home, name='home'),
    path('login', views.loginpage, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.user_logout, name='logout'),
]
