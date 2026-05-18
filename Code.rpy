# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = "Girl"

# The game starts here.

init python:
    def toggle_eyes():
        store.eyes_closed = not store.eyes_closed




screen eye_toggle():

    if eye_event_active:

        # BLACK SCREEN WHEN EYES CLOSED
        if eyes_closed:
            add Solid("#000000")

        imagebutton:
            xalign 0.98
            yalign 0.02

            idle ("eye_open.png" if not eyes_closed else "eye_close.png")
            hover ("eye_open.png" if not eyes_closed else "eye_close.png")

            action Function(toggle_eyes)

label start:
    jump day1


label day1:

   

    g "It broke."

    #image of a broken toy mayb shape of an angel (our evil angel took the inspo from here lol)

    g "Just around after mother left."
    g "And she isn't here to help me fix it."

    g "Today is silent, just like yesterday… and the day before."

    g "Mother said she would come back in a week, but I don't know when that is anymore."
    g "Or if it has already passed."

    g "I felt upset at first, but she told me i am a big girl now."
    g "And she told me not to cry, that the angels would take care of me just like they did with her."
    g "..."
    g "But i almost cried when doll got ripped."

    g "..."

    scene outside_day with fade 

    g "It's too quiet without mom here. I can almost hear my thoughts out loud."

    g "{cps=25}Huh?{/cps}" with vpunch

    g "Did the curtain just move?"

    g "That's weird... I thought I saw something outside."

    g "..."

    g "Oh, it's you."
   

    show angel_window with dissolve

    a "..."

    g "You're back."

    g "Sorry, i can't play now."

    g "Mom said I shouldn't stay up too long."
    
    g "Angel is nice"
    
    g "But you always leave when the sun goes down."

    g "And I don't know where you go."
    
   

    a "..."

    g "..."

    g "There's nothing I can do."

    g "I just wait."

    g "For mom to come back."

   

    g "She said she'd fix things."

    g "She always fixes things."

    g "So she'll fix my toy too."


    a "..."

    g "Right?"

    

    hide angel_window

    scene outside_night with dissolve

    g "It's getting dark…"
    g "oh..Electricity is not working?"
    g "I should light a candle before it gets worse."
    

    jump search_loop_day1


# -------------------------
# SEARCH LOOP
# -------------------------

label search_loop_day1:
     
    scene room_sunset with dissolve

    "You should light a candle before it gets worse."
    menu:

        "Look at the table":
            jump table_day1

        "Look at the dresser":
            jump dresser_day1

        "Look at the shelves":
            jump shelves_day1


label dresser_day1:

    scene dresser with dissolve

    call screen dresser_screen

    jump search_loop_day1
    

screen dresser_screen:

    add "dresser_default.png"

    # RETURN BUTTON (top)
    textbutton "RETURN":
        xpos 20
        ypos 20
        action Return()

    # LEFT DRAWER
    imagebutton:
        idle "asset_left_drawer.png" 
        xalign 0.2
        yalign 0.247
        action Jump("left_drawer")
        focus_mask True

    # RIGHT DRAWER
    imagebutton: 
        idle "asset_right_drawer.png" 
        xalign 0.812
        yalign 0.245
        action Jump("right_drawer")
        focus_mask True
    
    
label left_drawer:

    scene open_left_drawer with dissolve

    "You open the left drawer."

    "A faint smell of dust and old fabric comes out."

    "There's nothing useful there."

    jump dresser_day1


label right_drawer:

    scene open_right_drawer with dissolve

    "You open the right drawer."

    "A thread, needle and scissors."

    "Would be useful if you needed to cut something."

    "But not right now."

    jump dresser_day1


# -------------------------
# TABLE
# -------------------------

label table_day1:

    g "Oh…"
    
    g "Mom left something here."

    "You find matches on the table and a small note."

    g "I can't read well..."

    "as you try to decipher,it appears that the note reads: 'I'll be back. If anything scares you… close your eyes and stay still. Love, Mom.'"

    g "..."

    $ matches_found = True

    g "I should be quick…"

    "A strange feeling spreads through the room."

 
    $ eye_event_active = True
    show screen eye_toggle 

    "(you can now toggle close or open eyes)"

    jump search_loop_day1


# -------------------------
# SHELVES
# -------------------------

label shelves_day1:

    if not matches_found:
        g "There are candles here."
        g "But I need something to light them with..."

        jump search_loop_day1

    else:
        $ candles_found = True

        g "I can light the candle now."

        g "It's getting harder to see..."

        menu:
            "Light the candle":
                jump light_candle_day1


# -------------------------
# LIGHT CANDLE
# -------------------------

label light_candle_day1:

    "You strike the matches."

    "The flame flickers."

    scene candle_room with dissolve


    g "I hope there will be electricity tomorrow.."

    g "I don't have enough matches to light up many candles."

    g"..."

    "Time passes, eventually you tuck yourself in the bed."


    scene candle_bed with dissolve


    g "I can't fall asleep easily when i'm alone."
    g "It feels scary, as if something is hiding under my bed and it's waiting for me to go to sleep."
    g "If only i could talk to Angel at this time."
    g "..."

    scene dark_bed with dissolve

    g "..!" with vpunch

    g "The candle got blown of?"

    g "But the window is closed, and there's no wind.."

    g "I'm scared.."

    g "What's that noise?"
 
    g "I should close my eyes, but i'm scared to do so.."
    


    return
