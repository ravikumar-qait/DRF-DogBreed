from django.db import models
from django.db.models.deletion import Collector
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
BREED_CHOICES = (
    ("Tiny", "Tiny"),
    ("Small", "Small"),
    ("Medium", "Medium"),
    ("Large", "Large")
)


class Dogs(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey('Breed', null=True, on_delete=models.CASCADE)
    gender = models.CharField(null=True, blank=True, max_length=10)
    color = models.CharField(null=True, blank=True, max_length=20)
    favoritefood = models.CharField(null=True, blank=True, max_length=20)
    favoritetoy = models.CharField(null=True, max_length=20)

    def __str__(self):
        return self.name


class Breed(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(choices=BREED_CHOICES, max_length=100)
    friendliness = models.IntegerField(null=False,validators=[MinValueValidator(1), MaxValueValidator(5)])
    trainability = models.IntegerField(null=False,validators=[MinValueValidator(1), MaxValueValidator(5)])
    sheddingamount = models.IntegerField(null=False,validators=[MinValueValidator(1), MaxValueValidator(5)])
    exerciseneeds = models.IntegerField(null=False,validators=[MinValueValidator(1), MaxValueValidator(5)])


    def __str__(self):
        return self.name