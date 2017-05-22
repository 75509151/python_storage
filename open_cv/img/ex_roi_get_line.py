# coding: utf-8

import wx
import cv
import cv2
import numpy as np
import cStringIO

path = "/home/mm/code_dept/python/resource/img/"


class OriginImgPanel(wx.Panel):
    def __init__(self, parent, img_path):
        self.background = wx.Image(img_path, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.Panel.__init__(self, parent=parent, size=(
            self.background.GetWidth(), self.background.GetHeight()))
        # self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

    def OnEraseBackground(self, evt):
        """
        Add a picture to the background
        """
        # yanked from ColourDB.py
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            # print rect
            dc.SetClippingRect(rect)
        dc.Clear()

        dc.DrawBitmap(self.background, 0, 0)


class EdgePanel(wx.Panel):
    def __init__(self, parent, img_path):
        wx.Panel.__init__(self, parent)
        self.origin_img = cv2.imread(img_path)
        height, width = self.origin_img.shape[:2]
        self.SetSize((height, width))
        self.rbg_img = cv2.cvtColor(self.origin_img, cv2.COLOR_BGR2RGB)
        self.bmp = wx.BitmapFromBuffer(width, height, self.rbg_img)

        self.edge_img = wx.StaticBitmap(self, size=(height, width))
        print "origin", width, height
        self.edge_img.SetBitmap(self.bmp)
        self.sp = 5
        self.sr = 5
        self.w = width
        self.h = height

    def adjust_sp(self, sp):
        self.sp = sp
        self.fliter_img()

    def adjust_sr(self, sr):
        self.sr = sr
        self.fliter_img()

    def fliter_img(self):
        image = cv2.pyrMeanShiftFiltering(self.origin_img, self.sp, self.sr)
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        kernel_size = 3
        detected_edges = cv2.Canny(gray_img, 20, 150, apertureSize=kernel_size)
        dst = cv2.bitwise_and(self.origin_img, self.origin_img, mask=detected_edges)
        self.rbg_img = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)
        self.bmp = wx.BitmapFromBuffer(self.w, self.h, self.rbg_img)
        self.edge_img.SetBitmap(self.bmp)


class CtrlPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, size=(400, 150))
        self.parent = parent
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.sp_sld = wx.Slider(self, value=5, minValue=1, maxValue=100,
                                size=(400, 50), style=wx.SL_HORIZONTAL | wx.SL_LABELS)

        vbox.Add(self.sp_sld, 1, flag=wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.TOP)
        self.sp_sld.Bind(wx.EVT_SLIDER, self.slider_sp)
        self.sr_sld = wx.Slider(self, value=5, minValue=1, maxValue=100,
                                size=(400, 50), style=wx.SL_HORIZONTAL | wx.SL_LABELS)

        vbox.Add(self.sr_sld, 1, flag=wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.TOP)

        self.sr_sld.Bind(wx.EVT_SLIDER, self.slider_sr)
        self.SetSizer(vbox)

    def slider_sp(self, e):
        obj = e.GetEventObject()
        val = obj.GetValue()
        print val
        self.parent.edge_pnl.adjust_sp(val)

    def slider_sr(self, e):
        obj = e.GetEventObject()
        val = obj.GetValue()
        print val
        self.parent.edge_pnl.adjust_sr(val)


class Mywin(wx.Frame):

    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title, size=(400, 300))
        self.InitUI()

    def InitUI(self):
        v_lay = wx.BoxSizer(wx.VERTICAL)
        img_path = path + 'ex_ocupity_lg.jpg'
        self.ctrl_pnl = CtrlPanel(self)
        self.img_pnl = OriginImgPanel(self, img_path)
        self.edge_pnl = EdgePanel(self, img_path)

        v_lay.Add(self.ctrl_pnl)
        v_lay.Add(self.img_pnl)
        v_lay.Add(self.edge_pnl)
        self.SetSizer(v_lay)
        self.SetSize((500, 800))
        self.Centre()
        self.Show(True)


app = wx.App()
frame = Mywin(None, "roi set")

app.MainLoop()
