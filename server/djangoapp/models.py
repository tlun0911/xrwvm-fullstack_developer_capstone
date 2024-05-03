# Uncomment the following imports before adding the Model code

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    domestic = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return self.name

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CHOICE_TYPE = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('TRUCK', 'Truck'),
        ('CROSSOVER', 'Crossover'),
        ('VAN', 'Van'),
    ]
    type = models.CharField(max_length=100, 
                        choices=CHOICE_TYPE, default='SEDAN')
    year = models.IntegerField(default=2023, 
                        validators=[MaxValueValidator(2023),
                        MinValueValidator(2015)])
    electric = models.BooleanField(default=False)
    used = models.BooleanField(default=False)
    miles = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name
