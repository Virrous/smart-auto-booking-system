from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    city = models.CharField(max_length=100, choices=[
        ('Jhapa', 'Jhapa'),
        ('Ilam', 'Ilam'),
        ('Biratnagar', 'Biratnagar'),
    ])

    def __str__(self):
        return self.email
    
class Driver(models.Model):
    NEWYORK = 'New York'
    LOSANGELES = 'Los Angeles'
    CHICAGO = 'Chicago'

    TYPE_CHOICES = [
        (NEWYORK, 'New York'),
        (LOSANGELES, 'Los Angeles'),
        (CHICAGO, 'Chicago'),
    ]

    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.PositiveIntegerField()
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=280)
    city = models.CharField(max_length=20, choices=TYPE_CHOICES, default=NEWYORK)
    lisense_num = models.PositiveIntegerField()
    auto_number = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.fname +" "+ self.lname
