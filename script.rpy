# This is a sample script with the bootscreen
# and setup included. Edit this to your liking

label splashscreen:
    call oem_boot_screen
    if not persistent.setup_complete:
        call setup
        persistent.setup_complete = True
        $ renpy.utter_restart()
    else:
        pass
    return

label start:
    return