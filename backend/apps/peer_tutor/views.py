from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import PeerTutor
from .serializers import PeerTutorSerializer

@api_view(['GET', 'POST'])
def peer_tutor_list(request):
    if request.method == 'GET':
        # Fetch all tutors, ordered by `created_at` (most recent first)
        tutors = PeerTutor.objects.all().order_by('-created_at')
        serializer = PeerTutorSerializer(tutors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        # Deserialize the incoming data and validate
        serializer = PeerTutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the validated data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
