from django.db import models

# Create your models here.


class AudioFile(models.Model):
    file_path = models.CharField(max_length=255)
    processed = models.BooleanField(default=False)
    similarity_score = models.FloatField(null=True, blank=True)
    transcription = models.TextField(blank=True, null=True)
