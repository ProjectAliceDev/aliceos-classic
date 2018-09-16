## ASErrorHandler.rpy
# RSOD Managger
# Author: Marquis Kurt (@alicerunsonfedora)
# Copyright: (C) 2018
# RSOD-related files
init -1000 python:
    rsod_messages = {
                     "boot": "INACCESSIBLE_BOOT_DEVICE",
                     "gobfadu_lock": "GOBFADU_INTEGRITY_VIOLATION",
                     "applet_lock": "APPLET_INTEGRITY_VIOLATION",
                     "frame_lock": "FRAME_INTEGRITY_VIOLATION",
                     "os_lock": "SYSTEM_INTEGRITY_VIOLATION",
                     "gui_lock": "GUI_INTEGRITY_VIOLATION",
                     "resource_lock": "RESOURCE_INTEGRITY_VIOLATION",
                     "test_lock": "TEST_INTEGRITY_VIOLATION",
                     "missing_cyanide": "MISSING_CYANIDE_INSTRUMENT"
                    }
    rsod_search_text = "If you'd like to know more, you can search online later for this error: "

image rsod_bg_backup = "#c6262e"
image rsod_bg = "Resources/rsod_overlay.png"
image rsod_face = Text(":(", font="Resources/systemfont/Regular.ttf", size=128, color="#ff8c82", style="_default")
image rsod_generic_message = Text("AliceOS ran into an error it couldn't handle and\nneeds to restart.", font="Resources/systemfont/Regular.ttf", size=48, color="#ffffff", style="_default")

image rsod_search_error_text = Text(rsod_search_text, font="Resources/systemfont/Light.ttf", size=24, color="#ff8c82", style="_default")

image rsod_boot_message = Text(rsod_messages["boot"], font="Resources/systemfont/Medium.ttf", size=24, color="#ffffff", style="_default")
image rsod_gobfadu_lock_message = Text(rsod_messages["gobfadu_lock"], font="Resources/systemfont/Medium.ttf", size=24, color="#ffffff", style="_default")
image rsod_gobfadu_applet_lock_message = Text(rsod_messages["applet_lock"], font="Resources/systemfont/Medium.ttf", size=24, color="#ffffff", style="_default")
image rsod_gobfadu_frame_lock_message = Text(rsod_messages["frame_lock"], font="Resources/systemfont/Medium.ttf", size=24, color="#ffffff", style="_default")
image rsod_gobfadu_os_lock_message = Text(rsod_messages["os_lock"], font="Resources/systemfont/Medium.ttf", size=24, color="#ffffff", style="_default")
image rsod_gobfadu_gui_lock_message = Text(rsod_messages["gui_lock"], font="Resources/systemfont/Medium.ttf", size=24, color="#ffffff", style="_default")
image rsod_gobfadu_resource_lock_message = Text(rsod_messages["resource_lock"], font="Resources/systemfont/Medium.ttf", size=24, color="#ffffff", style="_default")
image rsod_gobfadu_test_lock_message = Text(rsod_messages["test_lock"], font="Resources/systemfont/Medium.ttf", size=24, color="#ffffff", style="_default")
image rsod_cyanide_message = Text(rsod_messages["missing_cyanide"], font="Resources/systemfont/Medium.ttf", size=24, color="#ffffff", style="_default")

label rsod_boot:
    scene rsod_bg
    show rsod_face:
        xpos 0.1
        yalign 0.3
    show rsod_generic_message:
        xpos 0.1
        yalign 0.6
    show rsod_search_error_text:
        xpos 0.1
        yalign 0.75
    show rsod_boot_message:
        xpos 0.1
        yalign 0.8
    pause 10.0
    $ renpy.utter_restart()
    return

label rsod_cyanide:
    scene rsod_bg
    show rsod_face:
        xpos 0.1
        yalign 0.3
    show rsod_generic_message:
        xpos 0.1
        yalign 0.6
    show rsod_search_error_text:
        xpos 0.1
        yalign 0.75
    show rsod_cyanide_message:
        xpos 0.1
        yalign 0.8
    pause 10.0
    $ renpy.utter_restart()
    return
