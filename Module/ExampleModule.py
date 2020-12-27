import wx
from .BaseModule import *

class ExampleModule(BaseModule):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = {
            "testA" : [wx.Button(self, wx.ID_ANY, 'A'), 0, wx.SHAPED | wx.ALL,  3],
            "testB" : [wx.Button(self, wx.ID_ANY, 'B'), 1, wx.GROW | wx.ALL,  3],
            "testC" : [wx.Button(self, wx.ID_ANY, 'C'), 2, wx.GROW | wx.ALL,  3],
        }
        # Key : [Widget, proportion, flag, border]

        self.bind = [
            ["testA", wx.EVT_BUTTON, self.ExampleEventA]
        ]
        # Key, Event, Function

        self.SelectSizer(wx.BoxSizer, [wx.VERTICAL])
        self.SetItem()

        self.SetValue("Click_num", 0)
    
    def ExampleEventA(self, event):
        v = self.GetValue("Click_num")
        print(v)
        self.SetValue("Click_num", v+1)
