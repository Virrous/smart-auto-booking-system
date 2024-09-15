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
