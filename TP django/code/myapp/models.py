from django.db import models

class Feature(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.titre