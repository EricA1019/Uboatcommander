init python:
    import math

    class Item:
        def __init__(self, name, cost):
            self.name = name
            self.cost = cost

    class Inventory:
        def __init__(self, requisition_points=5000):
            self.requisition_points = requisition_points
            self.items = []

        def buy(self, item, quantity=1):
            total_cost = item.cost * quantity

            # Check if we have enough points for the full quantity
            if self.requisition_points >= total_cost:
                current_count = sum(1 for i in self.items if i.name == item.name)
                max_capacity = {
                    "Torpedo": 10,
                    "Deck Gun Ammo": 20,
                    "Fuel": 15
                }.get(item.name, float("inf"))

                purchasable_quantity = min(quantity, max_capacity - current_count)
                if purchasable_quantity > 0:
                    cost_to_charge = item.cost * purchasable_quantity
                    self.requisition_points -= cost_to_charge
                    self.items.extend([item] * purchasable_quantity)
                    return purchasable_quantity
            # If we can’t afford it or capacity is 0, return 0
            return 0

        def earn(self, amount):
            self.requisition_points += amount

        def has_item(self, item_name):
            return any(item.name == item_name for item in self.items)

        def refill_all(self, items):
            total_cost = sum(item.cost for item in items)
            if self.requisition_points >= total_cost:
                self.requisition_points -= total_cost
                self.items.extend(items)

label premission:

    python:
        inventory = Inventory()
        player_submarine = Uboat(inventory, name=submarine_name.strip())  # Assuming Uboat is defined
        torpedo = Item("Torpedo", 50)
        deck_gun_ammo = Item("Deck Gun Ammo", 10)
        fuel = Item("Fuel", 5)

    $ rp = inventory.requisition_points
    "Welcome to the requisition depot. You have [rp] RP."

    jump preshop

label preshop:
    $ torpedocost = torpedo.cost
    $ deckgunammocost = deck_gun_ammo.cost
    $ fuelcost = fuel.cost
    $ total_cost = torpedocost + deckgunammocost + fuelcost
    jump shop2

label shop2:
    menu:
        "I approach the requisition officer."
        "Buy torpedoes ([torpedocost] RP each)":
            python:
                purchased = inventory.buy(torpedo)
            if purchased > 0:
                "You bought [purchased] torpedoes! You now have [inventory.requisition_points] RP left."
            else:
                "You couldn't buy any torpedoes. (Either you're at max capacity or short on RP.)"
            jump shop2

        "Buy deck gun ammo ([deckgunammocost] RP each)":
            python:
                purchased = inventory.buy(deck_gun_ammo)
            if purchased > 0:
                "You bought [purchased] deck gun ammo! You now have [inventory.requisition_points] RP left."
            else:
                "You couldn't buy any deck gun ammo. (Either you're at max capacity or short on RP.)"
            jump shop2

        "Buy fuel ([fuelcost] RP each)":
            python:
                purchased = inventory.buy(fuel)
            if purchased > 0:
                "You bought [purchased] fuel! You now have [inventory.requisition_points] RP left."
            else:
                "You couldn't buy any fuel. (Either you're at max capacity or short on RP.)"
            jump shop2

        "Refill all supplies for [total_cost] RP." if inventory.requisition_points >= total_cost:
            python:
                inventory.refill_all([torpedo, deck_gun_ammo, fuel])
            "All supplies refilled! You now have [inventory.requisition_points] RP left."
            jump shop2

        "Leave the shop.":
            menu:
                "Would you like to purchase something else?"
                "Yes":
                    jump shop2
                "No":
                    jump game_continues

label game_continues:
    python:
        torpedo_count = sum(1 for item in inventory.items if item.name == "Torpedo")
        deckgunammo_count = sum(1 for item in inventory.items if item.name == "Deck Gun Ammo")
        fuel_count = sum(1 for item in inventory.items if item.name == "Fuel")
    "I head back to my submarine with my supplies."
    $ current_rp = inventory.requisition_points
    "I have [current_rp] RP left with [torpedo_count] torpedoes, [deckgunammo_count] deck gun ammo, and [fuel_count] fuel."
    
    jump begin_patrol
