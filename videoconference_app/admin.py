from django.contrib import admin
from .models import VideoConference

@admin.register(VideoConference)
class VideoConferenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'created_at')

