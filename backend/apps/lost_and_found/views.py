from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import LostAndFound
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json

class LostAndFoundListView(View):
    def get(self, request):
        items = LostAndFound.objects.all().values('id', 'item_name', 'description', 'status', 'found_on', 'location')
        return JsonResponse(list(items), safe=False)

class LostAndFoundDetailView(View):
    def get(self, request, item_id):
        item = LostAndFound.objects.get(id=item_id)
        return JsonResponse({'id': item.id, 'item_name': item.item_name, 'description': item.description, 'status': item.status, 'found_on': item.found_on, 'location': item.location})

    @csrf_exempt
    def post(self, request, item_id=None):
        if item_id:
            # Edit an existing item (implement editing logic here)
            item = LostAndFound.objects.get(id=item_id)
            data = json.loads(request.body)
            item.status = data.get('status', item.status)
            item.save()
            return JsonResponse({'id': item.id, 'status': item.status})
        else:
            # Create a new lost and found item
            data = json.loads(request.body)
            item = LostAndFound.objects.create(
                item_name=data.get('item_name'),
                description=data.get('description'),
                status='lost',
                location=data.get('location')
            )
            return JsonResponse({'id': item.id, 'item_name': item.item_name, 'description': item.description, 'status': item.status, 'location': item.location}, status=201)
