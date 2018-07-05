#GOBFADU Policy 1.8 DDLC Edition 6/15/2018
#Python 3.8 MOS Edition 6/12/2018

label gobfadupolicygobfadu:
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    if renpy.exists("../ddtar-screens.rpyc"):
        call adutarscript
    else:
        call GOBFADULock
label adutarscript:
    if renpy.exists("../game/script.rpyc")
        call adutarsplash
    else:
        call GOBFADULock

label adutarsplash:
    if renpy.exists("../game/splash.rpyc")
       call adutarmenu
    else:
       call GOBFADULock

label adutarmenu:
    if renpy.exists("../game/main_menu.rpyc")
        call adutaroptions
    else:
        call GOBFADULock

label adutaroptions:
    if renpy.existsI("../game/options.rpyc")
        call adutarimport
    else:
        call GOBFADULock 
label adutarimport:
    if renpy.exists("../game/import_ddlc.rpyc")
        call adutaroveride
    else:
        call GOBFADULock

label adutaroveride:
    if renpy.exists("../game/overides.rpyc")
        call gobfaduverify
    else:
        call GOBFADULock
label gobfaduverify:
    if renpy.exists("../game/GOBFADULock.rpyc"):
        call gobfadupolicyapplet
    else:
        call screen dialog(message="GOBFADU Assets Missing. Please reinstall the Operating System.", ok_action=Function(renpy.quit))
