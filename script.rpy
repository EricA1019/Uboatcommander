# This is a basic Ren'Py script template for a submarine game. It includes labels for setting up the game, starting a patrol, and handling combat encounters. The script uses Ren'Py's built-in features for dialogue, menus, and transitions, as well as custom Python classes for managing the player's submarine, enemy ships, and inventory.
label start:
    # Fade in from black.
    scene black with dissolve
    nar "In the year 937 ADW, the Federation of Free States stands on the brink of a new conflict..."

    # Optional background image (if you have one).
    # show background port_day
    # with fade

    nar "At the bustling naval port of Carina, steam cranes hiss and clank. 
        Shipwrights put the finishing touches on the Federation's newest submarine—a vessel that may tilt the balance of war."

    # Transition to a conversation with Admiral Beckett.
    adm "Ah, Captain. Glad you’re here. We’ve been anxiously awaiting your arrival."

    cpt "Admiral Beckett. I came as soon as I received the orders."

    adm "I’m sure you’ve heard the rumors: Tiberium convoys have been sighted in the Polarian Sea. 
        High Command wants us to intercept their supply lines before they reach our shores."

    menu:
        "How should I respond?"
        "Understood, sir. We won't let you down.":
            cpt "Understood, sir. We won't let you down."
        "That sounds like a challenge. We're ready.":
            cpt "That sounds like a challenge. We're ready."

    adm "That’s why we’ve commissioned a new boat for you—a next-generation diesel-electric sub 
        with improved sonar and extended fuel capacity. She’s a beauty, though untested."

    # === ASK THE PLAYER TO NAME THEIR SUBMARINE ===
    $ submarine_name = renpy.input("Enter the name of your new submarine:", length=30)
    # .strip() to remove any leading/trailing spaces
    $ submarine_name = submarine_name.strip()

    # If the player leaves it blank, give a default name
    if not submarine_name:
        $ submarine_name = "Wolfhead"

    adm "Excellent choice, Captain. We'll register her as the [submarine_name]."

    # Show a short "naming ceremony" moment
    nar "A small crowd of dockworkers and officers applaud as you break a ceremonial bottle 
        against the hull, naming the vessel officially."

    adm "Now, let’s discuss your first patrol. We have intelligence that a Tiberium supply convoy 
        is scheduled to pass through the Polarian Sea within the next few days."

    adm "Your mission: intercept and disrupt that convoy. Our resources are limited, plan accordingly."

    adm "We’ll see if your new boat lives up to the Federation’s expectations. Dismissed, Captain. 
        Make ready to sail at dawn."

    # Transition / lead player into next scene (e.g., leaving port).
    nar "With your orders in hand, you head toward the dock. The [submarine_name] waits, 
        engines quietly ticking over as the crew readies for departure..."

    # Optionally jump to a new label that handles the patrol logic:
    jump premission

# === 5. PLACEHOLDER PATROL LABEL ===

label begin_patrol:
    # This is where you'd implement the gameplay:
    # random events on transit, radio intercept puzzle, etc.
    nar "You cast off from the port of Carina at dawn. The sea is calm, but a chill wind 
        foreshadows the dangers ahead. It's time to begin your first patrol..."

    # Transition to combat encounter
    nar "A lookout spots a Tiberium supply ship in the distance. It's time to engage."
    jump combat
    return
