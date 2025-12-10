from django.urls import path
from . import frontend_views

urlpatterns = [
    path('', frontend_views.homepage),
    path('event/<int:id>/', frontend_views.event_detail),
    path('create-event/', frontend_views.create_event),
]
