## Console
# Command-line interface for AliceOS.
# Author(s): Marquis Kurt (@alicerunsonfedora), Abdülhamit Yilmaz (@abduelhamit)
# Copyright: (C) 2018

init python:
    class Console(Applet):
        ## App Manifest
        # Define important information about your app here.
        # This information will be used in places like the
        # Control Center, notification badges, apps menus,
        # and the desktop shell.

        # Provide a short name and a long name for your app.
        short_name = "Console"
        long_name = "AliceOS Console"

        # Provide the author information, version number, and
        # description of your app, as where as the name of the
        # folder that your applet lives in.
        app_dir = "Console"
        author = "Project Alice"
        version = "1.0.0beta3"
        description = """\
A command-line interface for AliceOS.
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
        permissions = {pm_notify, pm_files, pm_sysadmin}
    
    terminal = Console()

## Applet Code
# Define your applet after you have established your
# app's manifest here. This may include screens, labels,
# or definitions. Please keep all of your applet's code
# in this file.