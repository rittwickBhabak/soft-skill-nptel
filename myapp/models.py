from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    video_id = models.CharField(max_length=30)
    is_completed = models.BooleanField(default=False)

    detail = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
