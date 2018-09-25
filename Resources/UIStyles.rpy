# Stylesheet
init 2:
    style confirm_frame is gui_frame
    style confirm_setup_frame is gui_frame
    style confirm_prompt is gui_prompt
    style confirm_prompt_text is gui_prompt_text
    style confirm_prompt_details is gui_prompt
    style confirm_prompt_details_text is gui_prompt_text
    style confirm_prompt_details_mute is gui_prompt
    style confirm_prompt_details_mute_text is gui_prompt_text
    style confirm_button is gui_medium_button
    style confirm_button_negative is gui_medium_button
    style confirm_button_text is gui_medium_button_text
    style confirm_button_negative_text is gui_medium_button_text
    
    style aliceos_input is gui_prompt_input
    style aliceos_input_text is gui_prompt_input_text

    style setup_title is gui_prompt
    style setup_details is gui_prompt_text
    style setup_mute is gui_prompt
    style setup_title_text is gui_prompt_text
    style setup_details_text is gui_prompt_text
    style setup_mute_text is gui_prompt_text

    # Fonts
    if aliceos.oem_mode and aliceos.oem_use_custom_font:
        style aliceos_regular is default:
            font "Resources/systemfont/OEM/Regular.ttf"
            outlines []

        style aliceos_bold is default:
            font "Resources/systemfont/OEM/Bold.ttf"
            outlines []

        style aliceos_medium is default:
            font "Resources/systemfont/OEM/Medium.ttf"
            outlines []

        style aliceos_black is default:
            font "Resources/systemfont/OEM/Black.ttf"
            outlines []

        style aliceos_italic is default:
            font "Resources/systemfont/OEM/Italic.ttf"
            outlines []

        style aliceos_thin is default:
            font "Resources/systemfont/OEM/Thin.ttf"
            outlines []

    else:
        style aliceos_regular is default:
            font "Resources/systemfont/Regular.ttf"
            outlines []

        style aliceos_bold is default:
            font "Resources/systemfont/Bold.ttf"
            outlines []

        style aliceos_medium is default:
            font "Resources/systemfont/Medium.ttf"
            outlines []

        style aliceos_black is default:
            font "Resources/systemfont/Black.ttf"
            outlines []

        style aliceos_italic is default:
            font "Resources/systemfont/Italic.ttf"
            outlines []

        style aliceos_thin is default:
            font "Resources/systemfont/Thin.ttf"
            outlines []


    style confirm_frame:
        background Frame([ "Resources/systemui/confirm_frame.png", "Resources/systemui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
        padding gui.confirm_frame_borders.padding
        xalign .5
        yalign .5

    style confirm_setup_frame:
        background Frame([ "Resources/pisa/setup_window.png", "Resources/pisa/setup_window.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
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

    if aliceos.oem_large_pisa_font:
        style setup_title_text is aliceos_bold:
            color "#000"
            outlines []
            text_align 0.0
            size 38
            layout "subtitle"

        style setup_details_text is aliceos_regular:
            color "#000"
            outlines []
            size 28
            xpadding 32
            ypadding 8
            layout "tex"

        style setup_mute_text is aliceos_regular:
            color slate[700]
            size 17.2
            outlines []
            xpadding 32
            ypadding 8
            layout "tex"

        style aliceos_input is aliceos_bold:
            size 48
            color blueberry[500]
    else:
        style setup_title_text is aliceos_bold:
            color "#000"
            outlines []
            text_align 0.0
            size 32
            layout "subtitle"

        style setup_details_text is aliceos_regular:
            color "#000"
            outlines []
            # text_align 0.5
            xpadding 32
            ypadding 8
            layout "tex"

        style setup_mute_text is aliceos_regular:
            color slate[700]
            size 16
            outlines []
            # text_align 0.5
            xpadding 32
            ypadding 8
            layout "tex"

        style aliceos_input is aliceos_bold:
            size 32
            color blueberry[500]

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
        background Frame(["Resources/systemui/banner_frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
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


    ## ASErrorHandler Styles
    style rsod_emoticon is aliceos_regular:
        size 128
        color strawberry[100]

    style rsod_title_text is aliceos_regular:
        size 48
        text_align 0.0
        color "#ffffff"

    style rsod_prompt_text is aliceos_thin:
        color strawberry[100]
        text_align 0.0
        size 24

    style rsod_error_text is aliceos_medium:
        size 24
        color "#ffffff"
