from django.urls import path
from .views import LostAndFoundListView, LostAndFoundDetailView

urlpatterns = [
    path('items/', LostAndFoundListView.as_view(), name='lost-and-found-list'),
    path('items/<int:item_id>/', LostAndFoundDetailView.as_view(), name='lost-and-found-detail'),
]
