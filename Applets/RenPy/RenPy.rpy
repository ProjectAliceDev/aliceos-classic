## RenPy Applet
# The "applet" for VN integration into AliceOS.
# Author(s): Marquis Kurt (@alicerunsonfedora), Abdülhamit Yilmaz (@abduelhamit)
# Copyright: (C) 2018

init python:
    class RenpyApp(Applet):
        ## App Manifest
        # Define important information about your app here.
        # This information will be used in places like the
        # Control Center, notification badges, apps menus,
        # and the desktop shell.

        # Provide a short name and a long name for your app.
        short_name = "DDLC"
        long_name = "Doki Doki Literature Club"

        # Provide the author information, version number, and
        # description of your app, as where as the name of the
        # folder that your applet lives in.
        app_dir = "RenPy"
        author = "Team Salvato"
        version = "1.1.1"
        description = gui.about

        # Define your icons here. They should be located in 
        # your Applet's Resources/icons/ folder
        icons = {
            16: "16-16.png",
            24: "24-24.png",
            32: "32-32.png",
            64: "64-64.png",
            128: "128-128.png",
            256: "256-256.png"
        }

        # Define what permissions your applet will need.
        permissions = {pm_notify, pm_files, pm_sysadmin}

        def notify_new_char(self, charname):
            self.send_temporary_notification("New character added!", "Congrats! \""+ charname +"\" has been added to DDLC.", action=Return(1))

        def send_mio_message(self, messagetext):
            messages.send_temporary_notification("Mio", messagetext, action=Return(1))
    
    renpyApp = RenpyApp()

## Applet Code
# Define your applet after you have established your
# app's manifest here. This may include screens, labels,
# or definitions. Please keep all of your applet's code
# in this file.

# RSOD Information for Demo End (eg. 'Act 2 is missing')
image rsod_corrupted_act_message = Text("ACT_FAULT_IN_NONACT_AREA", font="Resources/systemfont/Medium.ttf", size=24, color="#ffffff", style="_default")

label rsod_missing_act:
    scene rsod_bg
    show rsod_face:
        xpos 0.1
        yalign 0.3
    show rsod_generic_message:
        xpos 0.1
        yalign 0.6
    show rsod_search_error_text:
        xpos 0.1
        yalign 0.75
    show rsod_corrupted_act_message:
        xpos 0.1
        yalign 0.8
    pause 10.0
    $ renpy.utter_restart()
return