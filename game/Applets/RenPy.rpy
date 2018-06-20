## RenPy Applet
# The "applet" for VN integration into AliceOS.
# Author: Marquis Kurt (@alicerunsonfedora)
# Copyright: (C) 2018

python:
    RenpyApp = Applet()
    ## App Manifest
    # Define important information about your app here.
    # This information will be used in places like the
    # Control Center, notification badges, apps menus,
    # and the desktop shell.

    # Provide a short name and a long name for your app.
    RenpyApp.short_name = build.name
    RenpyApp.long_name = config.name

    # Provide the author information, version number, and
    # description of your app.
    RenpyApp.Author = "Ren'Py Team"
    RenpyApp.version = config.version
    RenpyApp.description = gui.about

    # Define your icons heres. They should be located in 
    # your Applet's Resources/icons/ folder
    RenpyApp.icons = {
        16: "renpy_16.png",
        24: "renpy_24.png",
        32: "renpy_32.png",
        64: "renpy_64.png",
        128: "renpy_128.png",
        256: "renpy_256.png"
    }

    # Define what permissions your applet will need.
    RenpyApp.permissions = [pm_notify, pm_files, pm_sysadmin]

## Applet Code
# Define your applet after you have established your
# app's manifest here. This may include screens, labels,
# or definitions. Please keep all of your applet's code
# in this file.