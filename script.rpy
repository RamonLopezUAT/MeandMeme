# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.





label start:
#PART 1 ------------------------------------------------------------------------------------
    scene gamestart 
    "Today is the day!"
    "I don't know about you, but I'm getting pretty tired about your love life."
    "It's barren, fully."
    "So. dear player. I've done you the favor of setting you up with an account for the most sucessful dating app of the last decade!"
    "..."
    "...Okay, you don't have to look THAT angry at me."
    "Look, just set up your profile already."
    "What's your name again?"
# The phrase in the brackets is the text that the game will display to prompt 
# the player to enter the name they've chosen.
    $ player_name = renpy.input("Type your name! (If you're using a controller: Don't.)")
    $ player_name = player_name.strip()
    define p = Character('You')
# The .strip() instruction removes any extra spaces the player 
# may have typed by accident.
#  If the player can't be bothered to choose a name, then we
#  choose a suitable one for them:
    if player_name == "":
        "Oh? You don't want one?"
        "What do you think you're too cool for a name?"
        "In that case, I dub thee, Frankfurt."
        "Idiot. "
        $ player_name="Frankfurt."    
# Now the other characters in the game can greet the player. 
"Pleased to meet you, %(player_name)s!"
p "i feeel nothing but painS"
"Alright, so next step."
# If pronouns needed add here.
"Alright, good, we got those now."
jump tindertime
# END PART 1 ---------------------------------------------------------------------------

label tindertime:
scene swipingbg with dissolve 
"fadas"
"Oh look at this clown"
show image djsahdad 


