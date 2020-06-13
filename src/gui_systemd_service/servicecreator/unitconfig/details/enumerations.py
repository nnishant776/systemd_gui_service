'''
Created on Mar 10, 2020

@author: neeraj
'''

import enum


class mEnum(enum.Enum):
    
    def __str__(self):
        return self.value


class BoolType(mEnum):
    TRUE = 'true'
    FALSE = 'false'


class ServiceType(mEnum):
    SIMPLE = 'simple'
    FORKING = 'forking'
    ONESHOT = 'oneshot'
    DBUS = 'dbus'
    NOTIFY = 'notify'
    IDLE = 'idle'


class NotifyAccessType(mEnum):
    NONE = 'none'
    MAIN = 'main'
    ALL = 'all'


class RestartType(mEnum):
    ALWAYS = 'always'
    ON_SUCCESS = 'on-success'
    ON_FAILURE = 'on-failure'
    ON_ABNORMAL = 'on-abnormal'
    ON_ABORT = 'on-abort'
    ON_WATCHDOG = 'on-watchdog'

    
class MountType(mEnum):
    AUTO = 'auto'
    EXT = 'ext'
    EXT2 = 'ext2'
    EXT3 = 'ext3'
    EXT4 = 'ext4'
    VFAT = 'vfat'
    EXFAT = 'exfat'

    
class SocketProtocolType(mEnum):
    UDPLITE = 'udplite'
    SCTP = 'sctp'

    
class SocketBindType(mEnum):
    DEFUALT = 'default'
    IPV6ONLY = 'ipv6-only'
    BOTH = 'both'

    
class SystemProtectionType(mEnum):
    TRUE = 'true'
    FALSE = 'false'
    FULL = 'full'
    STRICT = 'strict'


class BindIPV6Type(mEnum):
    DEFAULT = 'default'
    BOTH = 'both'
    IPV6_ONLY = 'ipv6-only'

    
del enum
