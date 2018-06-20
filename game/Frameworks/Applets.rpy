## Applets.rpy
# The framework for applets
# Author(s): Marquis Kurt (@alicerunsonfedora), Abdülhamit Yilmaz (@abduelhamit)
# Copyright: (C) 2018

init -10000 python:
    pm_notify = "notifications"
    pm_files = "filesystem"
    pm_sysadmin = "administrator"

    class Applet(object):
        # General manifest items
        short_name = "Short Name"
        long_name = "Long Name"
        app_dir = "Applet"
        author = "Author"
        version = "0.0.0"
        description = """\
        This is a sample description of my app.
        """
        # Icons
        icons = {
            16: "app_16.png",
            24: "app_24.png",
            32: "app_32.png",
            64: "app_64.png",
            128: "app_128.png",
            256: "app_256.png"
        }

        # Security permissions
        # Possible entries: "notifications", "filesystem", "administrator"
        permissions = {
            pm_notify,
            pm_files,
            pm_sysadmin
        }

        # Simplified Functions
        # These functions make use of AliceOS's frameworks so that developers
        # don't have to code in their own set. These include asking the player
        # all of the app's permissions, sending temporary notifications, etc.

        # Ask All Permissions
        # If a developer wants access information immediately rather than when
        # needed, this function should be called first.
        def ask_app_permissions(self):
            if pm_notify in self.permissions:
                renpy.call_screen("ask_permission", app_name=self.long_name, action=allow_un, no_action=Return(1), yes_action=Return(0))
                notification_permission = _return

            if pm_files in self.permissions:
                renpy.call_screen("ask_permission", app_name=self.long_name, action=allow_fs, no_action=Return(1), yes_action=Return(0))
                filesystem_permission = _return

            if pm_sysadmin in self.permissions:
                renpy.call_screen("ask_permission", app_name=self.long_name, action=allow_sip, no_action=Return(1), yes_action=Return(0))
                administrator_permission = _return

        # Send Temporary Notification
        # For basic control, developers can use this function to send banner
        # notifications to the player without needing to define the screen
        # itself. 
        def send_temporary_notification(self, sender, contents, action):
            renpy.call_screen("banner", applet=self, title=sender, message=contents, response=action)


        def __init__(self):
            pass
