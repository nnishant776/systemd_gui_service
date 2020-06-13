'''
Created on Mar 10, 2020

@author: neeraj
'''

import wx.adv

from gui_systemd_service.gui.wizards.custom_wizards import SimpleWizard
from gui_systemd_service.servicecreator.gui.wizard.pages import ServiceConfigurationPage


class SystemdUnitConfigWizard(SimpleWizard):

    def __init__(self, parent, systemdData, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.service = systemdData
        self.Bind(wx.adv.EVT_WIZARD_PAGE_SHOWN, self.onPageChage)

    def onPageChage(self, evt):
        if evt.GetDirection() == True:
            page = evt.GetPage().GetPrev()
            # print(page);
            if isinstance(page, ServiceConfigurationPage):
                page.storeData()
                page.processData()
    
