#GOBFADU Policy 1.8 DDLC Edition 6/15/2018
#Python 3.8 MOS Edition 6/12/2018

label gobfadupolicyresources:
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    if renpy.exists("../game/Resources/branding.png"):
        call adutarico16
    else:
        call GOBFADUResourceLock
label adutarico16:
    if renpy.exists("../game/Resources/icons/renpy_16.png")
        call adutarico24
    else:
        call GOBFADUResourceLock

label adutarico24:
    if renpy.exists("../game/Resources/icons/renpy_24.png")
        call adutarico32
    else:
        call GOBFADUResourceLock

label adutarico32:
    if renpy.exists("../game/Resources/icons/renpy_32.png")
        call adutarico48
    else:
        call GOBFADUResourceLock

label adutarico48:
    if renpy.exists("../game/Resources/icons/renpy_48.png")
        call adutarico64
    else:
        call GOBFADUResourceLock
label adutarico64:
    if renpy.exists("../game/Resources/icons/renpy_64.png")
        call adutarico128
    else:
        call GOBFADUResourceLock

label adutarico128:
    if renpy.exists("../game/Resources/icons/renpy_128.png")
        call adutarfoblack
    else:
        call GOBFADUResourceLock

label adutarfoblack:
    if renpy.exists("../game/Resources/systemfont/Black.ttf")
        call adutarfoblaital
    else:
        call GOBFADUResourceLock

label adutarfoblaital:
    if renpy.exists("../game/Resources/systemfont/BlackItalic.ttf")
        call adutarfobold
    else:
        call GOBFADUResourceLock

label adutarfobold:
    if renpy.exists("../game/Resources/systemfont/Bold.ttf")
        call adutarfoboital
    else:
        call GOBFADUResourceLock

label adutarfoboital:
    if renpy.exists("../game/Resources/systemfont/BoldItalic.ttf")
        call adutarfoital:
    else:
        call GOBFADUResourceLock

label adutarfoital:
    if renpy.exists("../game/Resources/systemfont/Italic.ttf")
        call adutarfoli
    else:
        call GOBFADUResourceLock

label adutarfoli:
    if renpy.exists("../game/Resources/systemfont/Light.ttf")
        call adutarfolital
    else:
        call GOBFADUResourceLock

label adutarfoital:
    if renpy.exists("../game/Resources/systemfont/LightItalic.ttf")
        call adutarfomed
    else:
        call GOBFADUResourceLock

label adutarfomed:
    if renpy.exists("../game/Resources/systemfont/MediumItalic.ttf")
        call adutarfomedital
    else:
        call GOBFADUResourceLock

label adutarfomedital:
    if renpy.exists("../game/Resources/systemfont/MediumItalic.ttf")
        call adutarforeg
    else:
        call GOBFADUResourceLock
label adutarforeg:
    if renpy.exists("../game/Resources/systemfont/Regular.ttf")
        call adutarfothin
    else:
        call GOBFADUResourceLock
label adutarfothin:
    if renpy.exists("../game/Resources/systemfont/Thin.ttf")
        call adutarfothinital
    else:
        call GOBFADUResourceLock
label adutarfothinital:
    if renpy.exists("../game/Resources/systemfont/ThinItalic.ttf")
        call adutarrif
    else:
        call GOBFADUResourceLock
label adutarrif:
    if renpy.exists("../game/Resources/systemfont/branding/RifficFree-Bold.ttf")
        call adutarsysui
    else:
        call GOBFADUResourceLock
label adutarsysui:
    if renpy.exists("../game/Resources/systemui/frame_notify.png")
        call adutarsysuiframe
    else:
        call GOBFADUResourceLock
label adutarsysuiframe:
    if renpy.exists("../game/Resources/systemui/frame.png")
        call adutarovlay
    else:
        call GOBFADUResourceLock

label adutarsysuiframe:
    if renpy.exists("../game/Resources/systemui/overlay_confirm.png")
        call gobfaduverify
    else:
        call GOBFADUResourceLock

label gobfaduverify:
    if renpy.exists("../game/GOBFADUResourceLock.rpyc"):
        call gobfadupolicytests
    else:
        call screen dialog(message="GOBFADU Assets Missing. Please reinstall the Operating System.", ok_action=Function(renpy.quit))