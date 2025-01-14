from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Collaboration
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json

class CollaborationListView(View):
    def get(self, request):
        projects = Collaboration.objects.all().values('id', 'project_name', 'description', 'created_at')
        return JsonResponse(list(projects), safe=False)

class CollaborationDetailView(View):
    def get(self, request, project_id):
        project = Collaboration.objects.get(id=project_id)
        return JsonResponse({'id': project.id, 'project_name': project.project_name, 'description': project.description, 'created_at': project.created_at})

    @csrf_exempt
    def post(self, request, project_id=None):
        if project_id:
            # Edit an existing project (implement editing logic here)
            project = Collaboration.objects.get(id=project_id)
            data = json.loads(request.body)
            project.description = data.get('description', project.description)
            project.save()
            return JsonResponse({'id': project.id, 'description': project.description})
        else:
            # Create a new collaboration project
            data = json.loads(request.body)
            project = Collaboration.objects.create(
                project_name=data.get('project_name'),
                description=data.get('description')
            )
            return JsonResponse({'id': project.id, 'project_name': project.project_name, 'description': project.description}, status=201)
