## UIView.rpy
# User interface elements for AliceOS
# Author: Marquis Kurt (@alicerunsonfedora)
# Copyright: (C) 2018

## Screens
# Default Window

init -501 screen UIWindow(applet):
    modal False
    zorder 200
    add "Resources/systemui/overlay_confirm.png"

    frame:
        xpadding 16
        ypadding 16
        xanchor -16
        yanchor -16
        xsize 1248
        ysize 688
        has vbox:
            spacing 16
            hbox:
                xsize 1216
                hbox:
                    python:
                        app_window_title = applet.long_name.upper()
                    add "Applets/" + applet.app_dir + "/Resources/icons/" + applet.icons[24]
                    text _(app_window_title):
                        style "app_window_name"
                        xalign 0.2
                imagebutton idle "Resources/systemui/close_button.png" hover "Resources/systemui/close_button_hover.png" action Return(0):
                        xalign 1.0

init -1 style app_default_text is gui_text

init -1 style app_default_text:
    color "#000"
    font "Resources/systemfont/Regular.ttf"
    outlines []
    text_align 0.0
    layout "tex"

init -501 screen UIWindowContent():
    frame:
        xanchor -16
        yanchor -68
        xsize 1248
        ysize 635


init -1 style app_window_name:
    color "#7e8087"
    font "Resources/systemfont/Regular.ttf"
    first_indent 8
    size 20
    outlines []
    text_align 0
    layout "tex"