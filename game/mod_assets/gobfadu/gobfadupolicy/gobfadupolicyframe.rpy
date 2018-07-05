#GOBFADU Policy 1.8 DDLC Edition 6/15/2018
#Python 3.8 MOS Edition 6/12/2018

label gobfadupolicyframe:
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    if renpy.exists("../game/Frameworks/UserNotifications.rpyc"):
        call gobfaduverify
    else:
        call GOBFADUFrameLock
label gobfaduverify:
    if renpy.exists("../game/GOBFADULock.rpyc"):
        call gobfadupolicygui
    else:
        call screen dialog(message="GOBFADU Assets Missing. Please reinstall the Operating System.", ok_action=Function(renpy.quit))