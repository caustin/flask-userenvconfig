from itertools import chain
from os import environ
import os.path


class MissingConfigException(Exception):

    def __init__(self, missing, app_name, config_path):
        m = ','.join(missing)
        

        s = """Required enviroment variable(s) %s missing.
        Please set them using your operating system's or shell's syntax or
        create the environment file '%s' and store the variables there using the
        following syntax:

        ENV_VAR_NAME=ENV_VAR_VALUE
        """ % (m, config_path)

        super(MissingConfigException, self).__init__(s)


class MultiEnvConfig(object):
    """Multi environment configuration for flask
    """

    def __init__(self, required, optional=None, app=None):
        self.required = required

        if optional is not None:
            self.optional = optional
        else:
            self.optional = list()

        if app is not None:
            self.init_app(app)

    def environ_file(self, app_name):
        return os.path.abspath(
            os.path.join(os.path.expanduser("~"), ".%s" % app_name, '.env')
        )

    def parse_environ_file(self, app_name):

        f = self.environ_file(app_name)
        if os.path.isfile(f):
            with open(f, 'r') as ef:
                for line in ef:
                    k, v = line.rstrip('\n').split('=')
                    if not callable(v):
                        os.environ[k] = v

    def init_app(self, app):
        missing = []
        app_name = app.name
        # try:
        self.parse_environ_file(app_name)

        for envar in chain(self.required, self.optional):
            if envar in self.required and envar not in os.environ:
                missing.append(envar)
            else:
                app.config.setdefault(envar, os.environ.get(envar))

        # except Exception as ex:
        #     raise ex

        if missing:
            raise MissingConfigException(missing, app.name, self.environ_file(app_name))