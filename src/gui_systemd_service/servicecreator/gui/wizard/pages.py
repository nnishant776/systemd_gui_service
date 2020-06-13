'''
Created on Mar 10, 2020

@author: neeraj
'''
import wx, re

from gui_systemd_service.gui.wizards.pages.custom_wizard_pages import SimpleWizardPage
from gui_systemd_service.servicecreator.unitconfig.details.enumerations import MountType, \
NotifyAccessType, \
RestartType, \
ServiceType, \
SocketBindType, \
SocketProtocolType, \
BoolType, \
SystemProtectionType, mEnum


class ServiceConfigurationPage(SimpleWizardPage):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.InitUI(parent.service)

    def InitUi(self, service_data):
        pass
    
    def storeData(self):
        pass
    
    def processData(self):
        pass

    def ProcessMultipleEntries(self, dataString, separators):
        data = re.sub('[' + separators + ']+', ' ', dataString)
        data = data.strip().split()
        for i in range(len(data)):
            data[i] = data[i].strip()
        data = " ".join(data)
        return data
    

class UnitConfiguration(ServiceConfigurationPage):
    '''
    This class represents a wizard page that is used to gather basic the systemd unit configuration data.
    '''
    
    def __init__(self, parent, *args, **kwargs):
        self.data = None
        self.inputs = dict()
        super().__init__(parent, *args, **kwargs)
                
    def storeData(self):
        for k in self.inputs:
            val = self.inputs[k].GetValue()
            vars(self.data)[k] = val if len(str(val)) > 0 else None

    def processData(self):
        for key in vars(self.data):
            if key not in ['Description', 'Documentation']:
                val = vars(self.data)[key]
                val = self.ProcessMultipleEntries(dataString=val, separators=", ;").split() if val is not None else None
                vars(self.data)[key] = val
        
    def InitUI(self, service_data):
        self.data = service_data.unitData
        for key in vars(service_data.unitData).keys():
            input_field = wx.TextCtrl(self, wx.ID_ANY)
            input_field.SetMinSize(wx.Size(300, -1))
            self.inputs[key] = input_field
            if key not in ['Description', 'Documentation']:
                input_field.SetToolTip("Separate multiple entries by space(' ') or a comma(',')")
            
        vbox = wx.BoxSizer(wx.VERTICAL)
        static_box_sizer = wx.StaticBoxSizer(wx.StaticBox(self, -1, '[Unit]', style=wx.ALIGN_LEFT), wx.VERTICAL)
        gridbox = wx.GridBagSizer(0, 0)
        row = 0;
        
        for k in self.inputs:
            gridbox.Add(wx.StaticText(self, wx.ID_ANY, k), pos=(row, 0), flag=wx.ALL | wx.EXPAND, border=5)
            gridbox.Add(self.inputs[k], pos=(row, 1), flag=wx.EXPAND | wx.ALL, border=5)
            row += 1
            
        gridbox.AddGrowableCol(0, proportion=100)
        gridbox.AddGrowableCol(1, proportion=100)
        static_box_sizer.Add(gridbox, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(static_box_sizer, flag=wx.EXPAND)
        self.SetSizer(vbox)
        self.Fit()

        
class ServiceConfiguration(ServiceConfigurationPage):
    '''
    This class represents a wizard page that is used to gather basic the systemd unit configuration data.
    '''
    
    def __init__(self, parent, *args, **kwargs):
        self.data = None
        self.inputs = dict()
        super().__init__(parent, *args, **kwargs)
        
    def processData(self):
        for key in self.inputs:
            org_val = vars(self.data)[key]
            if org_val is not None:
                if key == 'Type':
                    vars(self.data)[key] = ServiceType[org_val]
                elif key == 'Restart':
                    vars(self.data)[key] = RestartType[org_val]
                elif key == 'ProtectSystem':
                    vars(self.data)[key] = SystemProtectionType[org_val]
                elif key in ['remainAfterExit', 'PrivateTmp', 'PrivateDevice']:
                    vars(self.data)[key] = BoolType[org_val]
                elif key == 'NotifyAccess':
                    vars(self.data)[key] = NotifyAccessType[org_val]
                else:
                    pass
    
    def fileChooserDialog(self, evt):
        pathname = wx.FileSelector("Open the program to run")
        self.inputs[evt.GetEventObject().GetName()][0].SetValue(pathname)
    
    def storeData(self):
        for key in self.inputs:
            val = self.inputs[key]
            if isinstance(val, wx.Choice):
                v = val.GetString(val.GetSelection())
            elif key.startswith('Exec'):
                v = val[0].GetValue()
                if len(str(v)) > 0:
                    pass
                else:
                    v = None
            else:
                v = val.GetValue()
            #print(key, v)
            vars(self.data)[key] = v if len(str(v).strip()) > 0 else None
        
    def InitUI(self, service_data):
        self.data = service_data.serviceData
        for key in vars(self.data).keys():
            input_field = None
            if key =='Type':
                input_field = wx.Choice(self, id=wx.ID_ANY, choices=[choice.name for choice in ServiceType])
                input_field.SetToolTip('Select service type')
            elif key ==  'Restart':
                input_field = wx.Choice(self, id=wx.ID_ANY, choices=[ch.name for ch in RestartType])
                input_field.SetToolTip('Select a restart mode')
            elif key == 'ProtectSystem':
                input_field = wx.Choice(self, id=wx.ID_ANY, choices=[ch.name for ch in SystemProtectionType])
            elif key in ['RemainAfterExit', 'PrivateTmp', 'PrivateDevice']:
                input_field = wx.Choice(self, id=wx.ID_ANY, choices=[ch.name for ch in BoolType])
            elif key in ['OOMScoreAdjust', 'LimitNOFile']:
                input_field = wx.SpinCtrl(self, id=wx.ID_ANY, initial=0)
                input_field.SetToolTip('Set values within acceptable and valid range as per systemd')
            elif key in ['RestartSecs', 'TimeoutSec']:
                input_field = wx.TextCtrl(self, id=wx.ID_ANY)
                input_field.SetToolTip('Set value as per systemd format. For more information see man systemd.time')
            elif key.startswith('Exec'):
                input_field = [wx.TextCtrl(self, wx.ID_ANY), wx.Button(self, id=wx.ID_ANY, label='+', name=key)]
                text_field = input_field[0]
                button = input_field[1]
                text_field.SetMinSize(wx.Size(250, -1))
                text_field.SetToolTip("Specify executable/command in the text field or choose an existing binary")
                button.SetSize(wx.Size(30, -1))
                button.SetToolTip("Select file")
                button.Bind(wx.EVT_BUTTON, self.fileChooserDialog)
            elif key == 'NotifyAccess':
                input_field = wx.Choice(self, id=wx.ID_ANY, choices=[ch.name for ch in NotifyAccessType])
                input_field.SetToolTip('Select an appropriate notification type')
            else:
                input_field = wx.TextCtrl(self, wx.ID_ANY)
                input_field.SetMinSize(wx.Size(300, -1))
            
            self.inputs[key] = input_field
            
        vbox = wx.BoxSizer(wx.VERTICAL)
        static_box_sizer = wx.StaticBoxSizer(wx.StaticBox(self, -1, '[Service]', style=wx.ALIGN_LEFT), wx.VERTICAL)
        gridbox = wx.GridBagSizer(0, 0)
        row = 0;
        
        for k in self.inputs:
            gridbox.Add(wx.StaticText(self, wx.ID_ANY, k), pos=(row, 0), flag=wx.ALL | wx.EXPAND, border=5)
            if k.startswith('Exec'):
                gridbox.Add(self.inputs[k][0], pos=(row, 1), flag=wx.EXPAND | wx.ALL, border=5)
                gridbox.Add(self.inputs[k][1], pos=(row, 2), flag=wx.ALL ^ wx.LEFT, border=5)
            else:
                gridbox.Add(self.inputs[k], pos=(row, 1), span=(1, 2), flag=wx.EXPAND | wx.ALL, border=5)
            row += 1
            
        gridbox.AddGrowableCol(0, proportion=100)
        gridbox.AddGrowableCol(1, proportion=100)
        static_box_sizer.Add(gridbox, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(static_box_sizer, flag=wx.EXPAND)
        self.SetSizer(vbox)
        self.Fit()

        
class InstallConfiguration(ServiceConfigurationPage):
    '''
    This class represents a wizard page that is used to gather basic the systemd unit configuration data.
    '''
    
    def __init__(self, parent, *args, **kwargs):
        self.data = None
        self.inputs = dict()
        super().__init__(parent, *args, **kwargs)
                
    def storeData(self):
        for k in self.inputs:
            val = self.inputs[k].GetValue()
            vars(self.data)[k] = val if len(str(val)) > 0 else None 
        
    def InitUI(self, service_data):
        self.data = service_data.installationData
        for key in vars(service_data.installationData).keys():
            input_field = wx.TextCtrl(self, wx.ID_ANY)
            input_field.SetMinSize(wx.Size(300, -1))
            self.inputs[key] = input_field
            
        vbox = wx.BoxSizer(wx.VERTICAL)
        static_box_sizer = wx.StaticBoxSizer(wx.StaticBox(self, -1, '[Install]', style=wx.ALIGN_LEFT), wx.VERTICAL)
        gridbox = wx.GridBagSizer(0, 0)
        row = 0;
        
        for k in self.inputs:
            gridbox.Add(wx.StaticText(self, wx.ID_ANY, k), pos=(row, 0), flag=wx.ALL | wx.EXPAND, border=5)
            gridbox.Add(self.inputs[k], pos=(row, 1), flag=wx.EXPAND | wx.ALL, border=5)
            row += 1
            
        gridbox.AddGrowableCol(0, proportion=100)
        gridbox.AddGrowableCol(1, proportion=100)
        static_box_sizer.Add(gridbox, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(static_box_sizer, flag=wx.EXPAND)
        self.SetSizer(vbox)
        self.Fit()
        

class MountConfiguration(ServiceConfigurationPage):
    '''
    This class represents a wizard page that is used to gather basic the systemd unit configuration data.
    '''
    
    def __init__(self, parent, *args, **kwargs):
        self.data = None
        self.inputs = dict()
        super().__init__(parent, *args, **kwargs)
                
    def storeData(self):
        for k in self.inputs:
            if k in ['SloppyOptions', 'LazyUnmount', 'ForceUnmount']:
                val = self.inputs[k].GetString(self.inputs[k].GetSelection())
            else:
                val = self.inputs[k].GetValue()
            vars(self.data)[k] = val if len(str(val)) > 0 else None
        
    def InitUI(self, service_data):
        self.data = service_data.mountData
        for key in vars(service_data.mountData).keys():
            input_field = None
            if key in ['SloppyOptions', 'LazyUnmount', 'ForceUnmount']:
                input_field = wx.Choice(self, id=wx.ID_ANY, choices=[ch.name for ch in BoolType])
                input_field.SetToolTip('Select appropriate value')
            else:
                input_field = wx.TextCtrl(self, wx.ID_ANY)
                input_field.SetMinSize(wx.Size(300, -1))
            self.inputs[key] = input_field
            
        vbox = wx.BoxSizer(wx.VERTICAL)
        static_box_sizer = wx.StaticBoxSizer(wx.StaticBox(self, -1, '[Mount]', style=wx.ALIGN_LEFT), wx.VERTICAL)
        gridbox = wx.GridBagSizer(0, 0)
        row = 0;
        
        for k in self.inputs:
            gridbox.Add(wx.StaticText(self, wx.ID_ANY, k), pos=(row, 0), flag=wx.ALL | wx.EXPAND, border=5)
            gridbox.Add(self.inputs[k], pos=(row, 1), flag=wx.EXPAND | wx.ALL, border=5)
            row += 1
            
        gridbox.AddGrowableCol(0, proportion=100)
        gridbox.AddGrowableCol(1, proportion=100)
        static_box_sizer.Add(gridbox, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(static_box_sizer, flag=wx.EXPAND)
        self.SetSizer(vbox)
        self.Fit()
        
        
class AutomountConfiguration(ServiceConfigurationPage):
    '''
    This class represents a wizard page that is used to gather basic the systemd unit configuration data.
    '''
    
    def __init__(self, parent, *args, **kwargs):
        self.data = None
        self.inputs = dict()
        super().__init__(parent, *args, **kwargs)
                
    def storeData(self):
        for k in self.inputs:
            val = self.inputs[k].GetValue()
            vars(self.data)[k] = val if len(str(val)) > 0 else None
        
    def InitUI(self, service_data):
        self.data = service_data.automountData
        for key in vars(service_data.automountData).keys():
            input_field = wx.TextCtrl(self, wx.ID_ANY)
            input_field.SetMinSize(wx.Size(300, -1))
            self.inputs[key] = input_field
            
        vbox = wx.BoxSizer(wx.VERTICAL)
        static_box_sizer = wx.StaticBoxSizer(wx.StaticBox(self, -1, '[Automount]', style=wx.ALIGN_LEFT), wx.VERTICAL)
        gridbox = wx.GridBagSizer(0, 0)
        row = 0;
        
        for k in self.inputs:
            gridbox.Add(wx.StaticText(self, wx.ID_ANY, k), pos=(row, 0), flag=wx.ALL | wx.EXPAND, border=5)
            gridbox.Add(self.inputs[k], pos=(row, 1), flag=wx.EXPAND | wx.ALL, border=5)
            row += 1
            
        gridbox.AddGrowableCol(0, proportion=100)
        gridbox.AddGrowableCol(1, proportion=100)
        static_box_sizer.Add(gridbox, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(static_box_sizer, flag=wx.EXPAND)
        self.SetSizer(vbox)
        self.Fit()

        
class TimerConfiguration(ServiceConfigurationPage):
    '''
    This class represents a wizard page that is used to gather basic the systemd unit configuration data.
    '''
    
    def __init__(self, parent, *args, **kwargs):
        self.data = None
        self.inputs = dict()
        super().__init__(parent, *args, **kwargs)
                
    def storeData(self):
        for k in self.inputs:
            if k in ['OnClockChange', 'OnTimezoneChange', 'Persistent', 'WakeSystem', 'RemainAfterElapse']:
                val = self.inputs[k].GetString(self.inputs[k].GetSelection())
            else:
                val = self.inputs[k].GetValue()
            vars(self.data)[k] = val if len(str(val)) > 0 else None
        pass
        
    def InitUI(self, service_data):
        self.data = service_data.timerData
        for key in vars(service_data.timerData).keys():
            input_field = None
            if key in ['OnClockChange', 'OnTimezoneChange', 'Persistent', 'WakeSystem', 'RemainAfterElapse']:
                input_field = wx.Choice(self, id=wx.ID_ANY, choices=[ch.name for ch in BoolType])
                input_field.SetToolTip('Select appropriate value')
            else:
                input_field = wx.TextCtrl(self, wx.ID_ANY)
                input_field.SetMinSize(wx.Size(300, -1))
                if key.endswith('Sec'):
                    input_field.SetToolTip('Specify time as per systemd format. See man systemd.time for more details')
            self.inputs[key] = input_field
            
        vbox = wx.BoxSizer(wx.VERTICAL)
        static_box_sizer = wx.StaticBoxSizer(wx.StaticBox(self, -1, '[Timer]', style=wx.ALIGN_LEFT), wx.VERTICAL)
        gridbox = wx.GridBagSizer(0, 0)
        row = 0;
        
        for k in self.inputs:
            gridbox.Add(wx.StaticText(self, wx.ID_ANY, k), pos=(row, 0), flag=wx.ALL | wx.EXPAND, border=5)
            gridbox.Add(self.inputs[k], pos=(row, 1), flag=wx.EXPAND | wx.ALL, border=5)
            
            gridbox.AddGrowableRow(row, proportion=100)            
            row += 1
            
        gridbox.AddGrowableCol(0, proportion=100)
        gridbox.AddGrowableCol(1, proportion=100)
        static_box_sizer.Add(gridbox, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(static_box_sizer, flag=wx.EXPAND)
        self.SetSizer(vbox)
        self.Fit()


class SocketConfiguration(ServiceConfigurationPage):
    '''
    This class represents a wizard page that is used to gather basic the systemd unit configuration data.
    '''
    
    def __init__(self, parent, *args, **kwargs):
        self.data = None
        self.inputs = dict()
        super().__init__(parent, *args, **kwargs)
                
    def storeData(self):
        for k in self.inputs:
            if k in ['Writable', 'Accept']:
                val = self.inputs[k].GetString(self.inputs[k].GetSelection())
            else:
                val = self.inputs[k].GetValue()
            vars(self.data)[k] = val if len(str(val)) else None
        pass
        
    def InitUI(self, service_data):
        self.data = service_data.socketData
        for key in vars(service_data.socketData).keys():
            if key in ['Accept', 'Writable']:
                input_field = wx.Choice(self, wx.ID_ANY, choices=[k.name for k in BoolType])
            else:
                input_field = wx.TextCtrl(self, wx.ID_ANY)
            input_field.SetMinSize(wx.Size(300, -1))
            self.inputs[key] = input_field
            
        vbox = wx.BoxSizer(wx.VERTICAL)
        static_box_sizer = wx.StaticBoxSizer(wx.StaticBox(self, -1, '[Socket]', style=wx.ALIGN_LEFT), wx.VERTICAL)
        gridbox = wx.GridBagSizer(0, 0)
        row = 0;
        
        for k in self.inputs:
            gridbox.Add(wx.StaticText(self, wx.ID_ANY, k), pos=(row, 0), flag=wx.ALL | wx.EXPAND, border=5)
            gridbox.Add(self.inputs[k], pos=(row, 1), flag=wx.EXPAND | wx.ALL, border=5)
            row += 1
            
        gridbox.AddGrowableCol(0, proportion=100)
        gridbox.AddGrowableCol(1, proportion=100)
        static_box_sizer.Add(gridbox, flag=wx.ALL | wx.EXPAND, border=5)
        vbox.Add(static_box_sizer, flag=wx.EXPAND)
        self.SetSizer(vbox)
        self.Fit()
