from django.db import models

class Snippet(models.Model):
    code = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')