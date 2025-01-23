label combat:
    # Load player's submarine and enemy ship
    python:
        # Initialize the player's submarine using the previously selected name
        player_submarine = Uboat(inventory, name=submarine_name.strip())
        enemy_ship = EnemyShip(name="Supply Ship", health=100, evasion=20, armed=True)
        combat_active = True  # Flag to control the combat loop

    # Notify the player of an enemy encounter
    $ message = "You have encountered an enemy [enemy_ship.name]. Prepare for battle!"
    nar "[message]"

    while combat_active:
        python:
            # Define the combat options with dynamic inventory values
            torpedo_count = sum(1 for item in inventory.items if item.name == "Torpedo")
            deck_gun_count = sum(1 for item in inventory.items if item.name == "Deck Gun Ammo")

            choices = [
                ("Fire a torpedo (" + str(torpedo_count) + " left)", "torpedo"),
                ("Fire deck gun (" + str(deck_gun_count) + " rounds left)", "deck_gun"),
                ("Attempt to evade", "evade"),
                ("Retreat", "retreat")
            ]

        # Display a menu for the player’s action
        $ choice = renpy.display_menu(choices)

        if choice == "torpedo":
            if inventory.has_item("Torpedo"):
                # Attack the enemy ship with a torpedo
                $ result = player_submarine.attack(enemy_ship, "torpedo")
                $ message = "[result]"
                nar "[message]"
                if enemy_ship.health <= 0:
                    $ message = "[enemy_ship.name] has been sunk!"
                    nar "[message]"
                    $ combat_active = False
                    jump combat_victory
            else:
                nar "You're out of torpedoes!"

        elif choice == "deck_gun":
            if inventory.has_item("Deck Gun Ammo"):
                # Attack the enemy ship with the deck gun
                $ result = player_submarine.attack(enemy_ship, "deck_gun")
                $ message = "[result]"
                nar "[message]"
                if enemy_ship.health <= 0:
                    $ message = "[enemy_ship.name] has been sunk!"
                    nar "[message]"
                    $ combat_active = False
                    jump combat_victory
            else:
                nar "You're out of deck gun ammo!"

        elif choice == "evade":
            # Attempt to evade the enemy attack
            $ evaded = player_submarine.evade(enemy_ship)
            if evaded:
                nar "You successfully evaded the enemy!"
                $ combat_active = False
                jump combat_escape
            else:
                nar "You failed to evade, prepare for an incoming attack."

        elif choice == "retreat":
            # Player chooses to retreat from combat
            nar "You decided to retreat from battle."
            $ combat_active = False
            jump combat_escape

        # Enemy counterattack if still in combat
        if enemy_ship.armed and combat_active:
            $ enemy_attack = enemy_ship.retaliate(player_submarine)
            $ message = "[enemy_attack]"
            nar "[message]"
            if player_submarine.hull_integrity <= 0:
                nar "Your submarine has been destroyed!"
                jump combat_defeat

    return

label combat_victory:
    # Victory message and transition to next part of the game
    $ inventory.earn(50)  # Reward the player with requisition points
    nar "You have successfully destroyed the enemy ship and can return to base."
    return

label combat_defeat:
    # Defeat message and transition to next part of the game
    $ inventory.items.clear()  # Clear inventory on defeat
    nar "Your submarine has been lost. Mission failed."
    return

label combat_escape:
    # Escape message and transition to the next part of the game
    nar "You managed to retreat safely. Time to regroup."
    return
