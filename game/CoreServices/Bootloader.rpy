## Bootloader.rpy
# Boot Sequence and Splash Screen Manager
# Author: Name (@username)
# Copyright: (C) 2018

# OEM Boot Screen (should be called from splashscreen)
# Displays "Powered by AliceOS" text
label oem_boot_screen:
    stop music fadeout 1.0
    scene black with fade
    show powered_by_text:
        xalign 0.3
        yalign 0.4
    show alice_os_name at truecenter
    show boot_copyright:
        xalign 0.5
        yalign 1.0
    pause 3.0
    return