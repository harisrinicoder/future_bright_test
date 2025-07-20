# courses/models.py

from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='courses/images/', blank=True, null=True)  # <-- Add this line

    def __str__(self):
        return self.title
