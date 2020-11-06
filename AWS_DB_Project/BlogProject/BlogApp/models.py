from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    written_by = models.CharField(max_length=50)
