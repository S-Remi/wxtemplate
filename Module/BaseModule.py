import wx
import uuid

COMMON_VALUE_DICT = {}

class BaseModule(wx.Panel):      
    def __init__(self, parent):
        super().__init__(parent, wx.ID_ANY)
        self.basekey = str(uuid.uuid4()) + "_"
        self.layout = {}
        self.bind   = [[]]
        self.SelectSizer(wx.BoxSizer, [wx.VERTICAL])

    def SelectSizer(self, sizer, params):
        self.SIZER  = sizer
        self.PARAMS = params

    def SetItem(self):
        self.LO = self.SIZER(*self.PARAMS)
        self.LO.AddMany(list(self.layout.values()))
        self.SetSizer(self.LO)
        for i in self.bind:
            if i==[]:
                continue
            key = i.pop(0)
            self.layout[key][0].Bind(*i)
    
    def GetValue(self, key, c=True, default=None):
        key = ("COMMON_" if c else self.basekey) + key
        return COMMON_VALUE_DICT.get(key, default)

    def SetValue(self, key, value, c=True):
        key = ("COMMON_" if c else self.basekey) + key
        COMMON_VALUE_DICT[key] = value
    
    def PrintValue(self):
        for i in COMMON_VALUE_DICT.items():
            print(f"{i[0]} : {i[1]}")
