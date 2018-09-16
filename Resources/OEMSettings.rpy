##################################################
## AliceOS OEM Configurations
# This file can be used to set OEM settings such
# as colors, fonts, and custom branding. In code,
# replace the default strings with the OEM
# counterparts.
##################################################

## Define whether you want the OEM mode on or off.
## Turning the OEM mode on will use OEM fonts and
## settings instead of AliceOS's defaults.

define aliceos.oem_mode = False

## Define OEM properties such as the name, version,
## website, and support emails.

define aliceos.oem_name = ""
define aliceos.oem_website = ""
define aliceos.oem_support = ""

## Define the AliceOS OEM Fonts here. This covers
## required font weights to match the standard
## system.

define aliceos.oem_font_regular = ""
define aliceos.oem_font_bold = ""
define aliceos.oem_font_italic = ""
define aliceos.oem_font_black = ""
define alceos.oem_font_thin = ""
define aliceos.oem_font_medium = ""

## Define the AliceOS OEM Colors here. This covers
## branding colors scaling from the 100 (lightest)
## to 900 (darkest). If you can make use of AliceOS's
## default color palette (Elementary), you can simply
## ignore this.

init -10 python:
    aliceos_oem_colors = {
        100: "",
        300: "",
        500: "",
        700: "",
        900: ""
    }