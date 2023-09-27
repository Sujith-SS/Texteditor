from django.db import models

class SavedText(models.Model):
    font_family = models.CharField(max_length=250)
    font_size = models.CharField(max_length=250)
    content = models.TextField()
