"""
URL configuration for campusconnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/issues/', include('apps.issues.urls')),  # Use distinct base paths
    path('api/lost_and_found/', include('apps.lost_and_found.urls')),
    path('api/collaboration/', include('apps.collaboration.urls')),
    path('api/peer_tutor/', include('apps.peer_tutor.urls')),  # Correct base path
    path('', include('apps.home.urls')),
    path('api/users/', include('users.urls')),
]

