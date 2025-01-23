# This file contains the global definitions and settings for the game.
define adm = Character("Admiral Beckett", color="#c8c8ff")
define cpt = Character("Captain", color="#ffddc8")  # The player, first-person or direct.

define nar = Character(None)

# Background images
define bg_submarine = "images/submarine.jpg"
define bg_dock = "images/dock.jpg"

# Sound and music definitions
define audio.engine = "audio/engine_loop.ogg"
define audio.alarm = "audio/alarm.ogg"

# Functions for handling sound effects
init python:
    def play_alarm():
        renpy.sound.play("audio/alarm.ogg")

    def stop_alarm():
        renpy.sound.stop()

# Global game settings
default difficulty = "Normal"

# Transition effects
define fade_slow = Fade(1.0, 0.5, 1.0)
define dissolve_quick = Dissolve(0.3)


