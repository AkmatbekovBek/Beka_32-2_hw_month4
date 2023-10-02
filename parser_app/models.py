from django.db import models

class HdRezkaFilm(models.Model):
    title_name = models.CharField(max_length=300, null=True)
    title_url = models.CharField(max_length=300, null=True)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title_name