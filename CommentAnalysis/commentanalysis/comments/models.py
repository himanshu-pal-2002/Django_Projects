from django.db import models
from django.utils import timezone
import datetime

# Create Models for Comments:

class Comment(models.Model):

    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


