# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.

default preferences.text_cps = 30

label start:

    $ preferences.text_cps = 30

    scene black with fade

    pause 1.5

    "Humans have a tendacy to name things."

    "For flowers."

    "For houses."

    "For things we love."

    "A name, the most precious thing to a person. Their identity."

    "Come forth child, tell me your name."

    pause 1.0

    $ player_name = renpy.input(
        "Your name",
        default="",
        length=20
    ).strip()

    if player_name == "":
        $ player_name = "Girl"



    

    jump day1

label day1:



    g "It broke."

    #image of a broken toy mayb shape of an angel (our evil angel took the inspo from here lol)
    scene doll_bg with dissolve 

    g "Just around after mother left."
    g "And she isn't here to help me fix it."

    g "Today is silent, just like yesterday... and the day before."

    g "Mother said she would come back in a week, but I don't know when that is anymore."
    g "Or if it has already passed."

    g "I felt upset at first, but she told me i am a big girl now."
    g "And she told me not to cry, that the angels would take care of me just like they did with her."
    g "..."
    g "But i almost cried when doll got ripped."

    g "..."

    scene outside_day with fade 

    g "It's too quiet without mom here. I can almost hear my thoughts out loud."

    g "..."

    g "Nothing much happens here anyways. It's just... empty around."

    g "I sometimes see neighbours passing by, but they never say hi."


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
    
    g "You always leave when the sun goes down anyway. And there's not much time left now."


    a "My dear sweet child, you seem to be deep in thought."

    g "..."

    g "There's nothing I can do."

    "Angel glanced, quiet."
   

    g "She said she'd fix things."

    g "She always fixes things."

    g "So she'll fix my toy too."


    a "..."

    g "Right?"

    a "need a fix up on the dialogue here tbh - Lara"

    hide angel_window with dissolve

   
    g "The sun will go down soon."
    g "oh..Electricity is not working?"
    g "I should light a candle before it gets worse."
    

    jump search_loop_day1


# -------------------------
# SEARCH LOOP
# -------------------------

label search_loop_day1:

    scene room_wcup with dissolve

    "You should light a candle before it gets worse."

    call screen room_day_screen

    jump search_loop_day1


# -------------------------
# DRESSER CLOSE-UP
# -------------------------

label dresser_day1:

    scene dresser_corner with dissolve

    call screen dresser_closeup

    jump search_loop_day1


screen dresser_closeup:

    $ preferences.text_cps = 30

    # DRESSER CORNER BACKGROUND
    add "dresser_corner.png"


    # -------------------------
    # OBJECTS ON TOP OF DRESSER
    # -------------------------

    imagebutton:

        idle "dresser_closeup_stuff_n.PNG"
        hover "dresser_closeup_stuff_h.PNG"

        focus_mask True

        action Jump("dresser_day1_closeupstuff")


    # -------------------------
    # DRESSER DRAWERS / SHELVES
    # -------------------------

    imagebutton:

        idle "dresser_shelvesclose_n.PNG"
        hover "dresser_shelvesclose_h.PNG"

        focus_mask True

        action Jump("dresser_screen")


    # RETURN TO ROOM
    textbutton "RETURN":

        xpos 20
        ypos 20

        action Return()


# -------------------------
# OBJECTS ON TOP OF DRESSER
# -------------------------

label dresser_day1_closeupstuff:

    scene closeup_dresserstuff with dissolve

    if not matches_found:

        g "Matches! And a candle too!"

        g "There aren't many left though.."
        
        "You strike one of the matches, attempting to light up the candle you found."

        "But the half-burnt candle refuses to light up."

        g "Thats..odd, maybe i should find a new one?"

        $ matches_found = True

       

    else:

        g "The matches are still here."

        g "So is the useless candle."

    call screen dresser_stuff_screen

    jump dresser_day1


screen dresser_stuff_screen:

    textbutton "RETURN":

        xpos 20
        ypos 20

        action Return()


# -------------------------
# DRESSER DRAWERS / SHELVES
# -------------------------

label dresser_screen:

    scene dresser with dissolve

    call screen dresser_screen

    jump dresser_day1


screen dresser_screen:

    $ preferences.text_cps = 30

    add "dresser_default.png"


    # RETURN TO DRESSER CLOSE-UP
    textbutton "RETURN":

        xpos 20
        ypos 20

        action Return()


    # -------------------------
    # LEFT DRAWER
    # -------------------------

    imagebutton:

        idle "asset_left_drawer.png"

        xalign 0.2
        yalign 0.247

        focus_mask True

        action Jump("left_drawer")


    # -------------------------
    # RIGHT DRAWER
    # -------------------------

    imagebutton:

        idle "asset_right_drawer.png"

        xalign 0.812
        yalign 0.245

        focus_mask True

        action Jump("right_drawer")


    # -------------------------
    # 3RD SHELF
    # -------------------------

    imagebutton:

        idle "asset_3rd_shelf.png"

        focus_mask True

        action Jump("dresser_3rd_shelf")


    # -------------------------
    # 4TH SHELF
    # -------------------------

    imagebutton:

        idle "asset_4th_shelf.png"

        xalign 0.1
        yalign 0

        focus_mask True

        action Jump("dresser_4th_shelf")


    # -------------------------
    # 5TH SHELF
    # -------------------------

    imagebutton:

        idle "asset_5th_shelf.png"

        xalign 0.1
        yalign 0

        focus_mask True

        action Jump("dresser_5th_shelf")


# -------------------------
# LEFT DRAWER
# -------------------------

label left_drawer:

    scene open_left_drawer with dissolve

    "You open the left drawer."

    "A faint smell of dust and old fabric comes out."

    "There's nothing useful there."

    jump dresser_day1


# -------------------------
# RIGHT DRAWER
# -------------------------

label right_drawer:

    scene open_right_drawer with dissolve

    "You open the right drawer."

    "A thread, needle and scissors."

    "Would be useful if you needed to cut something."

    "But not right now."

    jump dresser_day1


# -------------------------
# 3RD SHELF
# -------------------------

label dresser_3rd_shelf:

    show dresser_3rd_shelf with dissolve

    "You open the drawer."

    "A hand mirror, hairbrush, a bowl..."

    if not matches_found:

        g "There are candles here!"

        g "But I need something to light them with..."

        g "I can take them after I found a match."

        jump search_loop_day1

    else:

        $ candles_found = True

        g "I can light the candle now."

        g "It's getting harder to see..."

        menu:

            "Light the candle":
                jump light_candle_day1

    jump dresser_day1


# -------------------------
# 4TH SHELF
# -------------------------

label dresser_4th_shelf:

    scene dresser

    "You try to open the lower drawer."

    g "..!" with vpunch

    g "It's stuck, or locked."

    "An odd smell comes from the drawer."

    g "Maybe a rat nested there."

    "You don't really want to open it anymore."

    jump dresser_day1


# -------------------------
# 5TH SHELF
# -------------------------

label dresser_5th_shelf:

    show dresser_5th_shelf with dissolve

    show shelf_plate_half with dissolve

    g "Oh. Who left this here?"

    g "It seems something has been living in this shelf."

    g "Better leave it alone for now."

    jump dresser_day1


# -------------------------
# TABLE
# -------------------------

label table_day1:

    scene black with dissolve

    g "The tea has gone cold. I should clean the cup."

    g "..."

    g "The flowers smell nice."

    jump search_loop_day1


# -------------------------
# BOOKSHELVES
# -------------------------

label shelves_day1:

    scene bookshelf with dissolve

    g "Just some old books."

    g "I can look at them later."

    jump search_loop_day1

    

# -------------------------
# LIGHT CANDLE
# -------------------------

label light_candle_day1:

    $ preferences.text_cps = 30
    
    scene sunset with dissolve

    "You strike the matches."

    "The flame flickers."

    scene candle_room with dissolve


    g "I hope there will be electricity tomorrow.."

    g "I don't have enough matches to light up many candles."

    g"..."

    "Time passes, eventually you tuck yourself in the bed."


    scene candle_bed with dissolve


    g "I can't fall asleep easily when i'm alone."
    g "It feels scary... like something is hiding under my bed."
    g "Waiting for me to close my eyes."
    g "If only i could talk to Angel at this time."
    g "..."

    scene dark_bed with dissolve
    show vign with dissolve 

    g "..!" with vpunch

    g "The candle got blown of?"

    g "But the window is closed, and there's no wind.."

    g "..."

    g "What's that noise?"

    "Something is wrong."

    # =========================
    # START HORROR MECHANIC HERE
    # =========================



    g "I'm scared.."

    g "Mom said.."

    g "That I should close my eyes."

    g "But... that doesn't feel safe right now."

    g "..."

    g"Oh no.."



    "You must close your eyes."

    "But it's scary, and you want to open your eyes."

    "If the urge gets to you, you will automatically."

    "But then you will be in danger again."

   
    

    $ result = start_eye_event()
   
    

    if result == "death":

        jump death_eyes

    

    g "{cps=25}...{/cps}"

    g "{cps=25}I'm too tired.{/cps}"

    g "{cps=25}I can't keep my eyes open..{/cps}"


    scene black with dissolve

    pause 1.5

    jump day_2



label death_eyes:

    $ preferences.text_cps = 30

    scene bed_4 with vpunch
    show vign_blood_2 with vpunchs
    scene black with fade

    "..."

    "You saw it, didn't you."

    window hide

    # Both hands enter from opposite sides.
    show a_hand_left at hand_left
    show a_hand_right at hand_right

    # Let them slowly creep into view.
    pause 5.0

    show text "{color=#ff0000}And you kept staring.{/color}" at truecenter, text_shake
    pause 3.0

    show text "{color=#ff0000}Stupid child, you were told what to do. It was easy.{/color}" at truecenter, text_shake
    pause 3.0

    show text "{color=#ff0000}Disobedient{/color}" at truecenter, text_shake
    pause 3.5

    show text "{color=#ff0000}But I'm not complaining. You just made it easier.{/color}" at truecenter, text_shake
    pause 3.5
    
    show text "{color=#ff0000}You'll meet your mother soon.{/color}" at truecenter, text_shake
    pause 3.5
    
    hide a_hand_left with moveoutbottom
    hide a_hand_right with moveoutbottom

    pause 2
    
    show vign_blood_2 with vpunch
    show placeholder with vpunch 
       
    
    return







#DAY 2 BEGINS HERE

# ============================================================
# DAY 2
# ============================================================

label day_2:

    $ preferences.text_cps = 30


    

    "There are many beautiful moments in life."

    "But the mind does not hold them all equally."

    "It remembers the fall."

    "The sound of something breaking."

    "The door that was left open."

    "The thing beneath the bed that was not there yesterday."

    "We may build ninety-nine bridges..."

    "And still remember the one that collapsed."


    

    pause 1.5


    # --------------------------------------------------------
    # MORNING
    # --------------------------------------------------------

    scene room_day with fade

    pause 1.0

    g "I didn't go to school today."

    g "I can't go outside yet."

    g "Until she is back.."

    pause 0.8

    g "I think."

    pause 1.0


    # --------------------------------------------------------
    # MIRROR
    # --------------------------------------------------------

    scene mirror_neutral with dissolve

    pause 1.2

    g "I look tired."

    g "I couldn't sleep very well."

    g "They say young girls have to sleep early."

    g "Otherwise they won't grow."

    g "I don't want to sleep."

    g "..."

    pause 1.2

    g "If Doll wasn't broken..."

    g "Maybe I could sleep."

    g "But I have to keep the house safe."

    g "She'll be back tomorrow."

    pause 1.0

    g "I'm sure."

    pause 1.2

    g "Then she'll be proud of me."


    # --------------------------------------------------------
    # ANGEL APPEARS
    # --------------------------------------------------------

    scene mirror_angel_neutral with dissolve

    pause 2.0

    g "Angel?"

    "The mirror remains still."

    "Then, very faintly, something moves beneath the surface of the glass."


    pause 1.5

    a "You called."

    pause 1.5

    g "Last night..."

    g "There was something in my room."

    g "It blew out the candle. I knew it did, there was no wind or anything."

    pause 0.8

    g "I was really scared."

    a "I know."

    g "You know?"


    a "I saw what looked upon you."

    pause 1.5

    g "What was it?"

    a "A foul creature, it is."
    a "Do not give a name to that which has none."

    g "It has no name? But then.. what was it?"

    a "A thing that dwells where the light is thin."

    a "When the sun withdraws..."

    a "the old places open."

    g "Old places?"


    a "Places which were never meant for you."


    g "Like under my bed?"

    pause 1.5


    a "..."

    a "Oh Child...my sweet child.."

    a "There are things beneath beds."

    a "There are things beneath houses."

    a "And there are things beneath the world."
    
    "Angel was never physically there. But for a brief moment... you sensed the harsh squeeze on your shoulder."
    g "Are they going to hurt me?"

    "Angel chuckled to your remark, not tauntingly but rather with a sweet reassurance."
    a "Not whilst I hear you."

    g "You'll protect me?"


    a "I have watched over this house longer than your mother has drawn breath."

    g "..."

    g "You knew my mom?"

    a "I knew the woman who came before you."

    a "And she knew to be afraid."

    g "Mom isn't afraid. You're lying!"

    a "Me? A liar?"

    a "Then why did she teach you to close your eyes? Run away while you can devote yourself to me, your Angel who will protect you?"

    g "..."

    g "She...she did say the angels would take care of me."

    a "Yet she thought you to look away."

    g "B-but then.. should i not look away?"

    a "hmmm... not yet. Maybe later,tomorrow or the day after. Your soul.. it's not strong enough."

    g "What do you mean not strong enough?"

    a "Not yet, that is."

    g "I can be strong! How can i become strong?"
    a "There is a way, my child."
    a "When darkness comes..."

    a "do not wander."

    a "Do not answer when something calls your name."

    a "And above all..."

    a "pray before you sleep."

    a "Like those who wish to remain among the living. Pray to me, to your Angel."

    g "Will you hear me?"


    a "If your heart reaches toward the light..."

    a "I shall hear you."

    g "Really?"

    a "I have never broken a promise to you my dearest."

    g "I trust you."

    a "Good. Smart child."

    a "Now rest well tonight."

    pause 2.0

    scene black with dissolve

    pause 3.5

    scene room_day with dissolve

    g"The house looks the same as yesterday."
    pause 1.0

    g"Almost."

    g"I guess I have some time to kill."
    jump search_loop_day2


# ============================================================
# DAY 2 SEARCH LOOP
# ============================================================

default plate_filled = False


label search_loop_day2:

    $ preferences.text_cps = 30

    scene room_day with dissolve

    call screen room_day_screen_day2

    jump search_loop_day2


# ============================================================
# DAY 2 ROOM SCREEN
# ============================================================

screen room_day_screen_day2:

    # --------------------------------------------------------
    # TABLE
    # --------------------------------------------------------

    imagebutton:

        idle "hover_table_n.png"
        hover "hover_table_y.png"

        focus_mask True

        action Jump("table_day2")


    # --------------------------------------------------------
    # DRESSER
    # --------------------------------------------------------

    imagebutton:

        idle "hover_dresser_n.png"
        hover "hover_dresser_y.png"

        focus_mask True

        action Jump("dresser_day2")


    # --------------------------------------------------------
    # BOOKSHELF
    # --------------------------------------------------------

    imagebutton:

        idle "hover_books_y.png"
        hover "hover_books_n.png"

        focus_mask True

        action Jump("shelves_day2")


# ============================================================
# TABLE
# ============================================================

label table_day2:

    scene black with dissolve

    g "The flowers are still here."

    g "But the table close up image isn't."

    pause 1.0

    g "..."

    g "I don't remember putting them in water."

    pause 1.5

    g "They're still alive."

    jump search_loop_day2


# ============================================================
# BOOKSHELF
# ============================================================
# Put this near the top of your script

style letter_text:
    color "#a4c274"
    font "DejaVuSerif.ttf"
    size 28
    italic True
    xalign 0.5
    text_align 0.5

label shelves_day2:

    scene bookshelf with dissolve

    g "I don't like these books."

    pause 1.0

    g "They feel eerie..."

    menu:

        "Pick one":

            

            "You trace with your fingers against the hard covers. Until your hand stops at one of the books."

            "It catches your attention, as it slightly sticks off from the shelf compared to the other perfectly placed books."

            "As you pull it out, a paper falls down."

            pause 0.8

            "{color=#5C3028}I have been stupid, what have I done? What have I attempted?{/color}"

            "{color=#5C3028}The greatest of all sins..{/color}"

            "{color=#5C3028}I couldn't go through with it, as I have now came to my senses.{/color}"

            "{color=#5C3028}But it calls for blood, and sacrifice.{/color}"

            "{color=#5C3028}I am afraid I don't have much time.{/color}"

            "{color=#5C3028}The creature gains its power at night.{/color}"

            "{color=#5C3028}The power, I gave him by going through with this.{/color}"

            "{color=#5C3028}Yet I haven't finished it.{/color}"

            "{color=#5C3028}It cannot manifest itself in the daylight, not yet.{/color}"

            "{color=#5C3028}It knows I left it unfinished.{/color}"

            "{color=#5C3028}It is angry.{/color}"

            "{color=#5C3028}I don't know what will happen when it gets what it needs.{/color}"

            pause 1.0

            jump dresser_day2


        "Leave them":

            g "I'll leave it alone."

            jump dresser_day2

    jump search_loop_day2


# ============================================================
# DRESSER
# ============================================================

label dresser_day2:

    scene dresser_corner with dissolve

    call screen dresser_closeup_day2

    jump search_loop_day2


# ============================================================
# DAY 2 DRESSER CLOSE-UP
# ============================================================

screen dresser_closeup_day2:

    add "dresser_corner.png"


    # --------------------------------------------------------
    # OBJECTS / SHELVES
    # --------------------------------------------------------
    imagebutton:

        idle "dresser_closeup_stuff_n.PNG"
        hover "dresser_closeup_stuff_h.PNG"

        focus_mask True

        action Jump("dresser_day2_closeupstuff")
    imagebutton:

        idle "dresser_shelvesclose_n.PNG"
        hover "dresser_shelvesclose_h.PNG"

        focus_mask True

        action Jump("dresser_screen_day2")


    # --------------------------------------------------------
    # RETURN TO ROOM
    # --------------------------------------------------------

    textbutton "RETURN":

        xpos 20
        ypos 20

        action Return()

label dresser_day2_closeupstuff:

    scene closeup_dresserstuff with dissolve

    "Nothing new, the not burning candle is still here."
    
    g "Who even makes a non-burning candle?"


    jump dresser_day2


# ============================================================
# DAY 2 DRESSER SHELVES / DRAWERS
# ============================================================

label dresser_screen_day2:

    scene dresser with dissolve

    call screen dresser_screen_day2

    jump dresser_day2


screen dresser_screen_day2:

    $ preferences.text_cps = 30

    add "dresser_default.png"


    # --------------------------------------------------------
    # RETURN
    # --------------------------------------------------------

    textbutton "RETURN":

        xpos 20
        ypos 20

        action Return()


    # --------------------------------------------------------
    # LEFT DRAWER
    # --------------------------------------------------------

    imagebutton:

        idle "asset_left_drawer.png"

        xalign 0.2
        yalign 0.247

        focus_mask True

        action Jump("left_drawer_day2")


    # --------------------------------------------------------
    # RIGHT DRAWER
    # --------------------------------------------------------

    imagebutton:

        idle "asset_right_drawer.png"

        xalign 0.812
        yalign 0.245

        focus_mask True

        action Jump("right_drawer_day2")


    # --------------------------------------------------------
    # 3RD SHELF
    # --------------------------------------------------------

    imagebutton:

        idle "asset_3rd_shelf.png"

        focus_mask True

        action Jump("dresser_3rd_shelf_day2")


    # --------------------------------------------------------
    # 4TH SHELF / STUCK DRAWER
    # --------------------------------------------------------

    imagebutton:

        idle "asset_4th_shelf.png"

        xalign 0.1
        yalign 0

        focus_mask True

        if plate_filled:

            action Jump("open_stuck_drawer_day2")

        else:

            action Jump("dresser_4th_shelf_day2")


    # --------------------------------------------------------
    # 5TH SHELF
    # --------------------------------------------------------

    imagebutton:

        idle "asset_5th_shelf.png"

        xalign 0.1
        yalign 0

        focus_mask True

        action Jump("dresser_5th_shelf_day2")


# ============================================================
# LEFT DRAWER
# ============================================================

label left_drawer_day2:

    scene open_left_drawer with dissolve

    "You open the left drawer."

    "A faint smell of dust and old fabric comes out."

    "There's nothing useful there."

    jump dresser_day2


# ============================================================
# RIGHT DRAWER
# ============================================================

label right_drawer_day2:

    scene open_right_drawer with dissolve

    "A thread, needle and scissors."

    "Would be useful if you needed to cut something."

    "But not right now."

    jump dresser_day2


# ============================================================
# 3RD SHELF
# ============================================================

label dresser_3rd_shelf_day2:

    show dresser_3rd_shelf with dissolve

    pause 1.0

    g "Nothing interesting."

    jump dresser_day2


# ============================================================
# 4TH SHELF / DRAWER  STILL STUCK
# ============================================================

label dresser_4th_shelf_day2:

    scene dresser

    "You try to open the lower drawer."

    g "..!" with vpunch

    g "It's stuck, or locked."

    "An odd smell comes from the drawer."

    g "Maybe a rat nested there."

    "You don't really want to open it anymore."

    jump dresser_day2



# ============================================================
# 5TH SHELF  PLATE
# ============================================================

label dresser_5th_shelf_day2:

    show dresser_5th_shelf with dissolve

    # --------------------------------------------------------
    # EMPTY PLATE
    # --------------------------------------------------------

    if not plate_filled:

        show shelf_plate_empty with dissolve

        g "The plate is empty."

        pause 0.8

        g "..."

        g "I wonder why it's here."

        menu:

            "Fill it":

                $ plate_filled = True

                show shelf_plate_full with dissolve

                g "I put some food on the plate."

                pause 0.8

                g "There."

                pause 1.0

                jump dresser_day2


            "Leave it":

                g "I'll leave it alone."

                jump dresser_day2


    # --------------------------------------------------------
    # PLATE HAS ALREADY BEEN FILLED
    # --------------------------------------------------------

    else:

        show shelf_plate_full with dissolve

        g "The plate is still here."

        jump dresser_day2
