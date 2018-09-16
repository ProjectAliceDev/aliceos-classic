## Branding.rpy
# AliceOS Branding Styling
# Author: Marquis Kurt (@alicerunsonfedora)
# Copyright: (C) 2018

init python:
    aliceTime = renpy.random.random() * .5 + .5
    alicePos = 0
    aliceOffset = 0
    aliceZoom = 1

    def chibiAliceHop(trans, st, at):
        global alicePos
        global aliceOffset
        global aliceZoom
        if st > .16:
            if alicePos > 0:
                alicePos = renpy.random.randint(-2,0)
            elif alicePos < 0:
                alicePos = renpy.random.randint(0,2)
            else:
                alicePos = renpy.random.randint(-2,2)
            if trans.xoffset * alicePos > 5: alicePos *= -1
            return None
        if alicePos > 0:
            trans.xzoom = -1
        elif alicePos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * alicePos
        aliceOffset = trans.xoffset
        aliceZoom = trans.xzoom
        return 0

    def randomPauseAlice(trans, st, at):
        global aliceTime
        if st > aliceTime:
            global AliceTime
            aliceTime = renpy.random.random() * .5 + .5
            return None
        return 0

image alice_os_name = "Resources/logomark-white.png"
image powered_by_text = Text("Powered by", font="Resources/systemfont/Regular.ttf")
image boot_copyright = Text("(C) 2018 | AliceOS Developers. Licensed under GNU GPLv3. All rights reserved.", font="Resources/systemfont/Light.ttf", size=14)

image alice_os_logomark = "Resources/logomark.png"
image alice_boot_mascot:
    "Resources/chibi.png"
    xoffset aliceOffset xzoom aliceZoom
    block:
        function randomPauseAlice
        parallel:
            function chibiAliceHop
        repeat