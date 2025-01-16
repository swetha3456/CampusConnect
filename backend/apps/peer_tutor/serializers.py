from rest_framework import serializers
from .models import PeerTutor

class PeerTutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeerTutor
        fields = '__all__'
