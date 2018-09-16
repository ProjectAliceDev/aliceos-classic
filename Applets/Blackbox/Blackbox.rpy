## Blackbox
# A puzzle minigame inside of DDLC
# Author(s): Marquis Kurt (@alicerunsonfedora)
# Copyright: (C) 2018

init python:
    class Blackbox(Applet):
        ## App Manifest
        # Define important information about your app here.
        # This information will be used in places like the
        # Control Center, notification badges, apps menus,
        # and the desktop shell.

        # Provide a short name and a long name for your app.
        short_name = "Blackbox"
        long_name = "Puzzle Time"

        # Provide the author information, version number, and
        # description of your app, as where as the name of the
        # folder that your applet lives in.
        app_dir = "Blackbox"
        author = "Marquis Kurt"
        version = "1.0.0"
        description = """\
Puzzle Time provides a fun and unique way of solving puzzles in between scenes in DDLC.
        """

        # Define your icons here. They should be located in 
        # your Applet's Resources/icons/ folder
        icons = {
            16: "16.png",
            24: "24.png",
            32: "32.png",
            64: "64.png",
            128: "128.png",
            256: "256.png"
        }

        # Define what permissions your applet will need.
        # See the Applet Manifest wiki page for all possible
        # permissions
        permissions = {pm_notify, pm_files, pm_sysadmin}

        def send_success_message(self):
            self.send_temporary_notification("Chapter unlocked", "Good job on solving the puzzle!", action=Return(0))

        def discover_notify(self):
            if persistent.aliceos_permissions["Blackbox_notify"] == True:
                return True
            else:
                return False

        def show_puzzle_window(self, puzzleno):
            if puzzleno == 1:
                renpy.call_screen("blackbox_puzzle_ch0")
            elif puzzleno == 2:
                renpy.call_screen("blackbox_puzzle_ch1")
            else:
                pass
    
    blackbox = Blackbox()

## Applet Code
# Define your applet after you have established your
# app's manifest here. This may include screens, labels,
# or definitions. Please keep all of your applet's code
# in this file.

## 1st Blackbox puzzle window.
init screen blackbox_puzzle_ch0:
    use UIWindow(blackbox)
    frame:
        style "blackbox_start"
        # xanchor -16
        yoffset 24
        xsize 1248
        ysize 635
        
        vbox:
            xoffset 32
            yoffset 32
            xsize 1216
            ysize 603
            
            vbox:
                text "Did you lose something?":
                    style "app_default_text"
                    xoffset 875
                    yoffset 100

## 2nd Blackbox puzzle window.
init screen blackbox_puzzle_ch1:
    use UIWindow(blackbox)
    frame:
        style "blackbox_elementary"
        # xanchor -16
        yoffset 24
        xsize 1248
        ysize 635
        
        vbox:
            xoffset 32
            yoffset 32
            xsize 1216
            ysize 603
            
            vbox:
                text "This content is not optimized for this screen size. Please increase your resolution.":
                    style "app_default_text"
                    xoffset 350
                    yoffset 200

## Blackbox Puzzles
init python:
    u_did_load = 0.0

# Puzzle 1 (Chapter 0)
# Check for Ren'Py saves in a specific spot.
label ch0_blackbox_puzzle:
    stop music fadeout 1.0
    scene blackbox bg with trueblack
    $ timeleft = get_pos()
    show vignette zorder 4 at truecenter
    play music t4
    show blight start zorder 2 at t11
    python:
        blackbox.ask_app_permissions()
        can_notify = blackbox.discover_notify()
        if can_notify == True:
            renpy.call_screen("blackbox_alert")
        else:
            try: sys.modules['renpy.error'].report_exception("The applet 'Blackbox' could not display the IntroUIView card. This usually happens if the user has disabled notifications for that applet. Please check your applet permissions and then run the applet again.", False)
            except: pass
            renpy.quit()
    # a "[player]..."
    # a "[player]..."
    # a "Why am I here?"
    # a "Why are you here?"
    # a "Why am I still alive?"
    # a "I don't understand, [player]..."
    # a "I don't deserve this."
    # a "No..."
    # a "This can't be..."
    # a "Why did you save me?"
    # a "Why did you {i}save{/i} me?"
    # a "{i}Why did you save me?{/i}"
    window hide(config.window_hide_transition)
    $ renpy.jump("ch0_blackbox_puzzle_loop")
    return

label ch0_blackbox_puzzle_loop:

    python:
        blackbox.show_puzzle_window(1)
        import os
        waittime = renpy.random.randint(4, 8)

        default = config.savedir
        renpy.list_saved_games()
        if renpy.can_load("1-3") == True:
            renpy.jump("ch0_blackbox_puzzle_success")

    window show(config.window_show_transition)
    a "{i}Why did you save me?{/i}"
    window hide(config.window_hide_transition)

    $ waittime -= 1
    $ u_did_load += 0.5
    $ pause(5)
    if u_did_load == 50.0:
        jump ch0_blackbox_puzzle_failure
    if waittime > 0:
        jump ch0_blackbox_puzzle_loop
    return

label ch0_blackbox_puzzle_failure:
    $ sweartext = glitchtext(8)
    window show(config.window_show_transition)
    $ style.say_dialogue = style.edited
    a "How can you be this clueless?"
    a "Is this your first time playing a visual novel or something?"
    a "Do you know how to play video games?"
    a "Just save in the third slot of the first page already, damn it!"
    a "It's not that [sweartext] hard!"
    $ style.say_dialogue = style.normal
    jump ch0_blackbox_puzzle_loop
    return

label ch0_blackbox_puzzle_success:
    show blight complete zorder 2 at t11
    $ blackbox.send_success_message()
    $ pause(0.75)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    return

# Puzzle 2 (Chapter 1)
# Check if the window is fullscreen.
label ch1_blackbox_puzzle:
    window hide(None)
    stop music fadeout 1.0
    scene blackbox bg with trueblack
    show blight start zorder 2 at t11
    $ timeleft = get_pos()
    show vignette zorder 4 at truecenter
    play music t4
    a "Well, at least we met each other."
    a "I'm no longer some obscure mystery to you, ahaha~"
    a "You probably already knew that from the start, didn't you?"
    a "You know, sometimes I wonder I'll take the big screen again..."
    a "{i}...or if I am forever trapped in a darkened window.{/i}"
    window hide(config.window_hide_transition)
    jump ch1_blackbox_puzzle_loop
    return

label ch1_blackbox_puzzle_loop:
    $ waittime = renpy.random.randint(4, 8)
    if preferences.fullscreen == True:
        jump ch1_blackbox_puzzle_success
    else:
        $ blackbox.show_puzzle_window(2)
        # window show(config.window_show_transition)
        # a "{i}...or if I am forever trapped in a darkened window.{/i}"
        # window hide(config.window_hide_transition)
        $ waittime -= 1
        $ pause(3)
        if waittime > 0:
            jump ch1_blackbox_puzzle_loop
    return

label ch1_blackbox_puzzle_success:
    show blight complete zorder 2 at t11
    $ blackbox.send_success_message()
    a "I don't understand this at all."
    a "I didn't want this."
    a "Why would I want to be in somebody else's universe?"
    a "For what, more control?"
    a "For pure torture because of how imperfect I really am?"
    a "Jeez, he really couldn't think of something more horrifying, could he?"
    a "Well, he's absolutely made a heavenly mistake."
    $ style.say_dialogue = style.edited
    a "Such a shame you have to pay that price."
    $ style.say_dialogue = style.normal
    return
