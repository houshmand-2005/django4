from django.db import models

# Create your models here.
class room(models.Model):
    # host = models.CharField(max_length=)
    # topics =
    name = models.CharField(max_length=200)
    deprecation = models.TextField(null=True, blank=True)
    # participants =
    updates = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
        