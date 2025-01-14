from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Issue
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
import json

class IssueListView(View):
    def get(self, request):
        issues = Issue.objects.all().values('id', 'title', 'description', 'status', 'reported_at')
        return JsonResponse(list(issues), safe=False)

class IssueDetailView(View):
    def get(self, request, issue_id):
        try:
            issue = Issue.objects.get(id=issue_id)
            return JsonResponse({'id': issue.id, 'title': issue.title, 'description': issue.description, 'status': issue.status, 'reported_at': issue.reported_at})
        except ObjectDoesNotExist:
            return HttpResponseNotFound('Issue not found')

    @csrf_exempt
    def post(self, request, issue_id=None):
        if issue_id:
            # Edit an existing issue (implement editing logic here)
            issue = Issue.objects.get(id=issue_id)
            data = json.loads(request.body)
            issue.status = data.get('status', issue.status)
            issue.save()
            return JsonResponse({'id': issue.id, 'status': issue.status})
        else:
            # Create a new issue
            data = json.loads(request.body)
            issue = Issue.objects.create(
                title=data.get('title'),
                description=data.get('description'),
                status='open'
            )
            return JsonResponse({'id': issue.id, 'title': issue.title, 'description': issue.description, 'status': issue.status}, status=201)
