import wx


class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_LEFT_DCLICK, self.on_left_double_click)

        self.show_yellow_box = False
        self.box_pos = None

    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        dc.DrawRectangle(50, 60, 90, 40)
        if self.show_yellow_box:
            x, y = self.box_pos
            dc.SetBrush(wx.Brush("yellow"))
            dc.DrawRectangle(x, y, 90, 40)

    def on_left_double_click(self, evt):
        x = evt.GetX()
        y = evt.GetY()
        self.box_pos = (x, y)
        self.show_yellow_box = True
        self.Refresh()  # important, to trigger EVT_PAINT on panel


class MyForm(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Test", style=wx.DEFAULT_FRAME_STYLE, size=wx.Size(400, 300))
        self.main_panel = MyPanel(self)


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
