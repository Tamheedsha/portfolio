from django.db import models
from django.db.models.fields import CharField
from datetime import datetime

# Create your models here.
class Image(models.Model):
    alt=models.CharField(max_length=60)
    image=models.ImageField(default=None, upload_to="")
    original=models.ImageField(default=None, upload_to="")
    uploadTimeStamp=models.DateTimeField(default=datetime.now, editable=False)
    isHighlight=models.BooleanField(default=False);

    def __str__(self) -> str:
        return self.alt