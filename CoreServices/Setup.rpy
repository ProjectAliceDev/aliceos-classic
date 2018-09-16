## Setup.rpy
# Post-install Setup Assistant (Pisa)
# Author: Marquis Kurt (@alicerunsonfedora)
# Copyright: (C) 2018
init python:
    gametos = """\
Insert your Terms of Service here.

By clicking \"I Agree\", you acknowledge this disclaimer and continue at your own risk.
"""
    gnutos = """\
You may copy, distribute and modify the software as long as you track changes/dates
in source files. Any modifications to or software including (via compiler) GPL-licensed
code must also be made available under the GPL along with build & install instructions.

The full license can be viewed at {a="https://www.gnu.org/licenses/gpl.html"}https://www.gnu.org/licenses/gpl.html{/a}.

By clicking \"I Agree\", you acknowledge this disclaimer and continue at your own risk.
        """
    xcoordinate=0.5
    ycoordinate=0.8

style setup_header_text is default:
    if not aliceos.oem_font_medium:
        font aliceos.font_medium
    else:
        font aliceos.oem_font_medium
    size 38

style setup_details_text is default:
    if not aliceos.oem_font_regular:
        font aliceos.font_regular
    else:
        font aliceos.oem_font_regular
    size 22

style setup_minor_text is default:
    if not aliceos.oem_font_light:
        font aliceos.font_light
    else:
        font aliceos.oem_font_light

image bg mojave setup = "Resources/bg_setup.png"
image setup_feedback = "Resources/feedback.png"
image mojave_setup = "Resources/setup-window.png"

# Setup Headers
image mojave setup header = Text("Alice OS Setup Assistant", style="setup_header_text")
image setup_beta_check_header = Text("Enroll in the Beta Program", style="setup_header_text")
image setup_game_tos_header = Text("License Agreement", style="setup_header_text")
image setup_accounts_header = Text("Create Your Computer Account", style="setup_header_text")

# Welcome
image setup_welcome_text = Text("Welcome to the Alice OS Setup Assistant. This tool will help you\nset up your computer and your game for playing.\n\nWhen you are ready, press 'Next'.", style="setup_details_text")

# Beta Information
image setup_prerelease_info = Text("We've detected that you're running a pre-release version of AliceOS.\nSome features of this operating system may not work properly\non your computer.\n\nIf you wish to roll back to a stable version of AliceOS, contact your\nsystem administrator.", style="setup_details_text")
image setup_send_feedback_info = Text("Your computer has been enrolled in the AliceOS Beta Program. You\ncan send feedback through the menu option on the main screen\nor in-game as seen below.", style="setup_details_text")

# Indicators
image setup_loader_text = Text("Initializing Setup Assistant...", size=14, style="setup_minor_text")
image setup_process_files = Text("Validating beta program files...", size=10, style="setup_minor_text")
image loader:
    "Resources/loader/1.png"
    pause 0.125
    "Resources/loader/2.png"
    pause 0.125
    "Resources/loader/3.png"
    pause 0.125
    "Resources/loader/4.png"
    pause 0.125
    "Resources/loader/5.png"
    pause 0.125
    "Resources/loader/6.png"
    pause 0.125
    "Resources/loader/7.png"
    pause 0.125
    repeat

# Computer Accounts
image setup_create_accnt = Text("Please create a username for this computer. Your password will be\ncreated automatically.", style="setup_details_text")

# License Agreements
image setup_game_tos_info = Text("AliceOS has detected that this game includes a License Agreement.\nPlease read the agreement and then agree to the terms.", style="setup_details_text")
image setup_tos_info = Text("AliceOS is licensed under the GNU GPL v3.\nPlease read the license summary below and agree to the terms.", style="setup_details_text")
image setup_game_tos_text = Text(gametos, size=16, style="setup_details_text")
image setup_tos_text = Text(gnutos, style="setup_details_text")

# Finished
image setup_complete_thankyou = Text("Your profile has been created and this computer is ready to be used.\n\nIf you need to enter a password, check the profiles file.\n\nThank you for choosing Alice OS.", style="setup_details_text")

        
label setup:
    stop music fadeout 1.0
    scene black with Dissolve(5.0)
    window hide(None)
    show loader at truecenter
    show setup_loader_text:
        xalign 0.5
        yalign 0.8
    pause 5.0
    show bg mojave setup zorder 2 with dissolve_scene_half
    window hide(None)
    show mojave_setup zorder 2 at truecenter
    show mojave setup header zorder 3:
        xalign 0.5 yalign 0.18
    show setup_welcome_text zorder 3:
        xalign 0.5 yalign 0.3
    $ ui.vbox(xalign=xcoordinate,yalign=ycoordinate)
    $ ui.textbutton("Next", ui.returns("choice1"), style="confirm_button", xalign=.5)
    $ ui.close()
    $ choice_selected=ui.interact()
    if aliceos.oem_mode:
        call screen alert("System Modified by Manufacturer", "This copy of AliceOS has been modified by your manufacturer, [aliceos.oem_name!t]. Your experience may vary from the standard AliceOS installation.", ok_action=Return(0))
    else:
        pass
    hide setup_welcome_text
    call setup_prepare_beta
    return

label setup_prepare_beta:
    if "beta" in config.version:
        show setup_prerelease_info zorder 3:
            xalign 0.5 yalign 0.3
        show setup_process_files zorder 3:
            xalign 0.5 yalign 0.85
        show loader zorder 4:
            xalign 0.5 yalign 0.7
        pause 5.0
        hide setup_prerelease_info
        hide loader
        hide mojave setup header
        call setup_feedback_mode
    else:
        call setup_tos
    return

label setup_feedback_mode:
    if "beta" in config.version:
        show setup_beta_check_header zorder 3:
            xalign 0.5 yalign 0.18
        show setup_feedback zorder 3 at truecenter
        show setup_send_feedback_info zorder 4:
            xalign 0.5 yalign 0.3
        $ renpy.pause(5.0)
        hide setup_process_files
        hide setup_feedback
        hide setup_send_feedback_info
        hide setup_beta_check_header
    else:
        pass
    call setup_tos
    return

label setup_tos:
    show setup_game_tos_header zorder 3:
        xalign 0.5 yalign 0.18
    show setup_tos_info zorder 3:
        xalign 0.5 yalign 0.3
    show setup_tos_text zorder 3:
        xalign 0.5 yalign 0.5
    $ ui.vbox(xalign=xcoordinate,yalign=ycoordinate)
    $ ui.textbutton("Agree", ui.returns("choice1"), style="confirm_button", xalign=.5)
    $ ui.close()
    $ choice_selected=ui.interact()
    call screen confirm_alert(title="Confirm Agreement", message="I have read and agreed to the terms of the software license agreement.", no_action_message="Disagree", no_action=Return(1), yes_action_message="Agree", yes_action=Return(0))
    if _return == 1:
        stop music fadeout 1.0
        scene black
        pause 0.5
        call rsod_cyanide
    else:
        pass
    hide setup_tos_info
    hide setup_tos_text
    call setup_tos_game
    return

label setup_tos_game:
    show setup_game_tos_info zorder 3:
        xalign 0.5 yalign 0.3
    show setup_game_tos_text zorder 3:
        xalign 0.5 yalign 0.5
    $ ui.vbox(xalign=xcoordinate,yalign=ycoordinate)
    $ ui.textbutton("Agree", ui.returns("choice1"), style="confirm_button", xalign=.5)
    $ ui.close()
    $ choice_selected=ui.interact()
    call screen confirm_alert(title="Confirm Agreement", message="I have read and agreed to the terms of the game's license agreement.", no_action_message="Disagree", no_action=Return(1), yes_action_message="Agree", yes_action=Return(0))
    if _return == 1:
        stop music fadeout 1.0
        scene black
        pause 0.5
        call rsod_cyanide
    else:
        pass
    hide setup_game_tos_info
    hide setup_game_tos_header
    hide setup_game_tos_text
    call setup_accounts
    return

label setup_accounts:
    show setup_accounts_header zorder 3:
        xalign 0.5 yalign 0.18
    show setup_create_accnt zorder 3:
        xalign 0.5 yalign 0.3
    python:
        if persistent.playername:
            p = persistent.playername
            SystemUIServer.send_temporary_notification("Username detected", "Press Respond to use the name '" + p + "'.", action=Jump("setup_complete"))
        player = renpy.input(' ')
        player = player.strip()
        persistent.playername = player
    show loader zorder 4:
        xalign 0.5 yalign 0.7
    $ renpy.pause(3.0)
    call setup_complete
    return

label setup_complete:
    hide setup_create_accnt
    hide loader
    python:
        with open(config.basedir + '/game/profiles.moj', 'w+') as f:
            f.write(player + ":sierra")
    show setup_complete_thankyou zorder 3:
        xalign 0.5 yalign 0.3
    $ renpy.pause(3.0)
    return
