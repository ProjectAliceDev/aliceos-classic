label notify:
    scene bg club_day
    with dissolve_scene_half
    play music t2
    # call screen alert("Test", "Test", ok_action=Return())
    "Well, it's another day at the Literature Club."
    python:
        # renpyApp.ask_app_permissions()
        # renpyApp.send_temporary_notification("Detention for you", "When will you learn?", action=Return(1))
        messages.ask_app_permissions()
        messages.send_temporary_notification("Alice Angel", "Just got my new iPhone.", action=Return(1))
    "Null text"
    return