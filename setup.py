"""
A flask configuration handler that checks for enviroment variables or a '.env' file located
at ~/<.appname>/.env.
"""

from setuptools import setup

setup(
    name="Flask-EnvConfig",
    version='0.1.11',
    url='https://github.com/caustin/flask-envconfig',
    download_url='https://github.com/caustin/flask-envconfig/archive/0.1.10.tar.gz',
    license='MIT',
    author='Chris Austin',
    description='Configure a flask app with environment variables or a file.',
    long_description=__doc__,
    py_module=['flask_envconfig'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['Flask', ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)


