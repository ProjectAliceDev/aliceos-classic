## Bootloader.rpy
# Boot Sequence and Splash Screen Manager
# Author: Name (@username)
# Copyright: (C) 2018

## Standard Bootloader
# This checks based on the OEM mode set in
# OEMSettings.rpy
label bootloader:
    if aliceos.oem_mode:
        stop music fadeout 1.0
        scene black with fade
        show powered_by_text:
            xalign 0.35
            yalign 0.4
        show alice_os_name at truecenter
        show boot_copyright:
            xalign 0.5
            yalign 1.0
        pause 5.0
    else:
        stop music fadeout 1.0
        scene black with fade
        show alice_os_logomark at truecenter
        show alice_boot_mascot:
            xalign 0.5
            yalign 0.3
        show boot_copyright:
            yalign 1.0
            xalign 0.5
        pause 5.0
    if not persistent.setup_complete:
        call setup
        $ persistent.setup_complete = True
        $ renpy.utter_restart()
    else:
        pass
    return
