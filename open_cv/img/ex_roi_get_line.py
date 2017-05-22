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

        self.edge_img.SetBitmap(self.bmp)
        # self.Bind(wx.EVT_PAINT, self.OnPaint)
        # self.Bind(wx.EVT_TIMER, self.NextFrame)

        # self.Refresh()

    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self)
        print "paint", self.bmp
        dc.DrawBitmap(self.bmp, 0, 0)

    def NextFrame(self, event):
        self.Refresh()

    def detect(self, sp, sr):
        image = cv2.pyrMeanShiftFiltering(self.origin_img, sp, sr)
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        detected_edges = cv2.Canny(gray_img, 20, 150, apertureSize=kernel_size)
        dst = cv2.bitwise_and(self.origin_img, self.origin_img, mask=detected_edges)


class CtrlPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.sld = wx.Slider(self, value=10, minValue=1, maxValue=100,
                             style=wx.SL_HORIZONTAL | wx.SL_LABELS)

        vbox.Add(self.sld, 1, flag=wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, border=20)
        self.sld.Bind(wx.EVT_SLIDER, self.OnSliderScroll)
        self.txt = wx.StaticText(self, label='Yiibai.com', style=wx.ALIGN_CENTER)
        vbox.Add(self.txt, 1, wx.ALIGN_CENTRE_HORIZONTAL)

        self.SetSizer(vbox)

    def OnSliderScroll(self, e):
        obj = e.GetEventObject()
        val = obj.GetValue()
        font = self.GetFont()
        font.SetPointSize(self.sld.GetValue())
        self.txt.SetFont(font)


class Mywin(wx.Frame):

    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title, size=(400, 300))
        self.InitUI()

    def InitUI(self):
        v_lay = wx.BoxSizer(wx.VERTICAL)
        img_path = path + 'ex_ocupity_lg.jpg'
        ctrl_pnl = CtrlPanel(self)
        img_pnl = OriginImgPanel(self, img_path)
        edge_pnl = EdgePanel(self, img_path)

        v_lay.Add(ctrl_pnl)
        v_lay.Add(img_pnl)
        v_lay.Add(edge_pnl)
        self.SetSizer(v_lay)
        self.SetSize((500, 800))
        self.Centre()
        self.Show(True)


app = wx.App()
frame = Mywin(None, "roi set")

app.MainLoop()
