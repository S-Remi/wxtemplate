import wx
from Module import *

window_name = "wx Window"
default_window_size = (640, 480)

if __name__ == '__main__':
    application = wx.App()
    window = BaseWindow(title=window_name, size=default_window_size)
    layout = [
        [ExampleModule(window), 0, wx.GROW | wx.ALL, 0],
        # Widget, proportion, flag, border
    ]
    window.SetLayout(layout, row=1, col=1)
    window.Show()
    application.MainLoop()
