from django.urls import path
from .views import peer_tutor_list

urlpatterns = [
    path('', peer_tutor_list, name='peer_tutor_list'),
]
