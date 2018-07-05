## Pendleton.rpy
# A manager for handling system functions.
# Author(s): Marquis Kurt (@alicerunsonfedora)
# Copyright: (C) 2018

init -10 python:
    class Pendleton(Applet):
        ## App Manifest
        # Define important information about your app here.
        # This information will be used in places like the
        # Control Center, notification badges, apps menus,
        # and the desktop shell.

        # Provide a short name and a long name for your app.
        short_name = "Pendleton"
        long_name = "AliceOS System"

        # Provide the author information, version number, and
        # description of your app, as where as the name of the
        # folder that your applet lives in.
        app_dir = "Pendleton"
        author = "AliceOS Developers"
        version = "1.0.0"
        description = """\
AliceOS System sends notifications to inform you about actions that happen between apps and services on your computer.
        """

        # Define your icons here. They should be located in 
        # your Applet's Resources/icons/ folder
        icons = {
            16: "16.png",
            24: "24.png",
            32: "32.png",
            64: "64.png",
            128: "128.png",
            256: "256.png"
        }

        # Define what permissions your applet will need.
        # See the Applet Manifest wiki page for all possible
        # permissions
        permissions = {pm_notify}

        trusted_apps = {"renpy", "messages"}

        def disable_notify_untrusted_apps(self):
            if "blackbox" not in self.trusted_apps:
                persistent.aliceos_permissions["Blackbox_notify"] = False
            if "aliceangel" not in self.trusted_apps:
                persistent.aliceos_permissions["Alice_notify"] = False
            if "renpy" not in self.trusted_apps:
                persistent.aliceos_permissions["DDLC_notify"] = False
            if "messages" not in self.trusted_apps:
                persistent.aliceos_permissions["Messages_notify"] = False

        def disable_notify_all_apps(self):
            persistent.aliceos_permissions["Blackbox_notify"] = False
            persistent.aliceos_permissions["Alice_notify"] = False
            persistent.aliceos_permissions["DDLC_notify"] = False
            persistent.aliceos_permissions["Messages_notify"] = False

        def enable_notify_all_apps(self):
            persistent.aliceos_permissions["Blackbox_notify"] = True
            persistent.aliceos_permissions["Alice_notify"] = True
            persistent.aliceos_permissions["DDLC_notify"] = True
            persistent.aliceos_permissions["Messages_notify"] = True

        def __init__(self):

            # Pendleton is a system-wide service. This command overrrides
            # any permissions and takes on a system-like role. This should
            # NOT be used for third-party Applets!
            persistent.aliceos_permissions["Pendleton_notify"] = True
                
    
    SystemUIServer = Pendleton()

## Applet Code
# Define your applet after you have established your
# app's manifest here. This may include screens, labels,
# or definitions. Please keep all of your applet's code
# in this file.
image resettext = Text("{color=#fff}Resetting AliceOS...{/color}", font="Resources/systemfont/Light.ttf", size=40, style="_default")
image deletesavetext = Text("{color=#fff}Deleting save data...{/color}", font="Resources/systemfont/Light.ttf", size=40, style="_default")


label utter_reset:
    scene black
    show resettext at truecenter
    pause 2.0
    $ persistent._clear()
    $ renpy.utter_restart()
    return

label save_reset:
    scene black
    show deletesavetext at truecenter
    pause 2.0
    $ delete_all_saves()
    $ renpy.utter_restart()
    return