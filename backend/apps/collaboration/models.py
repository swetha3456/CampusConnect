from django.db import models

# Create your models here.
class Collaboration(models.Model):
    project_name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField('auth.User')  # Example: Link to Django's built-in User model later

    def __str__(self):
        return self.project_name
