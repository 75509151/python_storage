# coding:utf-8
import wx
import cv
import cv2
import numpy as np


class ShowCapture(wx.Panel):
    def __init__(self, parent, capture, fps=15):
        wx.Panel.__init__(self, parent)

        self.capture = capture
        self.pre_frame = None  # 总是取前一帧做为背景（不用考虑环境影响）
        ret, frame = self.capture.read()

        height, width = frame.shape[:2]

        parent.SetSize((width, height))

        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        gray_img = cv2.GaussianBlur(gray_img, (21, 21), 0)
        element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        erode = cv2.erode(gray_img, element)
        if self.pre_frame is None:
            self.pre_frame = erode
        self.bmp = wx.BitmapFromBuffer(width, height, gray_img)

        self.timer = wx.Timer(self)
        self.timer.Start(1000. / fps)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_TIMER, self.NextFrame)

    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self)
        dc.DrawBitmap(self.bmp, 0, 0)

    def NextFrame(self, event):
        ret, frame = self.capture.read()

        if ret:

            gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            gray_img = cv2.GaussianBlur(gray_img, (21, 21), 0)
            element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
            erode = cv2.erode(gray_img, element)
            if self.pre_frame is None:
                self.pre_frame = erode
            else:
                diff_img = cv2.absdiff(self.pre_frame, erode)
                gray = cv2.cvtColor(diff_img, cv2.COLOR_BGR2GRAY)
                ret, binary = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)
                contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                for c in contours:
                    if cv2.contourArea(c) < 2000:  # 设置敏感度
                        continue
                    else:
                        # print(cv2.contourArea(c))
                        print("前一帧和当前帧不一样了, 有什么东西在动!")

                        break
                cv2.drawContours(diff_img, contours, -1, (0, 0, 255), 3)
                self.bmp.CopyFromBuffer(diff_img)
                self.Refresh()
                self.pre_frame = erode


capture = cv2.VideoCapture(0)
capture.set(cv.CV_CAP_PROP_FRAME_WIDTH, 1024)
capture.set(cv.CV_CAP_PROP_FRAME_HEIGHT, 780)

app = wx.App()
frame = wx.Frame(None)
cap = ShowCapture(frame, capture)
frame.Show()
app.MainLoop()
