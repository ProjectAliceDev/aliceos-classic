#GOBFADU Policy 1.8 DDLC Edition 6/15/2018
#Python 3.8 MOS Edition 6/12/2018

label gobfadupolicygobfadu64:
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    if renpy.exists("../game/CoreServices/Bootloader.rpyc"):
        call adutarinstall
    else:
        call GOBFADUOSLock

label adutarinstall:
    if renpy.exists("../game/Setup.rpyc")
        call gobfaduverify
    else:
        call GOBFADUOSLock

label gobfaduverify:
    if renpy.exists("../game/GOBFADULock.rpyc"):
        call gobfadupolicyframe
    else:
        call screen dialog(message="GOBFADU Assets Missing. Please reinstall the Operating System.", ok_action=Function(renpy.quit))