#!/bin/sh

# AliceOS Specific Shell Script


# Based on the DDMC Community there's only one specific DDLC version DDLC uses. 
# And since we're building against latest and DDLC renpy versions, We're doing this.
# As a failsafe as well.

dist="$DIST_TARGET"
version=
case "$dist" in
    "ddlc") 
      version="6.99.12.4" 
    ;;
    "latest") 
      version="7.1.0" 
    ;;
    *)
      echo "! -- Error: specify Target!"
      exit 127
    ;;
esac

echo " --> Looks like you're building against $version."
echo " --> Don't forget AliceOS modules built against a specific RenPy version won't work on older or future versions!"
wget "https://renpy.org/dl/$version/renpy-$version-sdk.tar.bz2"
tar xf "renpy-$version-sdk.tar.bz2"
mv "renpy-$version-sdk" renpy
rm -rf "renpy-$version-sdk.tar.bz2"

exit 0;