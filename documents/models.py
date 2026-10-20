from django.db import models
from collection.models import Collections


# Create your models here.
class Document(models.Model):
    class Status(models.TextChoices):
        UPLOADED = "uploaded","uploaded"
        PROCESSING = "processing", "Processing"
        COMPLETED = "completed", "Completed"
        FAILED = "failed", "Failed"

    Collections=models.ForeignKey(Collections,
    on_delete=models.CASCADE , related_name="documents")
    
    title = models.CharField(max_length=255)

    file = models.FileField(
        upload_to="documents/%Y/%m/"
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.UPLOADED
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
         return self.title