init python:
    import random

    class Uboat:
        def __init__(self, inventory, name="Unnamed Submarine", hull_integrity=100, speed=20, evasion=30):
            if inventory is None:
                raise ValueError("Inventory must be provided to ensure consistent state.")
            
            self.inventory = inventory
            self.name = name
            self.hull_integrity = hull_integrity
            self.speed = speed
            self.evasion = evasion

            # Additional stats
            self.morale = 5
            self.sonar_level = 1
            self.stealth_level = 1
            self.firepower = 1
        
        def attack(self, enemy, weapon="torpedo"):
            """
            Attacks the given 'enemy' ship using the specified 'weapon'.
            This method removes exactly one piece of ammo (torpedo or deck gun),
            calculates the hit chance, and returns a string describing the result.
            """
            if weapon == "torpedo" and self.inventory.has_item("Torpedo"):
                # Remove exactly 1 torpedo from inventory
                for i, item in enumerate(self.inventory.items):
                    if item.name == "Torpedo":
                        del self.inventory.items[i]
                        break

                hit_chance = 60 + (self.sonar_level * 5)
                if random.randint(1, 100) <= hit_chance:
                    damage = 30 * self.firepower
                    result = enemy.take_damage(damage)
                    return f"Direct hit! Enemy took {damage} damage. {result}"
                else:
                    return "Missed the shot!"

            elif weapon == "deck_gun" and self.inventory.has_item("Deck Gun Ammo"):
                # Remove exactly 1 deck gun ammo from inventory
                for i, item in enumerate(self.inventory.items):
                    if item.name == "Deck Gun Ammo":
                        del self.inventory.items[i]
                        break

                hit_chance = 40 + (self.firepower * 10)
                if random.randint(1, 100) <= hit_chance:
                    damage = 10 * self.firepower
                    result = enemy.take_damage(damage)
                    return f"Deck gun hit! Enemy took {damage} damage. {result}"
                else:
                    return "Deck gun missed!"

            else:
                return "No ammunition left for that weapon!"

        def evade(self, enemy):
            """
            Attempts to evade an attack from 'enemy'.
            Returns True if evasion succeeds, False if it fails.
            Make sure to call this as 'player_submarine.evade(enemy_ship)' in the script.
            """
            evade_chance = 50 + (self.stealth_level * 10) - (enemy.evasion * 2)
            return random.randint(1, 100) <= evade_chance

        def take_damage(self, damage):
            """
            Decreases the sub's hull integrity by 'damage'. 
            Returns a string indicating current hull status or destruction.
            """
            self.hull_integrity = max(0, self.hull_integrity - damage)
            if self.hull_integrity <= 0:
                return "Submarine has been destroyed!"

            # Use Ren'Py notify to display updated hull integrity
            renpy.notify(f"Hull integrity now at {self.hull_integrity}%")
            return f"Hull integrity now at {self.hull_integrity}%"

    class EnemyShip:
        def __init__(self, name="Supply Ship", health=100, evasion=20, armed=False):
            """
            Represents an enemy ship with certain attributes.
            'armed' determines whether it can retaliate.
            """
            self.name = name
            self.health = health
            self.evasion = evasion
            self.armed = armed
        
        def take_damage(self, damage):
            """
            Decreases the ship's health by 'damage'. 
            Returns a string describing the new state or if it's sunk.
            """
            self.health = max(0, self.health - damage)
            if self.health <= 0:
                sunk_msg = f"{self.name} has been sunk!"
                renpy.notify(sunk_msg)
                return sunk_msg
            
            renpy.notify(f"{self.name} health is now at {self.health}%")
            return f"{self.name} health is now at {self.health}%"

        def retaliate(self, uboat):
            """
            The enemy attempts to detect and retaliate against 'uboat'.
            If detection is successful, deals random damage.
            Otherwise returns a string indicating failed detection.
            """
            if self.armed:
                # Example detection formula. Adjust as desired for your game:
                detection_threshold = (uboat.sonar_level * 5) - (uboat.stealth_level * 10)
                detection_roll = random.randint(1, 100)

                if detection_roll > detection_threshold:
                    damage = random.randint(10, 30)
                    return uboat.take_damage(damage)

            return f"{self.name} failed to detect your submarine."
