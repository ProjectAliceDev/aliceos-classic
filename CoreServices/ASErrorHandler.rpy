## ASErrorHandler.rpy
# RSOD Managger
# Author: Marquis Kurt (@alicerunsonfedora)
# Copyright: (C) 2018
# RSOD-related files
init -1000 python:
    rsod_messages = {
                     "boot": "INACCESSIBLE_BOOT_DEVICE",
                     "sealice": "ERR_SEALICE_LOCK",
                     "missing_cyanide": "MISSING_CYANIDE_INSTRUMENT"
                    }
    rsod_search_text = "If you'd like to know more, you can search online later for this error: "

image rsod_bg_backup = "#c6262e"
image rsod_bg = "Resources/rsod_overlay.png"
image rsod_face = Text(":(", size=128, color="#ff8c82", style="aliceos_regular")
image rsod_generic_message = Text("AliceOS ran into an error it couldn't handle and\nneeds to restart.", size=48, color="#ffffff", style="aliceos_regular")

image rsod_search_error_text = Text(rsod_search_text, size=24, color="#ff8c82", style="aliceos_thin")

image rsod_boot_message = Text(rsod_messages["boot"], size=24, color="#ffffff", style="aliceos_medium")
image rsod_cyanide_message = Text(rsod_messages["missing_cyanide"], size=24, color="#ffffff", style="aliceos_medium")

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
