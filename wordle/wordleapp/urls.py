from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('process-item-lost/', views.process_item_lost, name='process_item_lost'),
    path('process-item-found/', views.process_item_found, name='process_item_found'),
    path('process-issue/', views.process_issue, name='process_issue'),
    path('process-comment/', views.process_comment, name='process_comment'),
    path('process-collaboration/', views.process_collaboration, name='process_collaboration'),
    path('lostandfound/', views.lost_and_found, name='lost_and_found'),
    path('issuecentral/', views.issue_central, name='issue_central'),
    path('collaboration/', views.collaboration, name='collaboration'),
    path('lostform/', views.lost_form, name='lost_form'),
    path('foundform/', views.found_form, name='found_form'),
    path('issueform/', views.issue_form, name='issue_form'),
    path('collaborationform/', views.collaboration_form, name='collaboration_form'),
    path('collaboration/<int:collaboration_id>/', views.collaboration_detail, name='collaboration_detail'),
    path('update_application_status/<int:application_id>/<str:status>/', views.update_application_status, name='update_application_status'),

]

