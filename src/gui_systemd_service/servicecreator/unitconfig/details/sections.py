'''
Created on Mar 10, 2020

@author: neeraj
'''
from .enumerations import *

class UnitDetails:

    def __init__(self):
        self.Description : str = None
        self.Documentation : str = None
        self.Requires : list = None
        self.Wants : list = None
        self.BindsTo : list = None
        self.Before : list = None
        self.After : list = None
        self.Conflicts : list = None

    def __str__(self):
        non_empty_flag = False
        string_repr = "[Unit]\n"
        for item in vars(self):
            val = vars(self)[item]
            if val is not None:
                if not non_empty_flag:
                    non_empty_flag = True
                if isinstance(val, list):
                    string_repr += item + ' = ' + ' '.join(val) + '\n'
                else:
                    string_repr += item + ' = ' + str(val) + '\n'
        if non_empty_flag:
            return string_repr
        else:
            return ""


class ServiceDetails:

    def __init__(self):
        self.Type : ServiceType = None
        self.Sockets : list = None
        self.RemainAfterExit : BoolType = None
        self.PIDFile : str = None
        self.BusName : str = None
        self.NotifyAccess : NotifyAccessType = None
        self.OOMScoreAdjust : int = None
        self.LimitNOFile : int = None
        self.ProtectSystem : SystemProtectionType = None
        self.PrivateTmp : BoolType = None
        self.PrivateDevice : BoolType = None
        self.ExecStart : str = None
        self.ExecStartPre : str = None
        self.ExecStartPost : str = None
        self.ExecReload : str = None
        self.ExecStop : str = None
        self.ExecStopPost : str = None
        self.RestartSecs : str = None
        self.Restart : RestartType = None
        self.TimeoutSec : str = None

    def __str__(self):
        string_repr = '[Service]\n'
        non_empty_flag : BoolType = False
        for item in vars(self):
            val = vars(self)[item]
            if val is not None:
                if non_empty_flag is False:
                    non_empty_flag = True
                if isinstance(val, list):
                    string_repr += item + ' = ' + ' '.join(val) + '\n'
                else:
                    string_repr += item + ' = ' + str(val) + '\n'
        if non_empty_flag:
            return string_repr
        else:
            return ""


class InstallationDetails:

    def __init__(self):
        self.WantedBy : str = None
        self.RequiredBy : str = None
        self.Alias : str = None
        self.Also : str = None
        self.DefaultInstance : str = None

    def __str__(self):
        string_repr = "[Install]\n"
        non_empty_flag = False
        for item in vars(self):
            val = vars(self)[item]
            if val is not None:
                if not non_empty_flag:
                    non_empty_flag = True
                string_repr += item + ' = ' + val + '\n'

        if non_empty_flag:
            return string_repr
        else:
            return ""


class SocketDetails:

    def __init__(self):
        self.ListenStream : str = None
        self.ListenDatagram : str = None
        self.ListenSequentialPacket : str = None
        self.ListenFIFO : str = None
        self.ListenSpecial : str = None
        self.ListenNetlink : str = None
        self.ListenMessageQueue : str = None
        self.Accept : BoolType = None
        self.Backlog : int = None
        self.BindIPv6Only : BindIPV6Type = None
        self.BindToDevice = None
        self.SocketMode : int = None
        self.SocketProtocol : SocketProtocolType = None
        self.SocketUser : str = None
        self.SocketGroup : str = None
        self.Service : str = None
        self.Writable : BoolType = None
        self.MaxConnections : int = None
        self.TimeoutSec : str = None

    def __str__(self):
        non_empty_flag = False
        string_repr = "[Socket]\n"
        for item in vars(self):
            val = vars(self)[item]
            if val is not None:
                if not non_empty_flag:
                    non_empty_flag = True
                if isinstance(val, list):
                    string_repr += item + ' = ' + ' '.join(val) + '\n'
                else:
                    string_repr += item + ' = ' + str(val) + '\n'

        if non_empty_flag:
            return string_repr
        else:
            return ""


class MountDetails:

    def __init__(self):
        self.What : str = None
        self.Where : str = None
        self.Type : str = None
        self.Options : list = None
        self.SloppyOptions : BoolType = None
        self.LazyUnmount : BoolType = None
        self.ForceUnmount : BoolType = None
        self.DirectoryMode : int = None
        self.TimeoutSec : str = None

    def __str__(self):
        non_empty_flag = False
        string_repr = "[Mount]\n"
        for item in vars(self):
            val = vars(self)[item]
            if val is not None:
                if not non_empty_flag:
                    non_empty_flag = True    
                string_repr += item + ' = ' + str(val) + '\n'

        if non_empty_flag:
            return string_repr
        else:
            return ""


class AutomountDetails:

    def __init__(self):
        self.Where : str = None
        self.DirectoryMode : str = None

    def __str__(self):
        non_empty_flag = False
        string_repr = "[Automount]\n"
        for item in vars(self):
            val = vars(self)[item]
            if val is not None:
                if not non_empty_flag:
                    non_empty_flag = True
                string_repr += item + ' = ' + str(val) + '\n'

        if non_empty_flag:
            return string_repr
        else:
            return ""


class SwapDetails:

    def __init__(self):
        self.What : str = None
        self.Priority : str = None
        self.Options : str = None
        self.TimeoutSec : str = None

    def __str__(self):
        non_empty_flag = False
        string_repr = "[Swap]\n"
        for item in vars(self):
            val = vars(self)[item]
            if val is not None:
                if not non_empty_flag:
                    non_empty_flag = True
                string_repr += item + ' = ' + str(val) + '\n'

        if non_empty_flag:
            return string_repr
        else:
            return ""


class PathDetails:

    def __init__(self):
        self.PathExists = None
        self.PathExistsGlob = None
        self.PathModified = None
        self.DirectoryNotEmpty = None
        self.MakeDirectory = None
        self.DirectoryMode = None

    def __str__(self):
        non_empty_flag = False
        string_repr = "[Path]\n"
        for item in vars(self):
            val = vars(self)[item]
            if val is not None:
                if not non_empty_flag:
                    non_empty_flag = True
                string_repr += item + ' = ' + str(val) + '\n'

        if non_empty_flag:
            return string_repr
        else:
            return ""


class TimerDetails:

    def __init__(self):
        self.OnActiveSec : str = None
        self.OnBootSec : str = None
        self.OnStartupSec : str = None
        self.OnUnitActiveSec : str = None
        self.OnUnitInactiveSec : str = None
        self.OnCalendar : str = None
        self.OnClockChange : BoolType = None
        self.OnTimezoneChange : BoolType = None
        self.RandomizeDelaySec : str = None
        self.AccuracySec : str = None
        self.Unit : str = None
        self.Persistent : BoolType = None
        self.WakeSystem : BoolType = None
        self.RemainAfterElapse : BoolType = None

    def __str__(self):
        non_empty_flag = False
        string_repr = "[Timer]\n"
        for item in vars(self):
            val = vars(self)[item]
            if val is not None:
                if not non_empty_flag:
                    non_empty_flag = True
                string_repr += item + ' = ' + str(val) + '\n'

        if non_empty_flag:
            return string_repr
        else:
            return ""
