## ASErrorHandler.rpy
# RSOD Managger
# Author: Marquis Kurt (@alicerunsonfedora)
# Copyright: (C) 2018
# RSOD-related files
init -1000 python:
    class ASErrorTypes():

        headers = {
            "FS": "FILESYSTEM_",
            "Screen": "SCREEN_",
            "SIP": "SEC_ADD_",
            "Setup": "SETUP_"
        }

        fserror = {
            "NoPerm": "INSUFFICIENT_PERMISSIONS",
            "UnreadableSector": "SECTOR_INVALID",
            "CriticalFileMissing": "CRITICAL_FILE_MISSING"
        }

        screrr = {
           "UnterminatedProgress": "PROGRESS_VOID",
           "MissingScreen": "SCREEN_UNDEFINED",
           "ScreenCorrupt": "SCREEN_INVALID" 
        }

        siperr = {
            "SIPComponentFailure": "SIP_FAILED_INIT",
            "SIPCriticalFileCheckFail": "SIP_CRITICAL_FILE_INVALID",
            "SIPComponentProfileFail": "SIP_COMPONENT_FAILED"
        }

        pisaerr = {
            "NullInput": "INPUT_REUTRNED_NULL"
        }

        def get_error(self, header, error):
            return header + error

        def __init__(self):
            pass

    SetASError = ASErrorTypes()

## ThrowASError screen
screen ThrowASError(error_type):
    
    modal True
    zorder 100
    style_prefix "rsod"
    add "#c6262e"
    add "Resources/rsod/background.png"

    vbox:
        xalign 0.2

        null height 192

        text _(":("):
            style "rsod_emoticon"
            yalign 0.4

        null height 56

        text _("AliceOS ran into an error it couldn't handle and\nneeds to restart."):
            style "rsod_title_text"
            yalign 0.7

        null height 32
        
        text _("If you'd like to know more, you can search the error database later for this error: "):
            style "rsod_prompt_text"

        text _(error_type):
            style "rsod_error_text"

    add "Resources/rsod/overlay.png" # Adds the QR Code

    timer 10.0 action Return(1)