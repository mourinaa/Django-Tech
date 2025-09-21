from django.db import models

class Module(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    installed = models.BooleanField(default=False)
    version = models.DecimalField(max_digits=3, decimal_places=1, default=1.0) 
    schema = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.name
