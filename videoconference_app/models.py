from django.db import models
from django.contrib.auth.models import User
import uuid

class VideoConference(models.Model):
    title = models.CharField(max_length=255)
    room_id = models.CharField(max_length=100, default=uuid.uuid4, unique=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    is_public = models.BooleanField(default=True)
    allowed_users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title
