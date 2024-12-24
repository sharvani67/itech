from django.db import models


# MODELS
class Software(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='software_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name