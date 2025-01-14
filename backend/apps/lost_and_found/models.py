
# Create your models here.
from django.db import models

class LostAndFound(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    found_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('lost', 'Lost'), ('found', 'Found')], default='lost')
    location = models.CharField(max_length=100)
    user = models.CharField(max_length=100)  # Example: Add user field later to link to actual users

    def __str__(self):
        return self.item_name
