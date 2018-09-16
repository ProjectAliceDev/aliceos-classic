## IntroUIView - Blackbox
# The initial screen that is displayed before puzzles begin
# Author(s): Marquis Kurt (@alicerunsonfedora)
# Copyright: (C) 2018

init -1000 python:
    blackbox_message = """\
Welcome to Puzzle Time! Over the course of the game, you will be asked to solve multiple puzzles. However, these aren't your standard puzzles. You must challenge your brain and think outside of the box for some of the solutions. As a fair warning, you may need to change the game's settings or manipulate files in your Home directory to achieve an action.

If you get stuck, don't worry. There are hints that can be displayed at any given time.
    """
    
init -501 screen blackbox_alert:
    modal True
    style_prefix "consent"
    zorder 2000
    add "gui/overlay/confirm.png"


    frame:
        xsize 600
        ysize 656
        style "confirm_frame"
        
        has vbox:
            xalign .5
            yalign .5
            spacing 16
            

        add "mod_assets/images/gui/puzzle.png":
            xalign 0.5
        label _("Puzzle Time"):
            style "consent_title"
            xalign 0.5

        label _(blackbox_message):
            style "consent_message"
            xalign 0.5

        frame:
            xalign 0.5
            xsize 568
            style "consent_button_frame"

            hbox:
                xalign 0.5
                spacing 16

                textbutton _("Get started") action Return(0):
                    style "consent_button"
                    xpadding 128
