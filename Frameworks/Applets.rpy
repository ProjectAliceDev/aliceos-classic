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
    pm_shell = "launcher"

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
            16: "16.png",
            24: "24.png",
            32: "32.png",
            64: "64.png",
            128: "128.png",
            256: "256.png"
        }

        # Security permissions
        # Possible entries: "notifications", "filesystem", "administrator", "launcher"
        permissions = {
            pm_notify, # Send notifications
            pm_files, # Access AliceOS filesystem
            pm_sysadmin, # Change AliceOS settings
            pm_shell # Manage launching of applets
        }

        # Launcher properties
        # These properties are used for desktop shells such as BingG. These
        # control how the applet is displayed in the desktop shell and what
        # happens when the button is clicked.
        launch = {
            "action": "Return(0)",
            "show_in_launchers": True
        }
        
        ## Simplified Functions
        ## These functions make use of AliceOS's frameworks so that developers
        ## don't have to code in their own set. These include asking the player
        ## all of the app's permissions, sending temporary notifications, etc.

        # Ask All Permissions
        # If a developer wants access information immediately rather than when
        # needed, this function should be called first.  
        def ask_app_permissions(self):
            store.notification_permission = False
            store.filesystem_permission = False
            store.administrator_permission = False
            store.launcher_permission = False
            
            if pm_notify in self.permissions:
                renpy.call_screen("ask_permission", app_name=self.long_name, action=allow_un, no_action=Return(1), yes_action=[SetVariable("notification_permission", True), Return(0)])

            if pm_files in self.permissions:
                renpy.call_screen("ask_permission", app_name=self.long_name, action=allow_fs, no_action=Return(1), yes_action=[SetVariable("filesystem_permission", True), Return(0)])

            if pm_sysadmin in self.permissions:
                renpy.call_screen("ask_permission", app_name=self.long_name, action=allow_sip, no_action=Return(1), yes_action=[SetVariable("administrator_permission", True), Return(0)])

            if pm_shell in self.permissions:
                renpy.call_screen("ask_permission", app_name=self.long_name, action=allow_sh, no_action=Return(1), yes_action=[SetVariable("launcher_permission", True), Return(0)])
            
            key = self.short_name + "_notify"
            value = store.notification_permission
            persistent.aliceos_permissions[key] = value

            key = self.short_name + "_files"
            value = store.filesystem_permission
            persistent.aliceos_permissions[key] = value

            key = self.short_name + "_sysadmin"
            value = store.administrator_permission
            persistent.aliceos_permissions[key] = value

            key = self.short_name + "_shell"
            value = store.launcher_permission
            persistent.aliceos_permissions[key] = value
                        
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

            key = self.short_name + "_shell"
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
define launcher_permission = "no"

## Screen Definitions
define allow_un = "Send Notifications"
define allow_fs = "Access The File System"
define allow_sip = "Modify System Settings"
define allow_sh = "Launch Applications"

define allow_un_details = "Notifications may include alerts, sounds, and banners. These can be configured in Control Center."
define allow_fs_details = "By giving this app access, this app can modify files beyond your Home folder. Only give file system access to apps that you trust."
define allow_sip_details = "By giving this app access, this app can modify system settings and control your computer. Only give this to apps that you trust."
define allow_sh_details = "By giving this app access, this app can launch applets on your computer. Only give this to apps that you trust."