from django.db import models

class File(models.Model):
    file = models.ImageField(blank=False, null=False)
    def __str__(self):
        return self.file.name



    