# Girl_room_game (working title lol)
define g = Character("Girl")
define a = Character("Angel")
define e = Character("Entity")

default angel_trust = 0
default gave_offering = False
default knows_ritual = False

label start:

    jump day1


label day1:

    scene room_day #placeholder code, will edit after images upload

    g "Today is silent, just like yesterday… and the day before."

    g "Mom said she would come back in a week, but I don’t know when that is anymore. Or if it has already passed."

    # window view / mirror foreshadow
    scene window_view

    g "Sometimes I miss her."

    g "But atleast I’m not alone."

    g "Before she left, she told me that angels would take care of me. Just like they did with her."

    g "I think I have my own angel."

    show angel_reflection at center

    g "I see it sometimes. It doesn’t always speak. I don’t know how it found me, but I know it protects me."

    a "..."

    # Angel interaction minimal, uncanny

    hide angel_reflection

    # candle mechanic intro
    scene dark_room
    g "it's getting dark, it seems today we have no electricity."

    g "I should light a candle before it turns even darker."

    # YELLOW: tutorial interaction sequence
    "You search the room for a light source..."

    #option a) look at the shelves (where candles are)

    #option b) look on the table 

    #player can find candles, but if they dont pick uo the matches first it doesnt light up. 
    label shelve_option:
    
    
    label Table_option:
    
    g "oh,Mom left something here..."

    # diary/note interaction
    "You find a note next to a candle."

    g "I can't read well.."

  "dearest.. food in the fridge...bla bla..If bla bla scares you… close your eyes and stay still. love you, mom."

    g "There are some matches next to it."

    "The room grows colder."
    "A sudden presence fills the darkness."

    
    g "I should be quick and light it up."

   #the player lights the candke up but it had already turned dark.

    show entity_flash

    e "..."

   
    jump day2


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

