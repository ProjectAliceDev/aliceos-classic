## UserNotifications.rpy
# Notification Management System
# Author: Marquis Kurt (@alicerunsonfedora)
# Copyright: (C) 2018

## Screen Implementation
# Alert
screen alert(title, message, ok_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "Resources/systemui/overlay_confirm.png"

    frame:
        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(title):
            style "confirm_prompt"
            xalign 0.5

        label _(message):
            style "confirm_prompt_details"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action


# Confirm
screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

# Detailed Dialog
screen confirm_alert(title, message, no_action_message, no_action, yes_action_message, yes_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(title):
            style "confirm_prompt"
            xalign 0.5

        label _(message):
            style "confirm_prompt_details"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _(no_action_message) action no_action:
                style "confirm_button_negative"
            textbutton _(yes_action_message) action yes_action

# Permissive Dialog (Variant of Detailed Dialog)
screen ask_permission(app_name, action, no_action,  yes_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(app_name + " Would Like To\n" + action):
            style "confirm_prompt"
            xalign 0.5

        if action == allow_un:
            label _(allow_un_details):
                style "confirm_prompt_details"
                xalign 0.5
        elif action == allow_fs:
            label _(allow_fs_details):
                style "confirm_prompt_details"
                xalign 0.5
        elif action == allow_sip:
            label _(allow_sip_details):
                style "confirm_prompt_details"
                xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Don't Allow") action no_action:
                style "confirm_button_negative"
            textbutton _("OK") action yes_action

# Banner
screen banner(applet, title, message, response):
    zorder 100
    frame at banner_appear:
        style "banner_frame"
        xpadding 16
        ypadding 16
        xalign 0.5
        yalign 0.025

        vbox:
            hbox:
                add "Applets/" + applet.app_dir + "/Resources/icons/" + applet.icons[24]
                text applet.short_name:
                    style "banner_frame_app"
                textbutton _("Respond") action response:
                    style "banner_dismiss"
                    xalign 0.9
                    ypadding 0
            null height 12
            text title:
                style "banner_frame_sender"
            text message:
                style "banner_frame_message"

    timer 5.0 action Return(0)

# Ren'Py Banner (Notification)
screen notify(message):
    zorder 100
    frame at banner_appear:
        style "banner_frame"
        xpadding 16
        ypadding 16
        xalign 0.5
        yalign 0.025

        vbox:
            hbox:
                # add "mod_assets/images/gui/frame_notify_default.png"
                text config.name:
                    style "banner_frame_app"
            null height 12
            text "Hey, something's happening!":
                style "banner_frame_sender"
            text message:
                style "banner_frame_message"

    timer 3.25 action Hide('notify')


transform -1 banner_appear:
    on show:
        yalign 0.0 xalign 0.5
        linear 0.25 ypos 0.025
    on hide:
        yalign 0.025 xalign 0.5
        linear 0.25 yalign -1.0

# Stylesheet
init -1 style confirm_frame is gui_frame
init -1 style confirm_prompt is gui_prompt
init -1 style confirm_prompt_text is gui_prompt_text
init -1 style confirm_prompt_details is gui_prompt
init -1 style confirm_prompt_details_text is gui_prompt_text
init -1 style confirm_button is gui_medium_button
init -1 style confirm_button_negative is gui_medium_button
init -1 style confirm_button_text is gui_medium_button_text
init -1 style confirm_button_negative_text is gui_medium_button_text


init -1 style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

init -1 style confirm_prompt_text:
    color "#000"
    font "Resources/systemfont/Bold.ttf"
    outlines []
    text_align 0.5
    layout "subtitle"

init -1 style confirm_prompt_details_text:
    color "#000"
    font "Resources/systemfont/Regular.ttf"
    outlines []
    text_align 0.5
    layout "subtitle"

init -1 style confirm_button:
    properties gui.button_properties("confirm_button")
    color "007AFF"
    font "Resources/systemfont/Regular.ttf"
    hover_color "#5AC8FA"
    outlines []

init -1 style confirm_button_negative:
    properties gui.button_properties("confirm_button")
    color "007AFF"
    font "Resources/systemfont/Bold.ttf"
    hover_color "#5AC8FA"
    outlines []

init -1 style confirm_button_text is navigation_button_text:
    properties gui.button_text_properties("confirm_button")
    color "007AFF"
    font "Resources/systemfont/Regular.ttf"
    hover_color "#5AC8FA"
    outlines []

init -1 style confirm_button_negative_text is navigation_button_text:
    properties gui.button_text_properties("confirm_button")
    color "007AFF"
    font "Resources/systemfont/Bold.ttf"
    hover_color "#5AC8FA"
    outlines []

init -1 style banner_frame:
    background Frame([ "gui/frame.png", "gui/banner_frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

init -1 style banner_frame_app:
    color "333333"
    font "Resources/systemfont/Regular.ttf"
    first_indent 8
    min_width 576
    size 20
    outlines []
    text_align 0
    layout "tex"

init -1 style banner_frame_sender:
    color "#000"
    font "Resources/systemfont/Bold.ttf"
    size 22
    outlines []
    text_align 0
    layout "tex"

init -1 style banner_frame_message:
    color "#000"
    font "Resources/systemfont/Regular.ttf"
    size 22
    outlines []
    text_align 0
    layout "tex"

init -1 style banner_dismiss is navigation_button_text:
    properties gui.button_text_properties("confirm_button")
    color "333"
    size 18
    font "Resources/systemfont/Regular.ttf"
    hover_color "000"
    outlines []

init -1 style banner_dismiss_text is navigation_button_text:
    properties gui.button_text_properties("confirm_button")
    color "000"
    size 18
    font "Resources/systemfont/Bold.ttf"
    hover_color "333"
    outlines []

## Screen Definitions
define allow_un = "Send Notifications"
define allow_fs = "Access The File System"
define allow_sip = "Modify System Settings"

define allow_un_details = "Notifications may include alerts, sounds, \nand banners. These can be configured in \nControl Center."
define allow_fs_details = "By giving this app access, this app can\nmodify files beyond your Home folder.\nOnly give file system access to apps that \nyou trust."
define allow_sip_details = "By giving this app access, this app can\nmodify system settings and control\nyour computer. Only give this to apps \nthat you trust."