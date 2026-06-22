from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Platform(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    rating = models.FloatField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    platform = models.ForeignKey(
        Platform,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    def __str__(self):
        return f'{self.name} ({self.year}) - {self.rating}/10'

