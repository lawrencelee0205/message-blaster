from django.db import models
from model_utils.models import TimeStampedModel, UUIDModel

# Create your models here.
class Message(TimeStampedModel, UUIDModel):
    message = models.TextField(blank=True)
    