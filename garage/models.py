from django.db import models

class Vehicle(models.Model):
    #  choices for the vehicle type
    TYPE_CHOICES = [
        ('CAR', 'Car'),
        ('MOTO', 'Motorcycle'),
    ]

    make = models.CharField(max_length=50, help_text="e.g., Subaru, Kawasaki")
    model_name = models.CharField(max_length=50, help_text="e.g., WRX STI, Ninja H2R")
    vehicle_type = models.CharField(max_length=4, choices=TYPE_CHOICES, default='CAR')
    year = models.IntegerField()
    engine_specs = models.CharField(max_length=150, help_text="e.g., 2.5L Turbocharged Boxer, 998cc Supercharged Inline-4")
    horsepower = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True, help_text="Any extra notes or modifications.")
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Display in admin panel 
        return f"{self.year} {self.make} {self.model_name}"