'''
Created on Mar 10, 2020

@author: neeraj
'''

import wx
from wx.adv import WizardPage, WizardPageSimple


class SimpleWizardPage(WizardPageSimple):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

    def SetLayout(self, layout : wx.Sizer):
        self.SetSizer(layout, deleteOld=True)

    def CreateLink(self, page : WizardPageSimple):
        self.Chain(page)
        
    def InitUI(self):
        pass
    
    def ProcessData(self):
        pass


class ComplexWizardPage(WizardPage):

    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

    def SetLayout(self, layout : wx.Sizer):
        self.SetSizer(layout, deleteOld=True)

    def GetNext(self):
        return self.Next

    def GetPrev(self):
        return self.Prev

    def SetNext(self, page):
        self.Next = page

    def SetPrev(self, page):
        self.Prev = page

    def CreateLink(self, page):
        self.Next = page
        page.Prev = self


class TitledWizardPage(SimpleWizardPage):

    def __init__(self, parent, title : str):
        self.pageTitle = title
        super().__init__(parent)

    def SetLayout(self, layout : wx.Sizer):
        self.SetSizer(layout, deleteOld=True)

    def InitUI(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)
        title = wx.StaticText(self, -1, self.pageTitle)
        sizer.Add(title, 0, wx.ALIGN_CENTRE | wx.ALL, 5)
        sizer.Add(wx.StaticLine(self, -1), 0, wx.EXPAND | wx.ALL, 5)
        return sizer

