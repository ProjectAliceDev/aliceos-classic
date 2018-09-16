label ctf_cipher:
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
    a "Welcome back, errand boy."
    a "Or girl..."
    a "I don't know, it's not easy to tell what's real and what's not!"
    a "Well, I think you might be able to really help me this round."
    a "You see, my IT department recently just released a private beta of a cloud storage solution."
    a "They sent me an email with the login information, but I can't figure out what the hell they're saying!"
    a "Unfortunately, I accidentally deleted the email, ehehe~"
    a "But, I do have a screenshot, at least."
    a "Here. I'll simply write the image to your hard drive. This might take a second..."
    $ consolehistory = []
    call updateconsole("f.write(img_data.decode('base64'))", "ciphermail.png written successfully.")
    python:
        with open(config.basedir + "/game/Applets/CaptureTheFlag/Resources/assets/data", 'r') as g:
            img_data = g.readline()
            with open(config.basedir + "/ciphermail.png", "wb") as f:
                f.write(img_data.decode('base64'))
    a "Did it work? Look for a file called {i}ciphermail.png{/i} in your game directory."
    a "I hope it did."
    call hideconsole
    a "Well, do you think you can extract the password in there for me?"
    a "It'd be a huge help."
    call ctf_cipher_check
    return

label ctf_cipher_check:
    python:
        b = ctf.flags[1].decode('base64')
        flaginput = renpy.input("Enter the flag.")
        if flaginput == b:
            ctf.send_temporary_notification("Flag Acquired", "Congrats on solving the challenge!", action=Return(0))
            renpy.call("ctf_cipher_end")
        elif flaginput == "famous":
            with open(config.basedir + "/game/Applets/CaptureTheFlag/Resources/assets/famous", 'r') as f:
                famous = f.readlines()
                with open(config.basedir + "/tesseract", 'w+') as g:
                    g.writelines(famous)
            renpy.call_screen("alert", title="Invalid Flag", message="The flag you have entered is incorrect.", ok_action=Return(1))
            a("Not again, famous!")
            renpy.call("ctf_cipher_check")
        else:
            renpy.call_screen("alert", title="Invalid Flag", message="The flag you have entered is incorrect.", ok_action=Return(1))
            renpy.call("ctf_cipher_check")

    return

label ctf_cipher_end:
    a "Oh... now I see why then encrypted the message..."
    a "Ehehe~"
    a "Jeez, I didn't see that coming."
    a "And to be fair, I don't only dream in OCR."
    a "I have some pretty crazy nightmare written in bytecode."
    a "Trust me, you do {i}not{/i} want to see them."
    return