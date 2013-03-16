NAME = 'PyRailgun'
VERSION = '0.12'
DESCRIPTION = "Fast Craweler for Python"
LONG_DESCRIPTION = """\
this is a simple Craweler Framework

from railgun import RailGun

railgun = RailGun()
railgun.setTask(file("basic.yaml"));
railgun.fire();
nodes = railgun.getShells('default')
print nodes

see test for more infomation
"""
AUTHOR = "zhongwei bai"
AUTHOR_EMAIL = 'baizhongwei@163.com'
LICENSE = "MIT"
PLATFORMS = "Any"
URL = "https://github.com/princehaku/pyrailgun"
DOWNLOAD_URL = "https://pypi.python.org/packages/source/P/PyRailgun/%s-%s.tar.gz" % (NAME, VERSION)
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
    "Topic :: Software Development :: Libraries :: Python Modules",
]
REQUIRS = [
    'pyyaml',
    'beautifulsoup4',
    'requests'
    ]

from setuptools import setup, find_packages

if __name__ == '__main__':

    setup(
        name=NAME,
        version=VERSION,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        license=LICENSE,
        platforms=PLATFORMS,
        url=URL,
        download_url=DOWNLOAD_URL,
        classifiers=CLASSIFIERS,
        packages=['railgun'],
        include_package_data = True,
        package_data = {
            'railgun':['*.conf']
        },
        requires=REQUIRS
    )

