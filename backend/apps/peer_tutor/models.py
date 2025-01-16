# from django.db import models

# class PeerTutor(models.Model):
#     tutor_name = models.CharField(max_length=100)
#     subject = models.CharField(max_length=100)
#     description = models.TextField()
#     contact = models.CharField(max_length=100)
#     availability = models.DateTimeField()

#     def __str__(self):
#         return self.tutor_name

from django.db import models

class PeerTutor(models.Model):
    tutor_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    contact = models.CharField(max_length=100)
    availability = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation

    def __str__(self):
        return self.tutor_name
