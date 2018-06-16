##This is an example scene
##It teaches you about making mods, and is also a code example itself!

define a = Character("Alice", color = "#ffffff")

#Each section needs a label, this is how we will call the scene in or parts of the script
label example_chapter:
    stop music fadeout 1.0
    scene black
    call updateconsole("os.add(\"characters/alice.chr\")", "alice.chr added successfully.")
    call updateconsole("os.replace(_yuri, _alice)", "Operation complete.")
    call updateconsole("renpy.file(\"characters/alice.chr\")", "Loaded alice.chr successfully.")
    $ renpy.call_screen("dialog", "And now I get what was promised to me, Henry.", ok_action=Return())
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5
    hide screen tear
    scene bg club_day2
    with dissolve_scene_half
    play music t2g3
    show monika 5 at t11 zorder 2
    m "Hi again, [player]!"
    m "Glad to see you didn't run away on us. Hahaha!"
    mc "Nah, don't worry."
    mc "This might be a little strange for me, but I at least keep my word."
    show monika at thide zorder 1
    hide monika
    "Well, I'm back at the Literature Club."
    "I was the last to come in, so everyone else is already hanging out."
    show yuri glitch2 at t32 zorder 2
    y "Thanks for keeping your promise, [player]."
    show yuri 1a at t32 zorder 2
    a "I hope this isn't too overwhelming of a commitment for you."
    show yuri 1u at t32 zorder 2
    a "Making you dive headfirst into literature when you're not accustomed to it..."
    show natsuki glitch1 at i33 zorder 2
    n "Oh, come on! Like he deserves any slack."
    n 4e "You already had to be dragged here by Monika."
    n "I don't know if you plan to just come here and hang out, or what..."
    n "But if you don't take us seriously, then you won't see the end of it."
    show monika 2b at l41 onlayer front
    m "Natsuki, you certainly have a big mouth for someone who keeps her manga collection in the clubroom."
    n 4o "M-M-M...!!"
    show monika at lhide onlayer front
    hide monika onlayer front
    "Natsuki finds herself stuck between saying \"Monika\" and \"Manga\"."
    show natsuki at h33
    n 1v "Manga is literature!!"
    show natsuki at thide zorder 1
    hide natsuki
    "Swiftly defeated, Natsuki plops back into her seat."
    show yuri 2s at t11 zorder 2
    call updateconsole("os.mask(_alice >> _yuri)", "Operation complete.")
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5
    hide screen tear
    call hideconsole
    play music t6g
    y "I'm sorry, [player]..."
    y "We'll make sure to put your comfort first, okay?"
    show yuri 2g
    "Yuri shoots Natsuki with a disappointed glance."
    y 1a "Um, anyway..."
    y "Now that you're in the club and all..."
    $ style.say_dialogue = style.edited
    y "...and I know this is a bit sudden, but..."
    y "...can I show you my poem, [player]?"
    y "I myself am a bit conflicted on it and could use your advice."
    $ style.say_dialogue = style.normal
    mc "Well..."
    mc "I can't really say no either way."
    mc "Like you said, I'm in this club now."
    mc "So it only feels right for me to do something like that, if you ask."
    y 4b "W-Wait..."
    y "I didn't mean it like that!"
    y "Uu..."
    y "If you don't really want to, then forget I said anything, I guess..."
    mc "Ah--No, it's not that, Yuri."
    mc "I want to try to be a part of this club."
    mc "So even if I don't read often, I'd be happy to look at your poem right now if you wanted me to."
    y 3t "A-Are you sure...?"
    y "I just felt like..."
    y 3u "...Well, as Vice President and all..."
    play music t5
    $ style.say_dialogue = style.edited
    y "...That I should her you out on a few things."
    y 1s "I know the poem's a bit rough, but..."
    y "I wanted to try something new."
    y "It's a short read, so it should keep your attention, even if you don't usually read."
    y "I h-hope..."
    show yuri at sink
    y 4b "God, I hope this works..."
    $ style.say_dialogue = style.normal
    "Th-This is..."
    "How is this girl accidentally being so cute?"
    define poem_name = Poem( author = "yuri", yuri_3 = True, title = "The Gal", text = """ She takes a look in the mirror
Revealing the face that she didn't see.

The axe that rests nearby
Sends the ink into a dark puddle.

The tears of disbelief from her face
join the puddle in regret and ignorance.""" )

    call showpoem(poem_name)
    mc "Uh, Yuri..."
    mc "I know you said you wanted to try something new, but..."
    mc "I'm kind of having a hard time reading it{nw}"
    y 2r "Maybe you're just jealous that [player] appreciates my advice more than he appreciated yours!"
    
    scene white
    with Dissolve(1.0)

    return
