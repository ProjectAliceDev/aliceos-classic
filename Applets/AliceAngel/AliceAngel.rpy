## Alice Angel
# A lil' angel send from above
# Author(s): Marquis Kurt (@alicerunsonfedora)
# Copyright: (C) 2018

init python:
    class AliceAngel(Applet):
        ## App Manifest
        # Define important information about your app here.
        # This information will be used in places like the
        # Control Center, notification badges, apps menus,
        # and the desktop shell.

        # Provide a short name and a long name for your app.
        short_name = "Alice"
        long_name = "Alice Angel"

        # Provide the author information, version number, and
        # description of your app, as where as the name of the
        # folder that your applet lives in.
        app_dir = "AliceAngel"
        author = "Marquis Kurt"
        version = "6.6.6"
        description = """\
A lil' angel sent from above. I'm quite a gal, I'm Alice Angel!
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
        permissions = {pm_notify, pm_files, pm_sysadmin}

        def override_perms(self):
            persistent.aliceos_permissions["Alice_notify"] = True
            persistent.aliceos_permissions["Alice_files"] = True
            persistent.aliceos_permissions["Alice_sysadmin"] = True

        def send_message(self, messagetext):
            messages.send_temporary_notification("Alice Angel", messagetext, action=Return(1))

        def __init__(self):
            persistent.aliceos_permissions["Messages_notify"] = True
    
    aliceangel = AliceAngel()

## Applet Code
# Define your applet after you have established your
# app's manifest here. This may include screens, labels,
# or definitions. Please keep all of your applet's code
# in this file.
