## RenPy Applet
# The "applet" for VN integration into AliceOS.
# Author: Marquis Kurt (@alicerunsonfedora)
# Copyright: (C) 2018

## App Manifest
# Define important information about your app here.
# This information will be used in places like the
# Control Center, notification badges, apps menus,
# and the desktop shell.

# Provide a short name and a long name for your app.
define renpy_short_name = build.name
define renpy_name = config.name

# Provide the author information, version number, and
# description of your app.
define renpy_author = "Ren'Py Team"
define renpy_version = config.version
define renpy_description = gui.about

# Define your icons heres. They should be located in
# Resources/icons/
define renpy_icon_16 = "renpy_16.png"
define renpy_icon_24 = "renpy_24.png"
define renpy_icon_32 = "renpy_32.png"
define renpy_icon_48 = "renpy_48.png"
define renpy_icon_64 = "renpy_64.png"
define renpy_icon_128 = "renpy_128.png"

## Applet Code
# Define your applet after you have established your
# app's manifest here. This may include screens, labels,
# or definitions. Please keep all of your applet's code
# in this file.

label ask_all_permissions():
    "Before you play this visual novel, we need you to do a couple of things."
    "We care about your data and privacy, and we want to only do things on your behalf."
    "To do this, we must ask you permissions to access AliceOS and send notifications."
    "We hope you understand and comply with AliceOS's data regulation policies."

    call screen ask_permission(renpy_name, allow_un, no_action=Return(1), yes_action=Return(0))
    python:
        if _return == 1:
            renpy.jump("ask_all_permissions_failure")

    call screen ask_permission(renpy_name, allow_fs, no_action=Return(1), yes_action=Return(0))
    python:
        if _return == 1:
            renpy.jump("ask_all_permissions_failure")

    call screen ask_permission(renpy_name, allow_sip, no_action=Return(1), yes_action=Return(0))
    python:
        if _return == 1:
            renpy.jump("ask_all_permissions_failure")
    "Alright! It looks like you're ready to play this visual novel."
    "Thank you! We hope you enjoy it."
    return

label ask_all_permissions_failure:
    "We're sorry, but it looks like you won't give us the permissions needed to run your visual novel properly."
    "We respect your choice and will therefore not continue."
    return