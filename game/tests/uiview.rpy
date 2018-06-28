label window_test:
    scene bg club_day
    with dissolve_scene_half
    play music t2
    "I wanted to try something new today."
    window hide(None)
    $ messages.show_window()
    "Alright this isn't funny anymore"
    return