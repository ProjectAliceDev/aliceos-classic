## Setup.rpy
# Post-install Setup Assistant (Pisa)
# Author: Marquis Kurt (@alicerunsonfedora)
# Copyright: (C) 2018

## Pisa class properties and methods
init python:

    class Pisa(object):

        gnulicense = """\
                                          GNU LESSER GENERAL PUBLIC LICENSE
                                            Version 3, 29 June 2007

                      Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
                      Everyone is permitted to copy and distribute verbatim copies
                      of this license document, but changing it is not allowed.


                        This version of the GNU Lesser General Public License incorporates
                      the terms and conditions of version 3 of the GNU General Public
                      License, supplemented by the additional permissions listed below.

                        0. Additional Definitions.

                        As used herein, "this License" refers to version 3 of the GNU Lesser
                      General Public License, and the "GNU GPL" refers to version 3 of the GNU
                      General Public License.

                        "The Library" refers to a covered work governed by this License,
                      other than an Application or a Combined Work as defined below.

                        An "Application" is any work that makes use of an interface provided
                      by the Library, but which is not otherwise based on the Library.
                      Defining a subclass of a class defined by the Library is deemed a mode
                      of using an interface provided by the Library.

                        A "Combined Work" is a work produced by combining or linking an
                      Application with the Library.  The particular version of the Library
                      with which the Combined Work was made is also called the "Linked
                      Version".

                        The "Minimal Corresponding Source" for a Combined Work means the
                      Corresponding Source for the Combined Work, excluding any source code
                      for portions of the Combined Work that, considered in isolation, are
                      based on the Application, and not on the Linked Version.

                        The "Corresponding Application Code" for a Combined Work means the
                      object code and/or source code for the Application, including any data
                      and utility programs needed for reproducing the Combined Work from the
                      Application, but excluding the System Libraries of the Combined Work.

                        1. Exception to Section 3 of the GNU GPL.

                        You may convey a covered work under sections 3 and 4 of this License
                      without being bound by section 3 of the GNU GPL.

                        2. Conveying Modified Versions.

                        If you modify a copy of the Library, and, in your modifications, a
                      facility refers to a function or data to be supplied by an Application
                      that uses the facility (other than as an argument passed when the
                      facility is invoked), then you may convey a copy of the modified
                      version:

                        a) under this License, provided that you make a good faith effort to
                        ensure that, in the event an Application does not supply the
                        function or data, the facility still operates, and performs
                        whatever part of its purpose remains meaningful, or

                        b) under the GNU GPL, with none of the additional permissions of
                        this License applicable to that copy.

                        3. Object Code Incorporating Material from Library Header Files.

                        The object code form of an Application may incorporate material from
                      a header file that is part of the Library.  You may convey such object
                      code under terms of your choice, provided that, if the incorporated
                      material is not limited to numerical parameters, data structure
                      layouts and accessors, or small macros, inline functions and templates
                      (ten or fewer lines in length), you do both of the following:

                        a) Give prominent notice with each copy of the object code that the
                        Library is used in it and that the Library and its use are
                        covered by this License.

                        b) Accompany the object code with a copy of the GNU GPL and this license
                        document.

                        4. Combined Works.

                        You may convey a Combined Work under terms of your choice that,
                      taken together, effectively do not restrict modification of the
                      portions of the Library contained in the Combined Work and reverse
                      engineering for debugging such modifications, if you also do each of
                      the following:

                        a) Give prominent notice with each copy of the Combined Work that
                        the Library is used in it and that the Library and its use are
                        covered by this License.

                        b) Accompany the Combined Work with a copy of the GNU GPL and this license
                        document.

                        c) For a Combined Work that displays copyright notices during
                        execution, include the copyright notice for the Library among
                        these notices, as well as a reference directing the user to the
                        copies of the GNU GPL and this license document.

                        d) Do one of the following:

                            0) Convey the Minimal Corresponding Source under the terms of this
                            License, and the Corresponding Application Code in a form
                            suitable for, and under terms that permit, the user to
                            recombine or relink the Application with a modified version of
                            the Linked Version to produce a modified Combined Work, in the
                            manner specified by section 6 of the GNU GPL for conveying
                            Corresponding Source.

                            1) Use a suitable shared library mechanism for linking with the
                            Library.  A suitable mechanism is one that (a) uses at run time
                            a copy of the Library already present on the user's computer
                            system, and (b) will operate properly with a modified version
                            of the Library that is interface-compatible with the Linked
                            Version.

                        e) Provide Installation Information, but only if you would otherwise
                        be required to provide such information under section 6 of the
                        GNU GPL, and only to the extent that such information is
                        necessary to install and execute a modified version of the
                        Combined Work produced by recombining or relinking the
                        Application with a modified version of the Linked Version. (If
                        you use option 4d0, the Installation Information must accompany
                        the Minimal Corresponding Source and Corresponding Application
                        Code. If you use option 4d1, you must provide the Installation
                        Information in the manner specified by section 6 of the GNU GPL
                        for conveying Corresponding Source.)

                        5. Combined Libraries.

                        You may place library facilities that are a work based on the
                      Library side by side in a single library together with other library
                      facilities that are not Applications and are not covered by this
                      License, and convey such a combined library under terms of your
                      choice, if you do both of the following:

                        a) Accompany the combined library with a copy of the same work based
                        on the Library, uncombined with any other library facilities,
                        conveyed under the terms of this License.

                        b) Give prominent notice with the combined library that part of it
                        is a work based on the Library, and explaining where to find the
                        accompanying uncombined form of the same work.

                        6. Revised Versions of the GNU Lesser General Public License.

                        The Free Software Foundation may publish revised and/or new versions
                      of the GNU Lesser General Public License from time to time. Such new
                      versions will be similar in spirit to the present version, but may
                      differ in detail to address new problems or concerns.

                        Each version is given a distinguishing version number. If the
                      Library as you received it specifies that a certain numbered version
                      of the GNU Lesser General Public License "or any later version"
                      applies to it, you have the option of following the terms and
                      conditions either of that published version or of any later version
                      published by the Free Software Foundation. If the Library as you
                      received it does not specify a version number of the GNU Lesser
                      General Public License, you may choose any version of the GNU Lesser
                      General Public License ever published by the Free Software Foundation.

                        If the Library as you received it specifies that a proxy can decide
                      whether future versions of the GNU Lesser General Public License shall
                      apply, that proxy's public statement of acceptance of any version is
                      permanent authorization for you to choose that version for the
                      Library.
        """

        general_step_titles = {
            0: "Welcome to Setup",
            1: "Technical Preview Details",
            2: "AliceOS License Agreement",
            3: "Game License Agreement",
            4: "AliceOS Provider Details",
            5: "Username Creation",
            6: "Thank You"
        }

        general_step_descriptions = {
            0: "Welcome to the Setup assistant for AliceOS! This assistant will help you set up [config.name!t] and AliceOS for a smooth, interactive experience. When you are ready to start, press Next to continue the process.",
            1: "AliceOS is currently a technical preview; some features may not work properly. If you have any issues with AliceOS, we recommend filing an issue on GitHub by heading to our website: {a=https://github.com/TheAngelReturns/aliceos/issues/create}https://github.com/TheAngelReturns/aliceos/issues/create{/a}. Your AliceOS provider may have already included buttons or menus to get here as well.",
            2: "AliceOS is free and open-source software licensed under the GNU LGPL v3. Please read the following license to understand your rights and agree to the terms listed.",
            3: "[config.name!t] may include an additional license or disclaimer besides what is provided with AliceOS. If there is a license agreement below, please read and agree to the terms listed. Otherwise, you can skip this step.",
            4: "AliceOS can be freely modified by the game's developers. If you run into an issue that isn't directly related to the core AliceOS experience, please contact your AliceOS provider with the details provided below.",
            5: "Create a username for AliceOS and [config.name!t]. Your name will be displayed when you speak and when other characters address you in the game. AliceOS also uses this name to create a Home folder where game files created by characters will be dropped. Press Enter or Return on your keyboard to proceed.",
            6: "The Setup assistant has finalized everything and you're now ready to play [config.name!t]! We hope you enjoy the game as well as the AliceOS experience. For more details on the AliceOS project, head to our website: {a=https://aliceos.app}https://aliceos.app{/a}."
        }
        

        def __init__(self):
            pass

    setup = Pisa()

## Pisa Screens
screen pisa_element(step, step_details, extra_info, require_input, has_back, advance_type, ok_action):
    modal False
    zorder 200
    style_prefix "confirm"
    add "Resources/pisa/background.png"

    frame:
        xalign 0.9
        yalign 1.0
        style "confirm_setup_frame"
        has vbox:
            spacing 16
            xsize 656
            ymaximum 600
            ysize 600
            
        vbox:
            spacing 16
            style_prefix "setup"
            label _(step):
                style "setup_title"

            label _(step_details):
                style "setup_details"

            if extra_info != None:
                viewport id "vp":
                    draggable True
                    scrollbars "vertical"
                    ymaximum 275
                    mousewheel True

                    text _(extra_info):
                        style "setup_mute_text"

            if require_input:
                input:
                    yalign 0.5
                    style_prefix "aliceos"
                    style "aliceos_input"

                # vbar value YScrollValue("vp")

        hbox:
            if has_back:
                textbutton _("Back") action Rollback()
            xalign 1.0
            yalign 1.0
            spacing 32
            python:
                if advance_type == 0:
                    action_name = "Next"
                elif advance_type ==1:
                    action_name = "Agree"
                elif advance_type == 2:
                    action_name = "Finish"
                elif advance_type == 3:
                    action_name = ""
                else:
                    action_name = "Next"
            textbutton _(action_name) action ok_action:
                style "confirm_button_negative"


## Setup Label
# This is called in the bootloader. Use the call screen command
# to add additonal steps in the process.
label setup:
  stop music fadeout 1.0
  scene black with Dissolve(2.5)
  pause 0.5
  $ quick_menu = False
  call screen pisa_element(setup.general_step_titles[0], setup.general_step_descriptions[0], extra_info=None, has_back=False, require_input=None, advance_type=0, ok_action=Return(0))
  call screen pisa_element(setup.general_step_titles[1], setup.general_step_descriptions[1], extra_info=None, has_back=True, require_input=None, advance_type=0, ok_action=Return(0))
  call screen pisa_element(setup.general_step_titles[2], setup.general_step_descriptions[2], extra_info=setup.gnulicense, has_back=True, require_input=None, advance_type=1, ok_action=Return(0))
  call screen pisa_element(setup.general_step_titles[3], setup.general_step_descriptions[3], extra_info=license, has_back=True, require_input=None, advance_type=1, ok_action=Return(0))
  call screen pisa_element(setup.general_step_titles[4], setup.general_step_descriptions[4], extra_info=oem_info, has_back=True, require_input=None, advance_type=0, ok_action=Return(0))
  call screen pisa_element(setup.general_step_titles[5], setup.general_step_descriptions[5], extra_info=None, has_back=True, require_input=True, advance_type=3, ok_action=Return(input))
  python:
    message = _return
    if not isinstance(message, basestring) or message == "" or message == "\n":
      renpy.call_screen("ThrowASError", error_type=SetASError.get_error(SetASError.headers["Setup"], SetASError.pisaerr["NullInput"]))
      renpy.utter_restart()
    else:
      persistent.playername = _return
  call screen pisa_element(setup.general_step_titles[6], setup.general_step_descriptions[6], extra_info=None, has_back=True, require_input=None, advance_type=2, ok_action=Return(0))
  return