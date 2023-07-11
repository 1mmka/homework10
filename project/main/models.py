from django.db import models

# Create your models here.
class Film(models.Model):
    name = models.CharField(max_length=64)
    genre = models.CharField(max_length=32)
    rating = models.FloatField()
    year = models.IntegerField()

    def __str__(self):
        return self.name + " " + str(self.pk)

class Newspapers(models.Model):
    name = models.CharField(max_length=64)
    publisher = models.CharField(max_length=128)
    language = models.CharField(max_length=32)
    genre = models.CharField(max_length=32)

    def __str__(self):
        return self.name + " " + str(self.pk)