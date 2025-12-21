# -*- coding: utf-8 -*-

"""
ncjishaku.meta
~~~~~~~~~~~~

Meta information about ncjishaku.

:copyright: (c) 2021 Devon (scarletcafe) R
:copyright: (c) 2025 CrystalAlpha358
:license: MIT, see LICENSE for more details.

"""

import typing

__all__ = (
    '__author__',
    '__copyright__',
    '__docformat__',
    '__license__',
    '__title__',
    '__version__',
    'version_info'
)


class VersionInfo(typing.NamedTuple):
    """Version info named tuple for Jishaku"""
    major: int
    minor: int
    micro: int
    releaselevel: str
    serial: int

    def __str__(self) -> str:
        version = '.'.join(map(str, (self.major, self.minor, self.micro)))
        match self.releaselevel.lower():
            case 'final' | '':
                return version
            case 'alpha':
                releaselevel = 'a'
            case 'beta':
                releaselevel = 'b'
            case 'c' | 'pre' | 'preview':
                releaselevel = 'rc'
            case 'dev':
                releaselevel = '.dev'
            case 'post' | 'rev' | 'r':
                releaselevel = '.post'
            case other:
                releaselevel = other
        return f'{version}{releaselevel}{self.serial}'


version_info = VersionInfo(major=3, minor=0, micro=0, releaselevel='beta', serial=1)

__author__ = 'CrystalAlpha358'
__copyright__ = 'Copyright (c) 2025 CrystalAlpha358'
__docformat__ = 'restructuredtext en'
__license__ = 'MIT'
__title__ = 'ncjishaku'
__version__ = str(version_info)
