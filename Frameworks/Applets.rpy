## Applets.rpy
# The framework for applets
# Author(s): Marquis Kurt (@alicerunsonfedora), Abdülhamit Yilmaz (@abduelhamit)
# Copyright: (C) 2018

init -100000 python:
    persistent.aliceos_permissions = {}

init -10000 python:
    pm_notify = "notifications"
    pm_files = "filesystem"
    pm_sysadmin = "administrator"

    """
    An Applet object.
    """
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
            store.notification_permission = False
            store.filesystem_permission = False
            store.administrator_permission = False
            
            if pm_notify in self.permissions:
                renpy.call_screen("ask_permission", app_name=self.long_name, action=allow_un, no_action=Return(1), yes_action=[SetVariable("notification_permission", True), Return(0)])

            if pm_files in self.permissions:
                renpy.call_screen("ask_permission", app_name=self.long_name, action=allow_fs, no_action=Return(1), yes_action=[SetVariable("filesystem_permission", True), Return(0)])

            if pm_sysadmin in self.permissions:
                renpy.call_screen("ask_permission", app_name=self.long_name, action=allow_sip, no_action=Return(1), yes_action=[SetVariable("administrator_permission", True), Return(0)])
            
            key = self.short_name + "_notify"
            value = store.notification_permission
            persistent.aliceos_permissions[key] = value

            key = self.short_name + "_files"
            value = store.filesystem_permission
            persistent.aliceos_permissions[key] = value

            key = self.short_name + "_sysadmin"
            value = store.administrator_permission
            persistent.aliceos_permissions[key] = value

            # with open(config.basedir + "/game/" + self.app_dir + ".apf", "w+") as f:
            #     if pm_notify in self.permissions:
            #         if store.notification_permission:
            #             f.write('pm_notify\n')
            #         else:
            #             f.write('pm_notify_disable\n')
            #     if pm_files in self.permissions:
            #         if store.filesystem_permission:
            #             f.write('pm_files\n')
            #         else:
            #             f.write('pm_files_disable\n')
            #     if pm_sysadmin in self.permissions:
            #         if store.administrator_permission:
            #             f.write('pm_sysadmin\n')
            #         else:
            #             f.write('pm_sysadim_disable\n')
                        
            notification_permission = "no"
            filesystem_permission = "no"
            administrator_permission = "no"

        # Send Temporary Notification
        # For basic control, developers can use this function to send banner
        # notifications to the player without needing to define the screen
        # itself. 
        def send_temporary_notification(self, sender, contents, action):
            checknotify = self.short_name + "_notify"
            if persistent.aliceos_permissions[checknotify] == True:
                renpy.play("Resources/systemsounds/message.oga")
                renpy.call_screen("banner", applet=self, title=sender, message=contents, response=action)
            else:
                renpy.call_screen("alert", title="Notifications Are Disabled", message="Notifications are disabled for this Applet. Please check your permissions.", ok_action=Return(1))

        def __init__(self):
            key = self.short_name + "_notify"
            if key not in persistent.aliceos_permissions:
                persistent.aliceos_permissions[key] = False

            key = self.short_name + "_files"
            if key not in persistent.aliceos_permissions:
                persistent.aliceos_permissions[key] = False

            key = self.short_name + "_sysadmin"
            if key not in persistent.aliceos_permissions:
                persistent.aliceos_permissions[key] = False

            pass
# Mandatory Applet Temporary Variables
# This is needed to set the permissions accordingly
# These will reset to the defaul values after
# running the ask_all_permissions() function.           
define notification_permission = "no"
define filesystem_permission = "no"
define administrator_permission = "no"
