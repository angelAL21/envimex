from django.db import models

# model de información.
class Info(models.Model):
    municipio = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    colonia = models.CharField(max_length=50)
    cp = models.CharField(max_length=5)
    
    def __str__(self):
        return self.municipio