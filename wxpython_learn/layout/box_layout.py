#!/usr/bin/env python
# -*-  coding: utf-8 -*-
# author:JarvisChu
# blog:zhujiangtao.com

import wx


class ExampleFrame(wx.Frame):
    def __init__(self, parent=None, id=-1, title='MyFrame'):
        wx.Frame.__init__(self, parent=parent, id=id, title=title)
        self.Centre()
        panel = wx.Panel(self, -1)

        btn1 = wx.Button(panel, label='btn1')
        btn2 = wx.Button(panel, label='btn2')
        btn3 = wx.Button(panel, label='btn3')
        btn4 = wx.Button(panel, label='btn4')
        btn5 = wx.Button(panel, label='btn5')

        # BoxSizer布局
        vBoxSizer = wx.BoxSizer(wx.VERTICAL)
        vBoxSizer.Add(btn1, proportion=1, flag=wx.TOP | wx.BOTTOM | wx.EXPAND, border=5)
        vBoxSizer.Add(btn2, proportion=2, flag=wx.TOP | wx.BOTTOM | wx.EXPAND, border=10)
        vBoxSizer.Add(btn3, proportion=3, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=10)
        vBoxSizer.Add(btn4, proportion=2, flag=wx.ALL | wx.EXPAND, border=10)
        vBoxSizer.Add(btn5, proportion=1, flag=wx.TOP | wx.BOTTOM | wx.EXPAND, border=5)
        # vBoxSizer.AddMany([(btn3,proportion=2,flag=wx.LEFT|wx.RIGHT|wx.EXPAND,border=10),(btn4)])
        panel.SetSizer(vBoxSizer)


class ExampleApp(wx.App):
    def OnInit(self):
        frame = ExampleFrame()
        frame.Show()
        return True


if __name__ == "__main__":
    app = ExampleApp()
    app.MainLoop()
