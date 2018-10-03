#!/bin/sh

# AliceOS Specific Shell Script

description_template="REPLACE"

  sed -i "s/build.package(build.directory_name + \"CoreFiles\",'zip',build.name,description='REPLACE')/build.package(build.directory_name + \"$DIST_TARGET\",'zip',build.name,description='$DIST_TARGET-compatible module')/g" mod/game/options.rpy;
  cat mod/game/options.rpy | grep build.package;
  