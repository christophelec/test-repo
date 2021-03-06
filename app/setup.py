# coding: utf-8

import sys
from setuptools import setup, find_packages

with open('../job.properties', 'r') as props_file:
    props = {l.split('=')[0]: l.split('=')[1] for l in props_file}

NAME = props['project'][:-1]
VERSION = "1.1.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion==1.0.129"]

setup(
    name=NAME,
    version=VERSION,
    description="Swagger Petstore",
    author_email="apiteam@swagger.io",
    url="",
    keywords=["Swagger", "Swagger Petstore"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    long_description="""\
    This is a sample server Petstore server.  You can find out more about     Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).      For this sample, you can use the api key &#x60;special-key&#x60; to test the authorization     filters.
    """,
    entry_points={
        'console_scripts': [
            '{name}={name}.__main__:main'.format(name=NAME)
        ]
    },
)

