# Continuous Delivery Script for OSS DDLC Mods [![Build Status](https://travis-ci.org/Sayo-nika/quickstart-oss.svg?branch=master)](https://travis-ci.org/Sayo-nika/quickstart-travis)

This is a CI template to get you started on automated builds on [Travis CI](https://travis-ci.org)

Travis CI is a automated build tool to test and deploy your code. In the concept of DDLC Mods, this would
reduce your team's strain to have a dedicated builder for your team.

## Using

This is a Recipe intended to familiarize yourself on how to use Travis CI for Ren'Py applications. This way, you can code more
and worry less about releasing and packaging mods to upload it.

Take a look at `.travis.yml` to let you know on how to build mods with it!

We recommend using the `master` version of the Template or Version 1.1.0 to work until they release the no-script.rpa patch. Using released versions below 1.1.0 is known to be untested and breaks the recipe.

## Configuring

Of course, it could work outside the box, but you'll need to configure some things inside the `travis/` folder. This would be `travis/inject_version.sh`.

To get `inject_version.sh` replace your `config.version` in `options.rpy` correctly, do the following:
  - Set your desired template value for `config.version` in `options.rpy`.
  - Go to `travis/inject_version.sh`.
  - Replace the value of `replacer` with your template value that you set in `options.rpy`.


After that, you will also might need to write the `quickstart-oss/sample_mod` and `quickstart-oss/` paths into your own project paths. See how the folks in [The Angel Returns Mod](https://github.com/TheAngelReturns/the-angel-returns/blob/nightly/.travis.yml) configured this template to work.

## Copyright

The travis build script has been modified for use from Monika After Story repository. All rights reserved.

We used the amazing [Doki Doki : The Angel Returns](https://github.com/TheAngelReturns/the-angel-returns) mod as our sample mod. 

