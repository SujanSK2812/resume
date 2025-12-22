
# Create your models here.
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    components = models.CharField(max_length=300, help_text="Comma-separated technologies")
    
    video = models.FileField(upload_to='projects/videos/', blank=True, null=True)  # Video upload
    github_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def components_list(self):
        return [c.strip() for c in self.components.split(',')]

    def __str__(self):
        return self.title

