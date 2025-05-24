from django.test import TestCase
from .models import VideoConference
from django.utils import timezone
from datetime import timedelta

class VideoConferenceModelTest(TestCase):
    def test_string_representation(self):
        conference = VideoConference(title="Test Conference", start_time=timezone.now(), end_time=timezone.now() + timedelta(hours=1))
        self.assertEqual(str(conference), "Test Conference")

    def test_create_conference(self):
        start = timezone.now()
        end = start + timedelta(hours=1)
        conference = VideoConference.objects.create(title="Meeting", start_time=start, end_time=end)
        self.assertIsNotNone(conference.id)
        self.assertEqual(conference.title, "Meeting")
