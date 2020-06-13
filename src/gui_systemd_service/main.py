#!/usr/bin/python3

import subprocess
import sys
import argparse

import wx

from gui_systemd_service.gui.wizards.pages.custom_wizard_pages import TitledWizardPage 
from gui_systemd_service.servicecreator.gui.wizard.pages import AutomountConfiguration, \
InstallConfiguration, \
MountConfiguration, \
ServiceConfiguration, \
SocketConfiguration, \
TimerConfiguration, \
UnitConfiguration
from gui_systemd_service.servicecreator.gui.wizards import SystemdUnitConfigWizard
from gui_systemd_service.servicecreator.unitconfig.servicedata import SystemdServiceData


def check_for_wxPython():
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
    if "wxPython" not in installed_packages:
        raise ImportError("Package 'wxPython' not found. Please install 'wxPython'")

    
def main():

    check_for_wxPython()
    app = wx.App()
    service_data = SystemdServiceData()
    unit_config_wizard = SystemdUnitConfigWizard(None, service_data, id=wx.ID_ANY, title="Service Creation Wizard")
    title_page = TitledWizardPage(unit_config_wizard, "Welcome to the systemd unit file generator wizard")
    end_page = TitledWizardPage(unit_config_wizard, "Done!")
    unit_config_page = UnitConfiguration(unit_config_wizard)
    service_config_page = ServiceConfiguration(unit_config_wizard)
    install_config_page = InstallConfiguration(unit_config_wizard)
    socket_config_page = SocketConfiguration(unit_config_wizard)
    mount_config_page = MountConfiguration(unit_config_wizard)
    automount_config_page = AutomountConfiguration(unit_config_wizard)
    timer_config_page = TimerConfiguration(unit_config_wizard)
    unit_config_wizard.AddPages([
        title_page,
        unit_config_page,
        service_config_page,
        install_config_page,
        socket_config_page,
        mount_config_page,
        automount_config_page,
        timer_config_page,
        end_page
    ])
    unit_config_wizard.StartWizard()
    print(str(service_data))
    
    
if __name__ == '__main__':
    main()
