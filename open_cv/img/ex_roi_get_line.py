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
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.origin_img = cv2.imread(img_path)
        height, width = self.origin_img.shape[:2]
        self.SetSize((height * 3, width * 3))
        self.rbg_img = cv2.cvtColor(self.origin_img, cv2.COLOR_BGR2RGB)
        self.bmp = wx.BitmapFromBuffer(width, height, self.rbg_img)

        self.edge_img = wx.StaticBitmap(self, size=(width, height))

        self.edge_img.SetBitmap(self.bmp)

        hbox.Add(self.edge_img, 1)
        hbox.Add((-1, -1), 1)
        self.binary_img = wx.StaticBitmap(self, size=(width, height))

        self.binary_img.SetBitmap(self.bmp)
        hbox.Add(self.binary_img)
        self.sp = 5
        self.sr = 5
        self.threshold = 20
        self.w = width
        self.h = height
        self.cv_bmp = None
        self.SetSizer(hbox)

    def adjust_sp(self, sp):
        self.sp = sp
        self.fliter_img()

    def adjust_sr(self, sr):
        self.sr = sr
        self.fliter_img()

    def adjust_threshold(self, th):
        self.threshold = th
        self.threshold_img()

    def fliter_img(self):
        image = cv2.pyrMeanShiftFiltering(self.origin_img, self.sp, self.sr)
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        kernel_size = 3
        detected_edges = cv2.Canny(gray_img, 20, 150, apertureSize=kernel_size)
        self.cv_bmp = cv2.bitwise_and(self.origin_img, self.origin_img, mask=detected_edges)
        self.rbg_img = cv2.cvtColor(self.cv_bmp, cv2.COLOR_BGR2RGB)
        self.bmp = wx.BitmapFromBuffer(self.w, self.h, self.rbg_img)
        self.edge_img.SetBitmap(self.bmp)

    def threshold_img(self):
        if self.cv_bmp is not None:
            gray_img = cv2.cvtColor(self.cv_bmp, cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(gray_img, self.threshold, 255, cv2.THRESH_BINARY)
            # mask_inv = cv2.bitwise_not(mask)
            img = cv2.bitwise_and(self.cv_bmp, self.cv_bmp, mask=mask)
            bmp = wx.BitmapFromBuffer(self.w, self.h, img)
            self.binary_img.SetBitmap(bmp)


class CtrlPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, size=(420, 150))
        self.parent = parent
        # vbox = wx.BoxSizer(wx.VERTICAL)
        sizer = wx.GridBagSizer(hgap=10, vgap=0)

        self.sp_sld = wx.Slider(self, value=5, minValue=1, maxValue=40,
                                size=(200, 50), style=wx.SL_HORIZONTAL | wx.SL_LABELS)

        # vbox.Add(self.sp_sld)
        sizer.Add(self.sp_sld, (0, 0))
        self.sp_sld.Bind(wx.EVT_SLIDER, self.slider_sp)
        self.sr_sld = wx.Slider(self, value=5, minValue=1, maxValue=40,
                                size=(200, 50), style=wx.SL_HORIZONTAL | wx.SL_LABELS)

        # vbox.Add(self.sr_sld)
        sizer.Add(self.sr_sld, (0, 1))
        self.sr_sld.Bind(wx.EVT_SLIDER, self.slider_sr)

        self.thre_sld = wx.Slider(self, value=5, minValue=1, maxValue=40,
                                  size=(200, 50), style=wx.SL_HORIZONTAL | wx.SL_LABELS)

        sizer.Add(self.thre_sld, (1, 1))
        self.thre_sld.Bind(wx.EVT_SLIDER, self.slider_threshold)

        self.SetSizer(sizer)

    def slider_sp(self, e):
        obj = e.GetEventObject()
        val = obj.GetValue()
        print "sp", val
        self.parent.edge_pnl.adjust_sp(val)

    def slider_sr(self, e):
        obj = e.GetEventObject()
        val = obj.GetValue()
        print val
        self.parent.edge_pnl.adjust_sr(val)

    def slider_canny(self, e):
        obj = e.GetEventObject()
        val = obj.GetValue()
        print val

    def slider_threshold(self, e):
        obj = e.GetEventObject()
        val = obj.GetValue()
        print val
        self.parent.edge_pnl.adjust_threshold(val)


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
        self.SetSize((1000, 900))
        self.Centre()
        self.Show(True)


app = wx.App()
frame = Mywin(None, "roi set")

app.MainLoop()
