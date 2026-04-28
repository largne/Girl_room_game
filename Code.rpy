# Girl_room_game (working title)

define g = Character("Girl")
define a = Character("Angel")
define e = Character("Entity")

default angel_trust = 0
default gave_offering = False
default knows_ritual = False
default matches_found = False
default candles_found = False


label start:
    jump day1


label day1:

    scene room_day  # placeholder

    g "It broke."

   #image of a broken toy mayb shape of an angel (our evil angel took the inspo from here lol)

    g "Not too long ago, just around after mom left."
    g "And she isn't here to help me fix it."

    g "Today is silent, just like yesterday… and the day before."
   
    scene window_view

    g "Mom said she would come back in a week, but I don’t know when that is anymore."
    g "Or if it has already passed."

    g "I feelt upset at first."
    g "My only toy is broken."
   
    show Angel with dissolve

    g "But i have another angel now. A real one."
   g "Mom told me before she left, that sometimes for good things to happen you need to make sacrifices."

   g "Maybe this was what she meant."
   
   g "Angel is nice, but I'm sad i can't play with angel long, it always leaves when the sun goes down."
    
    g "Nothing much i can do, other than wait for mom to come back."
    g "And maybe she can fix my toy when she is back.."
    g "She always says she will fix things anyways."
 
    #OLD SCRIPT _____________________

    g "Before she left, she told me that angel would take care of me. That was, before it broke."

    g "But I have my own angel anyways, a real one."

    show angel_reflection at center

    g "I see it sometimes. It doesn’t always speak."


    g "I don’t know how it found me, but I know it protects me."
    
   ______________________________________


   
    a "..."

    hide angel_reflection

    scene dark_room

    g "It’s getting dark…"
    g "oh..Electricity is not working?"
    g "I should light a candle before it gets worse."

    "You search the room for a light source..."

    jump search_loop


# -------------------------
# SEARCH LOOP
# -------------------------

label search_loop:

    menu:

        "Look at the table":
            jump table

        "Look at the shelves":
            jump shelves


# -------------------------
# TABLE
# -------------------------

label table:

    g "Oh… Mom left something here."

    "You find matches and a small note."

    g "I can’t read well..."

    "The note reads: 'If anything scares you… close your eyes and stay still. Love, Mom.'"

    g "..."

    $ matches_found = True

    g "I should be quick…"

    "A strange feeling spreads through the room."

    jump search_loop


# -------------------------
# SHELVES
# -------------------------

label shelves:

    if not matches_found:
        g "There are candles here."
        g "But I need something to light them with..."

        jump search_loop

    else:
          $ candles_found = True

        g "I can light the candle now."

        g "It’s getting harder to see..."

        menu:
            "Light the candle":
                jump light_candle


# -------------------------
# LIGHT CANDLE
# -------------------------

label light_candle:

    "You strike the matches."

    "The flame flickers."

    show entity_flash

    e "..."

    

    return

   
    DAY 2:


label day2:

    scene morning_room

    g "..."

    g "I woke up."

    show mirror_scene

    g "Am I hurt?"

    show angel_reflection_mirror

    a "oh dearest.."

    a "What happened to you.."

    g "It was… that thing.."

    a "I can protect you."

    a "But only if you help me."

    g "Help… you?"

    a "Pray for me. And give me something you cherish."

    # choice
    menu:
        "Trust the angel?":
            "Yes":
                $ angel_trust += 1
                $ gave_offering = True
                jump day2_gift
            "No":
                jump day2_no_trust


label day2_gift:

    g "Okay… I will."

    "You leave a small offering."

    a "Good child."

    "The night feels different."

    jump day3


label day2_no_trust:

    g "I don’t understand."

    a "Then the monster will return."

    jump day3


label day3:

    scene morning_kitchen

    g "I slept… I think."

    g "The monster didn’t come."

    g "My angel protected me."

    g "But… I’m still scared."

    scene breakfast_table

    # YELLOW: distorted food / uncanny domestic scene
    "The room feels slightly wrong."

    show angel_glitch

    a "Have you rested well?"

    g "Yes… thank you."

    a "There is a way to remove the monster forever."

    a "But everything has a price."

    g "I don’t have money."

    a "I don’t want money."

    a "I want something… from your world."

    g "I don’t understand..."

    a "You don’t need to."

    a "Just trust me."

    g "What is it?"

    a "A ritual."

    menu:
        "Accept ritual?":
            "Refuse":
                jump day3_refuse
            "Ask more":
                jump day3_continue


label day3_refuse:

    g "No… I can’t."

    a "Then it will return."

    jump night3


label day3_continue:

    g "I

