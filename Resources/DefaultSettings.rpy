##################################################
## AliceOS Default Configurations
# This file is used to set the default fonts and
# colors for AliceOS. Please do not modify this
# file if you are using the OEM settings. Please
# edit OEMSettings.rpy instead.
##################################################

## Define the AliceOS Fonts here. This covers
## required font weights to match the standard
## system.

define aliceos.font_regular = "Resources/systemfont/Regular.ttf"
define aliceos.font_bold = "Resources/systemfont/Bold.ttf"
define aliceos.font_italic = "Resources/systemfont/Italic.ttf"
define aliceos.font_black = "Resources/systemfont/Black.ttf"
define alceos.font_thin = "Resources/systemfont/Thin.ttf"
define aliceos.font_medium = "Resources/systemfont/Medium.ttf"

## Define the AliceOS Colors here.
init -10000 python:
    strawberry = {
        100: "#ff8c82",
        300: "#ed5353",
        500: "#c6262e",
        700: "#a10705",
        900: "#7a0000"
    }

    orange = {
        100: "#ffc27d",
        300: "#ffa154",
        500: "#f37329",
        700: "#cc3b02",
        900: "#a62100"
    }

    banana = {
        100: "#fff394",
        300: "#ffe16b",
        500: "#f9c440",
        700: "#d48e15",
        900: "#ad5f00"
    }

    lime = {
        100: "#d1ff82",
        300: "#9bdb4d",
        500: "#68b723",
        700: "#3a9104",
        900: "#206b00"
    }

    blueberry = {
        100: "#8cd5ff",
        300: "#64baff",
        500: "#3689e6",
        700: "#0d52bf",
        900: "#002e99"
    }

    grape = {
        100: "#e4c6fa",
        300: "#cd9ef7",
        500: "#a56de2",
        700: "#7239b3",
        900: "#452981"
    }

    cocoa = {
        100: "#a3907c",
        300: "#8a715e",
        500: "#715344",
        700: "#57392d",
        900: "#3d211b"
    }

    silver = {
        100: "#fafafa",
        300: "#d4d4d4",
        500: "#abacae",
        700: "#7e8087",
        900: "#555761"
    }

    slate = {
        100: "#95a3ab",
        300: "#667885",
        500: "#485a6c",
        700: "#273445",
        900: "#0e141f"
    }

    black = {
        100: "#666666",
        300: "#4d4d4d",
        500: "#333333",
        700: "#1a1a1a",
        900: "#000000"
    }

init -50000:
    ## Define whether you want the OEM mode on or off.
    ## Turning the OEM mode on will use OEM fonts and
    ## settings instead of AliceOS's defaults.

    default aliceos.oem_mode = False

    ## Define OEM properties such as the name, version,
    ## website, and support emails.

    default aliceos.oem_name = None
    default aliceos.oem_website = None
    default aliceos.oem_support = None

    ## Define the AliceOS OEM Fonts here. This covers
    ## required font weights to match the standard
    ## system.

    default aliceos.oem_font_regular = None
    default aliceos.oem_font_bold = None
    default aliceos.oem_font_italic = None
    default aliceos.oem_font_black = None
    default alceos.oem_font_thin = None
    default aliceos.oem_font_medium = None

    default aliceos.font_regular = "Resources/systemfont/Regular.ttf"
    default aliceos.font_bold = "Resources/systemfont/Bold.ttf"
    default aliceos.font_italic = "Resources/systemfont/Italic.ttf"
    default aliceos.font_black = "Resources/systemfont/Black.ttf"
    default alceos.font_thin = "Resources/systemfont/Thin.ttf"
    default aliceos.font_medium = "Resources/systemfont/Medium.ttf"
