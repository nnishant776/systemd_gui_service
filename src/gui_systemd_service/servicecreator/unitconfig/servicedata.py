'''
Created on Mar 10, 2020

@author: neeraj
'''
from gui_systemd_service.servicecreator.unitconfig.details.sections import \
InstallationDetails, \
MountDetails, \
AutomountDetails, \
PathDetails, \
ServiceDetails, \
SocketDetails, \
SwapDetails, \
TimerDetails, \
UnitDetails


class SystemdServiceData(object):
    '''
    classdocs
    '''

    def __init__(self, *args, **kwargs):
        '''
        Constructor
        '''
        self.unitData = UnitDetails()
        self.installationData = InstallationDetails()
        self.mountData = MountDetails()
        self.automountData = AutomountDetails()
        self.pathData = PathDetails()
        self.serviceData = ServiceDetails()
        self.socketData = SocketDetails()
        self.swapData = SwapDetails()
        self.timerData = TimerDetails()
    
    def __str__(self):
        string_repr = ""
        for item in vars(self).values():
            print_val = str(item)
            string_repr += print_val + '\n' if len(print_val) > 0 else ''
        return string_repr
    
    def WriteString(self):
        string_repr = ""
        for data_item in vars(self).values():
            string_repr += str(data_item)
        return string_repr
    
    def json(self):
        print(vars(self))

