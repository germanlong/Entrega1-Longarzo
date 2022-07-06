from django.db import models

# Create your models here.

class Blog(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return f"Mi nombre es {self.nombre}"