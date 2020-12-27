import wx

class BaseWindow(wx.Frame):
    def __init__(self, title="BaseTitle", size=(640, 480)):
        super().__init__(None, wx.ID_ANY, title, size=size)
        self.base_panel = wx.Panel(self, wx.ID_ANY)
    
    def SetLayout(self, layout, row=1, col=1):
        self.layout = layout
        lo = wx.GridSizer(rows=row, cols=col, gap=(0, 0))
        self.SelectSizer(wx.GridSizer, [row, col, (0, 0)])
        self.SetItem()

    def SelectSizer(self, sizer, params):
        self.SIZER  = sizer
        self.PARAMS = params

    def SetItem(self):
        self.LO = self.SIZER(*self.PARAMS)
        self.LO.AddMany(self.layout)
        self.SetSizer(self.LO)
