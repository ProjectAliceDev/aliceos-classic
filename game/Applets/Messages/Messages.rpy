## Messages CoreService Applet
# Send and receive messages from characters
# Author(s): Marquis Kurt (@alicerunsonfedora)
# Copyright: (C) 2018

init -10 python:
    class MessagesApp(Applet):
        ## App Manifest
        # Define important information about your app here.
        # This information will be used in places like the
        # Control Center, notification badges, apps menus,
        # and the desktop shell.

        # Provide a short name and a long name for your app.
        short_name = "Messages"
        long_name = "Messages"

        # Provide the author information, version number, and
        # description of your app, as where as the name of the
        # folder that your applet lives in.
        app_dir = "Messages"
        author = "AliceOS Developers"
        version = "0.1.0"
        description = """\
Send and receive text messages from characters in a Ren'Py project.
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
        permissions = {pm_notify}

        def report_send_error():
            renpy.call_screen("alert", "Message Not Sent", "The message couldn't be sent.", ok_action=Return(0))
    
    messages = MessagesApp()

## Applet Code
# Define your applet after you have established your
# app's manifest here. This may include screens, labels,
# or definitions. Please keep all of your applet's code
# in this file.