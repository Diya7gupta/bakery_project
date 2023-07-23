from .models import BakeryItem
from .models import InventoryItem

class BakeryItemRepository:
    def getBakeryItem(self, id):
        try:
            return BakeryItem.objects.get(id=id)
        except BakeryItem.DoesNotExist:
            return None

    def createBakeryItem(self, name, quantity):
        bakery_item = BakeryItem(name=name, quantity=quantity)
        bakery_item.save()
        return bakery_item

    def getAllBakeryItems(self):
        return BakeryItem.objects.all()

    def getBakeryItemByName(self, name):
        try:
            return BakeryItem.objects.get(name=name)
        except BakeryItem.DoesNotExist:
            return None
    
    # def updateBakeryItemQuantity(self, id, new_quantity):
    #     try:
    #         bakery_item = BakeryItem.objects.get(id=id)
    #         bakery_item.quantity = new_quantity
    #         bakery_item.save()
    #         return bakery_item
    #     except BakeryItem.DoesNotExist:
    #         return None

     
class InventoryItemRepository:

    def createInventoryItem(self, name, quantity, price):
        # todo - add unique contraint on name
        inventory_item = InventoryItem(name=name, quantity=quantity, price=price)
        inventory_item.save()
        return inventory_item
    
    def getAllInventoryItems(self):
        return InventoryItem.objects.all()

    def getInventoryItemById(self, id):
        try:
            return InventoryItem.objects.get(id=id)
        except InventoryItem.DoesNotExist:
            return None

    def updateInventoryItem(self, id, name=None, quantity=None, price=None):
        try:
            inventory_item = InventoryItem.objects.get(id=id)

            # Update the fields if provided
            if name is not None:
                inventory_item.name = name
            if quantity is not None:
                inventory_item.quantity = quantity
            if price is not None:
                inventory_item.price = price

            inventory_item.save()
            return inventory_item
        except InventoryItem.DoesNotExist:
            return None