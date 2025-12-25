
# Create your models here.
from django.db import models
import uuid
import os

def video_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    # Generate unique filename
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('projects/videos/', filename)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    components = models.CharField(max_length=300, help_text="Comma-separated technologies")
    image = models.ImageField(upload_to='projects/images/', blank=True, null=True)
    video_url = models.URLField(
        blank=True,
        null=True,
        help_text="Paste YouTube / MP4 / hosted video link"
    )
    github_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def components_list(self):
        return [c.strip() for c in self.components.split(',')]

    def __str__(self):
        return self.title
