## Setup.rpy
# Post-install Setup Assistant (Pisa)
# Author: Marquis Kurt (@alicerunsonfedora)
# Copyright: (C) 2018

## Pisa class properties and methods
init python:

    class Pisa(object):

        general_step_titles = 
        {
            0: "Welcome to Setup",
            1: "Technical Preview Details",
            2: "AliceOS License Agreement",
            3: "Game License Agreement",
            4: "AliceOS Provider Details",
            5: "Username Creation",
            6: "Thank You"
        }

        general_step_descriptions =
        {
            0: "Welcome to the Setup assistant for AliceOS! This assistant will help you set up [config.name!t] and AliceOS for a smooth, interactive experience. When you are ready to start, press Next to continue the process.",
            1: "AliceOS is currently a technical preview; some features may not work properly. If you have any issues with AliceOS, we recommend filing an issue on GitHub by heading to our website: https://github.com/TheAngelReturns/aliceos/issues/create. Your AliceOS provider may have already included buttons or menus to get here as well.",
            2: "AliceOS is free and open-source software licensed under the GNU GPL v3. Please read the following license to understand your rights and agree to the terms listed.",
            3: "[config.name!t] may include an additional license or disclaimer besides what is provided with AliceOS. If there is a license agreement below, please read and agree to the terms listed. Otherwise, you can skip this step.",
            4: "AliceOS can be freely modified by the game's developers. If you run into an issue that isn't direclty related to the core AliceOS experience, please contact your AliceOS provider with the details provided below.",
            5: "Create a username for AliceOS and [config.name!t]. Your name will be displayed when you speak and when other characters address you in the game. AliceOS also uses this name to create a Home folder where game files created by characters will be dropped.",
            6: "The Setup assistant has finalized everything and you're now ready to play [config.name!t]! We hope you enjoy the game as well as the AliceOS experience. For more details on the AliceOS project, head to our website: https://aliceos.app."
        }
        

        def __init__(self):
            pass

## Pisa Screens