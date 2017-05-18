# coding:utf-8
import wx
import cv
import cv2
import numpy as np
path = "/home/mm/code_dept/python/resource/img/"


class ShowCapture(wx.Panel):
    def __init__(self, parent, capture=None, fps=15):
        wx.Panel.__init__(self, parent)

        # self.capture = capture
        # ret, frame = self.capture.read()

        # frame = frame[0:300, 0:300]
        frame = cv2.imread(path + "ex.jpg")
        height, width = frame.shape[:2]
        # height, width = 300, 300
        parent.SetSize((width, height))
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        print gray
        cv2.imwrite(path + "ex_gray.jgp", gray)
        # gray = cv2.GaussianBlur(gray, (5, 5), 0)
        # ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

        contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame, contours, -1, (0, 0, 255), 3)
        # res = cv2.GaussianBlur(res, (5, 5), 0)
        self.bmp = wx.BitmapFromBuffer(width, height, frame)

        # self.timer = wx.Timer(self)
        # self.timer.Start(1000. / fps)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        # self.Bind(wx.EVT_TIMER, self.NextFrame)

    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self)
        dc.DrawBitmap(self.bmp, 0, 0)

    def NextFrame(self, event):
        pass
        # frame = frame[0:300, 0:300]
        # if ret:
        #     gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        #     gray = cv2.GaussianBlur(gray, (5, 5), 0)
        #     # ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
        #     binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        #     contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        #     cv2.drawContours(frame, contours, -1, (0, 0, 255), 3)
        #     self.bmp.CopyFromBuffer(frame)
        #     self.Refresh()


app = wx.App()
frame = wx.Frame(None)
cap = ShowCapture(frame)
frame.Show()
app.MainLoop()
