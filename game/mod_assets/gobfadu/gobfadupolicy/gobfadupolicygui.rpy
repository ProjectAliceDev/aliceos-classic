#GOBFADU Policy 1.8 DDLC Edition 6/15/2018
#Python 3.8 MOS Edition 6/12/2018

label gobfadupolicygui:
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    if renpy.exists("../game/gui/banner_frame.png"):
        call adutarframe
    else:
        call GOBFADUGUILock
label adutarframe:
    if renpy.exists("../game/gui/frame.png")
        call adutaroverlay
    else:
        call GOBFADUGUILock

label adutaroverlay:
    if renpy.exists("../game/gui/overlay/confirm.png")
       call gobfaduverify
    else:
       call GOBFADUGUILock

label gobfaduverify:
    if renpy.exists("../game/GOBFADUGUILock.rpyc"):
        call gobfadupolicyresources
    else:
        call screen dialog(message="GOBFADU Assets Missing. Please reinstall the Operating System.", ok_action=Function(renpy.quit))