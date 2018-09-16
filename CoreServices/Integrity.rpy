## Integrity.rpy
# System Integrity Protection via GOBFADU policy
# Author: Monika/D. Va (@GanstaKingofSA), Marquis Kurt (@alicerunsonfedora)
# Copyright: (C) 2018
image integrity_message = Text("Checking system integrity...", font="Resources/systemfont/Light.ttf", size=14, style="_default")

label Integrity:
    # Show Integrity check message before loading
    show integrity_message zorder 3:
        xalign 0.5
        yalign 0.8
    call gobfadu_policy_gobfadu
return
