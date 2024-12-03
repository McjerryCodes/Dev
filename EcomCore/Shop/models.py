from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Concept(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    room = models.ForeignKey(Room, related_name="products", on_delete=models.SET_NULL, null=True)
    concept = models.ForeignKey(Concept, related_name="products", on_delete=models.SET_NULL, null=True)
    image = models.URLField(upload_to='products/')
    
    def __str__(self):
        return self.name
