# Stylesheet
init 2:
    style confirm_frame is gui_frame
    style confirm_setup_frame is gui_frame
    style confirm_prompt is gui_prompt
    style confirm_prompt_text is gui_prompt_text
    style confirm_prompt_details is gui_prompt
    style confirm_prompt_details_mute is gui_prompt
    style confirm_prompt_details_mute_text is gui_prompt_text
    style confirm_prompt_details_text is gui_prompt_text
    style confirm_button is gui_medium_button
    style confirm_button_negative is gui_medium_button
    style confirm_button_text is gui_medium_button_text
    style confirm_button_negative_text is gui_medium_button_text
    style aliceos_input is gui_prompt_input

    # Fonts
    if aliceos.oem_mode:
        style aliceos_regular is default:
            font aliceos.oem_font_regular
            outlines []

        style aliceos_bold is default:
            font aliceos.oem_font_bold
            outlines []

        style aliceos_medium is default:
            font aliceos.oem_font_medium
            outlines []

        style aliceos_black is default:
            font aliceos.oem_font_black
            outlines []

        style aliceos_italic is default:
            font aliceos.oem_font_italic
            outlines []

        style aliceos_thin is default:
            font aliceos.oem_font_regular
            outlines []

    else:
        style aliceos_regular is default:
            font aliceos.font_regular
            outlines []

        style aliceos_bold is default:
            font aliceos.font_bold
            outlines []

        style aliceos_medium is default:
            font aliceos.font_medium
            outlines []

        style aliceos_black is default:
            font aliceos.font_black
            outlines []

        style aliceos_italic is default:
            font aliceos.font_italic
            outlines []

        style aliceos_thin is default:
            font aliceos.font_regular
            outlines []


    style confirm_frame:
        background Frame([ "Resources/systemui/confirm_frame.png", "Resources/systemui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
        padding gui.confirm_frame_borders.padding
        xalign .5
        yalign .5

    style confirm_setup_frame:
        background Frame([ "Resources/pisa/setup_window_blank.png", "Resources/pisa/setup_window_blank.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
        padding gui.confirm_frame_borders.padding
        xalign .5
        yalign .5

    style extra_info_mode:
        background "#fff"

    style confirm_prompt_text is aliceos_bold:
        color "#000"
        outlines []
        text_align 0.0
        size 32
        layout "subtitle"

    style confirm_prompt_details_text is aliceos_regular:
        color "#000"
        outlines []
        # text_align 0.5
        xpadding 32
        ypadding 8
        layout "tex"

    style confirm_prompt_details_mute_text is aliceos_regular:
        color slate[700]
        size 16
        outlines []
        # text_align 0.5
        xpadding 32
        ypadding 8
        layout "tex"

    style confirm_button is aliceos_bold:
        properties gui.button_properties("confirm_button")
        color blueberry[500]
        hover_color blueberry[100]
        outlines []
        size 28

    style confirm_button_negative is aliceos_bold:
        properties gui.button_properties("confirm_button")
        color blueberry[500]
        hover_color blueberry[100]
        outlines []

    style confirm_button_text is aliceos_regular:
        properties gui.button_text_properties("confirm_button")
        color blueberry[500]
        hover_color blueberry[100]
        outlines []

    style confirm_button_negative_text is aliceos_bold:
        properties gui.button_text_properties("confirm_button")
        color blueberry[500]
        hover_color blueberry[100]
        outlines []

    style banner_frame:
        background Frame(["gui/banner_frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
        xalign .5
        yalign .5

    style banner_frame_app is aliceos_regular:
        color "333333"
        first_indent 8
        size 20
        outlines []
        text_align 0
        layout "tex"

    style banner_frame_sender is aliceos_bold:
        color "#000"
        size 22
        outlines []
        text_align 0
        layout "tex"

    style banner_frame_message is aliceos_regular:
        color "#000"
        size 22
        outlines []
        text_align 0
        layout "tex"

    style banner_dismiss is navigation_button_text:
        properties gui.button_text_properties("confirm_button")
        color "333"
        size 18
        hover_color "000"
        outlines []

    style banner_dismiss_text is navigation_button_text:
        properties gui.button_text_properties("confirm_button")
        color "000"
        size 18
        hover_color "333"
        outlines []

    style aliceos_input_text is aliceos_italic:
        color blueberry[500]

