"""
A flask configuration handler that checks for enviroment variables or a '.env' file located
at ~/<.appname>/.env.
"""

from setuptools import setup

setup(
    name="Flask-MultiConfig",
    version='1.0',
    url='',
    license='MIT',
    author='Chris Austin',
    description='Configure a flask app with environment variables or a file.',
    long_description=__doc__,
    py_module=['flask_multiconfig'],
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


