Flask-MultiConfig
=================

A flask config parser that allows the user to supply a set of required and optional
configuration items.  These values can then be supplied by either the OS or shell's
environment variables or in a configuration file containing the values located at
~/.app_name/.env.

The format for the environment values in the .env file is:

    VARIABLE_NAME=VALUE

Where the VARIABLE_NAME

    * Must be in all caps.
    * Cannot be a python callable.


Setting Up Your Environment:
----------------------------

You can use multiconfig in two ways.

* Set your enviroment variables at the OS / Shell level.
* Create an '.env' file a hidden folder in your home folder.

Using an environment variable:

    $ export MY_CONFIG_VARIABLE='somethingVeryImportant'

Using a .env file:

    echo MY_CONFIG_VARIABLE='somethingVeryImportant' >> ~/.foo/.env


Example Usage:
--------------

    >>> from flask import Flask
    >>>from flask.ext.multiconfig import MultiEnvConfig
    >>> app = Flask('foo')
    >>> config = MultiEnvConfig(required=['MY_CONFIG_VARIABLE'], app=app)

Now all of the supplied config values is set up:

    >>> app.config.get("MY_CONFIG_VARIABLE")

Or using the factory / app_init() approach.

    >>> config = MultiEnvConfig(required=['MY_CONFIG_VARIABLE'])
    # Later in the app setup
    >>> config.init_app(app)



Install:
--------

    $ pip install Flask-MultiConfig