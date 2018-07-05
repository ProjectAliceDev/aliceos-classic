label messages_demo:
    scene bg club_day
    with dissolve_scene_half
    play music t2
    "Well, it looks like another day at the Literature Club."
    show monika 5a at t11
    m "Hiya, [player]!"
    mc "Hi, Monika. I wonder why you're excited today."
    m "Ahaha!"
    m 1b "I got a new phone yesterday!"
    m 1k "It works with AliceOS Messages, the messaging system around here!"
    m 2b "I'd love to show you!"
    mc "Okay. Why not send a sample text?"
    m 4d "There's a slight issue, though..."
    m "You won't see any notifications for it."
    m "You need to give AliceOS Messages permission to do so."
    m "Let me see if I can trigger the command for it."
    call updateconsole("messages.ask_app_permissions()", "")
    call hideconsole
    $ messages.ask_app_permissions()
    mc "I think it worked..."
    m 4b "Let's see!"
    $ messages.send_temporary_notification("Monika", "You know I love you, right?", action=Return(1))
    mc "Yep, looks like it worked..."
    m 5a "Great!"
    m "That message was a real statement, by the way... ehehe~"
    return