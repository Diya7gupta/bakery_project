from . import repositories

class InventoryService:
    def __init__(self):
        self.repository = repositories.InventoryItemRepository()

    def createInventoryItem(self, name, quantity, price):
        self.repository.createInventoryItem(name, quantity, price)

    def getInventoryItem(self, id):
        return self.repository.getInventoryItemById(id=id)
    
    def updateInventoryItem(self, id, new_name, new_quantity, new_price):
        self.repository.updateInventoryItem(id, new_name, new_quantity, new_price)
    
    def searchInventoryItemByPrefix(self, prefix):
        all_inventory_items = self.repository.getAllInventoryItems()
        matching_items = [item for item in all_inventory_items if item.name.startswith(prefix)]
        return matching_items


class BakeryService:
    def __init__(self):
        self.repository = repositories.BakeryItemRepository()
        self.inventoryService = InventoryService()
    
    def checkIfIngredientsPresent(self, ingredients, bakery_item_quantity):
        for ingredient in ingredients:
            ingredient_id = ingredient['id']
            ingredient_quantity = bakery_item_quantity * ingredient['quantity']

            ingredient_from_inventory = self.inventoryService.getInventoryItem(ingredient_id)
            if ingredient_from_inventory.quantity < ingredient_quantity:
                raise Exception('Insufficient inventory')
    
    def reduceIngredientsQuantity(self, ingredients, bakery_item_quantity):
        for ingredient in ingredients:
            ingredient_id = ingredient['id']
            ingredient_quantity = bakery_item_quantity * ingredient['quantity']

            ingredient_from_inventory = self.inventoryService.getInventoryItem(ingredient_id)

            self.inventoryService.updateInventoryItem(
                ingredient_from_inventory.id, 
                ingredient_from_inventory.name, 
                ingredient_from_inventory.quantity - ingredient_quantity,
                ingredient_from_inventory.price
            )
            
    def createBakeryItem(self, create_bakery_item_reqeust):
        name = create_bakery_item_reqeust['name']
        quantity = create_bakery_item_reqeust['quantity']
        ingredients = create_bakery_item_reqeust['ingredients']

        self.checkIfIngredientsPresent(ingredients, quantity)
        self.reduceIngredientsQuantity(ingredients, quantity)

        self.repository.createBakeryItem(name, quantity)

    def searchBakeryItemByPrefix(self, prefix):
        all_bakery_item = self.repository.getAllBakeryItems()
        matching_items = [item for item in all_bakery_item if item.name.startswith(prefix)]
        return matching_items