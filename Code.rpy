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
     g"And she isn't here to help me fix it."

     g"Today is silent, just like yesterday… and the day before."
   
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

    jump search_loop_day1


# -------------------------
# SEARCH LOOP
# -------------------------

label search_loop:

    menu:

        "Look at the table":
            jump table_day1

        "Look at the shelves":
            jump shelves_day1


# -------------------------
# TABLE
# -------------------------

label table_day1:

    g "Oh… Mom left something here."

    "You find matches on the table and a small note."

    g "I can’t read well..."

    "as you try to decipher,it appears that the note reads: 'I'll be back. If anything scares you… close your eyes and stay still. Love, Mom.'"

    g "..."

    $ matches_found = True

    g "I should be quick…"

    "A strange feeling spreads through the room."

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

        g "It’s getting harder to see..."

        menu:
            "Light the candle":
                jump light_candle_day1


# -------------------------
# LIGHT CANDLE
# -------------------------

label light_candle_day1:

    "You strike the matches."

    "The flame flickers."

    show entity_flash

    e "..."

    

    return

   
   # DAY 2__________________________


label day2:

    scene morning_room

    g "..."

    g "It's morning already.."

    show mirror_scene

    g "Am I hurt?"

    show angel_reflection_mirror

    a "oh dearest.."

    g "Angel!"
     
    "Angel frowns glancing at the scar"

    a "What happened to you.."

    g "It was… that thing.. That..."
    
    show angel_hug

    "Angel's hug was visible on the mirror, yet you didn't feel it on you."

    "It still felt nice."
    
    a "A presence.."
    a "You came across something last night, didn't you?
    a "Something not of this realm, just as i am"

    "Angel's face seemed concerned"

    a "I can protect thee.

    a "But only if you help me aswell."

    g "Help… you?"

    a "yes, my dear sweet child. But do not fret, it isn't something big i ask of you, infact you can do it easily."

    g "what is it?"

    a "simple."

    a "Pray for me."

    a "then i can bring my power to protect you, help you rest a night without this creatures presence"

    a "But i need your prayers, you see my powers grows weak once the sun goes down."

    # choice
    menu:
        "Accept Angel's offer?":
            "Yes":
                $ angel_trust += 1
                $ gave_prayer = True
                jump gift_day2

            "No"
             jump persuasion_day2

label gift_day2:

    g "Okay… I will."

    a "Good child."

    "You tuck yourself in bed, and pray as you fall asleep."

    "The night feels different."

    jump day3

label persuasion_day2

  a "Are you certain?"

  "The scar on your face, didn't hurt that much but it was a reminder."

 "That something far much strong might hurt you"

 "Was it really a good idea to refuse the angel? Afterall the creature could do far much worse."

g "..." 

 "the choice was obvious, and its just a simple prayer."

g "I'll do it."

$ angel_trust += 1
$ gave_prayer = True

a "Good child."

    "You tuck yourself in bed, and pray as you fall asleep."

    "The night feels different."




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

