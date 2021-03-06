#!/usr/bin/env python3
import sys
from setuptools import setup

if sys.version_info < (2, 5):
    sys.exit("Python 3.5 or greater is required.")

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

VERSION = "2.1.0"

LICENSE = "apache"

setup(
    name="easymq",
    version=VERSION,
    description=(
        "easy to connect activemq"
    ),
    long_description=readme,
    long_description_content_type="text/markdown",
    author="unknown-admin",
    author_email="niushuaibing@foxmail.com",
    maintainer="eric",
    maintainer_email="niushuaibing@foxmail.com",
    license=LICENSE,
    packages=[
        "easymq"
    ],
    platforms=["all"],
    url="https://github.com/localhost-sys/easymq",
    install_requires=[
        "stomp.py",
        "docopt"
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3'
    ],
)
