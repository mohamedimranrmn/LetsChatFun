from django.contrib import admin
from .models import VideoConference

@admin.register(VideoConference)
class VideoConferenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'room_id', 'start_time', 'end_time', 'created_at')
    search_fields = ('title', 'room_id')
    list_filter = ('start_time', 'end_time', 'created_at')
