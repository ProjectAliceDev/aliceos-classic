label notify:
    scene bg club_day
    with dissolve_scene_half
    # play music t2
    # call screen alert("Test", "Test", ok_action=Return())
    "Well, it's another day at the Literature Club."
    $ renpyApp.ask_app_permissions()
    # call screen ask_permission("Messages", allow_fs, no_action=Quit(), yes_action=Return())
    "Null text"
    return