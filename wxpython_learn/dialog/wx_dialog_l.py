#!/usr/bin/env python2
# -*- coding:utf-8 -*-

import wx

#---------------------------------------------------------------------------


class TestPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)

        b = wx.Button(self, -1, "Create and Show a TextEntryDialog", (50, 50))
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)

    def OnButton(self, EVT):
        dlgtext = wx.TextEntryDialog(
            self, 'What is your favorite programming language?',
            'Eh??', 'Python')

        dlgtext.SetValue("Python is the best!")

        if dlgtext.ShowModal() == wx.ID_OK:

            dlgmsg = wx.MessageDialog(self, dlgtext.GetValue(),
                                      'A Message Box',
                                      wx.OK | wx.ICON_INFORMATION
                                      #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                                      )
            dlgmsg.Center()
            dlgmsg.ShowModal()
            dlgmsg.Destroy()
        dlgtext.Destroy()
#---------------------------------------------------------------------------


app = wx.App()
frame = wx.Frame(None)
p = TestPanel(frame)
frame.Show()
app.MainLoop()
#---------------------------------------------------------------------------
