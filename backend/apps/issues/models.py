
# Create your models here.
from django.db import models

class Issue(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    reported_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('open', 'Open'), ('resolved', 'Resolved')], default='open')
    user = models.CharField(max_length=100)  # Example: Add user field later to link to actual users

    def __str__(self):
        return self.title
