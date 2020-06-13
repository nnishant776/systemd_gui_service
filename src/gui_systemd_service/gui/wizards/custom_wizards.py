'''
Created on Mar 10, 2020

@author: neeraj
'''

import sys

from wx.adv import Wizard

from gui_systemd_service.gui.wizards.pages.custom_wizard_pages import SimpleWizardPage


class SimpleWizard(Wizard):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.pages : SimpleWizardPage = []
        
    def AddPage(self, page : SimpleWizardPage):
        if self.pages:
            prev = self.pages[-1]
            prev.Chain(page)
        self.pages.append(page)
        
    def AddPages(self, list_of_pages):
        prev_page : SimpleWizardPage = None
        if len(self.pages) != 0:
            prev_page = self.pages[-1]
        else:
            try:
                prev_page = list_of_pages.pop(0)
                self.pages.append(prev_page)
                # self.GetSizer().Add(prev_page)
                for page in list_of_pages:
                    prev_page.CreateLink(page)
                    prev_page = page
                    self.pages.append(page)
                    # self.GetSizer().Add(page)
            except ValueError:
                print("List of pages is empty. No page found!")
            except:
                print("Unexpected error :", sys.exc_info()[0])
                
    def StartWizard(self):
        self.FitToPage(self.pages[0])
        self.RunWizard(self.pages[0])
        self.Destroy()
        
