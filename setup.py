import os
import re
from setuptools import setup

PATTERN = r'^{target}\s*=\s*([\'"])(.+)\1$'

PKG_NAME = "easy_logging"

HERE = os.path.abspath(os.path.dirname(__file__))

PACKAGE_NAME = re.compile(PATTERN.format(target='__package_name__'), re.M)
VERSION = re.compile(PATTERN.format(target='__version__'), re.M)
AUTHOR = re.compile(PATTERN.format(target='__author__'), re.M)
AUTHOR_EMAIL = re.compile(PATTERN.format(target='__author_email__'), re.M)
DESCRIPTION = re.compile(PATTERN.format(target='__description__'), re.M)
URL = re.compile(PATTERN.format(target='__url__'), re.M)

def readme():
    with open('README.MD') as f:
        return f.read()


def read():
    with open(os.path.join(HERE, PKG_NAME, 'easy_logging.py')) as f:
        file_data = f.read()
    return [regex.search(file_data).group(2) for regex in
            (PACKAGE_NAME, VERSION, VERSION, AUTHOR_EMAIL, DESCRIPTION, URL)]


package_name, version, author, author_email, description, url = read()

setup(
    name=package_name,
    version=version,
    description=description,
    long_description=readme(),
    long_description_content_type='text/markdown',
    author=author,
    author_email=author_email,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
    ],
    install_requires=['PySimpleGUI', 'loguru', 'toml'],
    license="MIT license",
    packages=[package_name],
    url=url,
    zip_safe=False
)