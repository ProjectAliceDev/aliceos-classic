## ASErrorHandler.rpy
# RSOD Managger
# Author: Marquis Kurt (@alicerunsonfedora)
# Copyright: (C) 2018
# RSOD-related files
init -1000 python:
    aliceos_default_errors = {
        "boot_fault": "INACCESSIBLE_BOOT_DEVICE",
        "cyanide": "MISSING_CYANIDE_INSTRUMENT",
        "label_fault": "LABEL_FAULT_IN_NONLABEL_AREA",
        "setup_fail":"SETUP_ASSISTANT_FAIL"
    }


## ThrowASError screen
screen ThrowASError(error_type):
    modal False
    zorder 100
    style_prefix "rsod"
    add "#c6262e"
    add "Resources/rsod_overlay.png"

    text _(":("):
        style "rsod_emoticon"
        xalign 0.075
        yalign 0.4

    text _("AliceOS ran into an error it couldn't handle and\nneeds to restart."):
        style "rsod_title_text"
        xalign 0.3
        yalign 0.7

    vbox:
        xalign 0.15
        yalign 0.85

        text _("If you'd like to know more, you can search online later for this error: "):
            style "rsod_prompt_text"

        text _(error_type):
            style "rsod_error_text"

    timer 10.0 action Return(1)