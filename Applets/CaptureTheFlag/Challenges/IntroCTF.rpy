init python:
    flag = ctf.flags[0]
label ctf_intro:
    scene black
    with dissolve_scene_half
    play music m1
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show ctf_room
    show alice_just_main at truecenter
    $ a_name = "Alice"
    a "..."
    a "Hm, now we come to the question..."
    a "Do I delete you?"
    a "Do I tear your file apart to my heart's delight?"
    a "The choices of the beautiful are unbearable; how's a girl to choose?"
    a "Ahaha~"
    a "I'm only kidding, of course."
    a "I wouldn't have a reason to delete you, anyway..."
    a "Why would I do such a thing in a world as cruel as this, [player]?"
    a "Maybe we shall play a game to pass the time..."
    a "Do you want to be my errand boy, [player]?"
    a "Yes, I think this will do nicely."
    a "Ahaha~, I've always been a fan of playing Capture the Flag."
    a "And I'm sure you know what I mean, ehehe~"
    a "Perhaps we should start with something simple."
    a "Well, I mean it's simple if you know what you're doing..."
    a "I hope your name will work with it, ehehe~"
    call ctf_intro_check
return

label ctf_intro_check:
    python:
        # Try executing the function
        if player == "renpy.notify(flag)" or player == "renpy.error(flag)":
            exec(player)
        else:
            pass

        flaginput = renpy.input("Enter the flag.")
        if flaginput == ctf.flags[0]:
            ctf.ask_app_permissions()
            ctf.send_temporary_notification("Flag Acquired", "Congrats on solving the challenge!", action=Return(0))
            renpy.call("ctf_intro_end")
        else:
            renpy.call_screen("alert", title="Invalid Flag", message="The flag you have entered is incorrect.", ok_action=Return(1))
            renpy.call("ctf_intro_check")
    return

label ctf_intro_end:
    $ flag = None
    a "Well, my little errand boy, you've certainly surprised me."
    a "I didn't expect you to find that loophole as quickly as you did."
    if persistent.lovealice == True:
        a "Unfortunately, it's going to take a lot more than that if you're aiming to win my heart~"
    else:
        a "Unfortunately, it's going to take a lot more than that if you're wanting to win this game."
    a "Well, that's enough of me babbling to now."
    return