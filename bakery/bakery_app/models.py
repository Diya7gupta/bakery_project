from django.db import models

# Create your models here.
class InventoryItem(models.Model):
    # id = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.IntegerField()


class BakeryItem(models.Model):
    # id = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()

class BakeryItemInventoryItem(models.Model):
    bakeryItemId = models.CharField(max_length=50)
    inventoryItemId = models.CharField(max_length=50)
    inventoryItemQuantity = models.IntegerField()