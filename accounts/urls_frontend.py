from django.urls import path
from . import frontend_views

urlpatterns = [
    path('login/', frontend_views.login_page, name='login'),
    path('register/', frontend_views.register_page, name='register'),
    path('logout/', frontend_views.logout_user, name='logout'),
]
