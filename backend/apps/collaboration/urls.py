from django.urls import path
from .views import CollaborationListView, CollaborationDetailView

urlpatterns = [
    path('projects/', CollaborationListView.as_view(), name='collaboration-list'),
    path('projects/<int:project_id>/', CollaborationDetailView.as_view(), name='collaboration-detail'),
]
