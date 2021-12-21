# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="RDF Graphs Sharing/Exhange Server API Specifications",
    author_email="",
    url="",
    keywords=["Swagger", "RDF Graphs Sharing/Exhange Server API Specifications"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    This is a RDF Graph Exhange Server REST API specifications to provide users to access (CRUD - create, retrieve, update, and delete) RDF Graph-compliant RDF resources.  - Each user&#x27;s RDF graph (RDF Graph-compliant) can be shared with other users to enable Federated SPARQL query if the aggregated user roles and permissions over the RDF graphs passing the Access Control validation. Otherwise, the access will be denied. - The create operation can accept data source formats JSON-LD, RDF/XML, N3, or Turtle format for upload/create. - It is up to the implementation to support multiple data source formats. - The RDF Graph Exchange reference implementation will only support one of JSON-LD, N3, or Turtle formats.
    """
)
