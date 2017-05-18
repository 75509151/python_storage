# coding:utf-8
import wx
import cv
import cv2
import numpy as np


class ShowCapture(wx.Panel):
    def __init__(self, parent, capture, fps=15):
        wx.Panel.__init__(self, parent)

        self.capture = capture
        ret, frame = self.capture.read()

        # frame = frame[0:300, 0:300]
        height, width = frame.shape[:2]
        # height, width = 300, 300
        parent.SetSize((width, height))
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # define range of blue color in HSV
        lower_blue = np.array([110, 50, 50])
        upper_blue = np.array([124, 255, 255])
        # HSV中黑色范围
        # lower_blue = np.array([0, 0, 0])
        # upper_blue = np.array([180, 255, 46])

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(frame, lower_blue, upper_blue)

        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame, frame, mask=mask)
        # res = cv2.GaussianBlur(res, (5, 5), 0)
        self.bmp = wx.BitmapFromBuffer(width, height, res)

        self.timer = wx.Timer(self)
        self.timer.Start(1000. / fps)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_TIMER, self.NextFrame)

    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self)
        dc.DrawBitmap(self.bmp, 0, 0)

    def NextFrame(self, event):
        ret, frame = self.capture.read()
        # frame = frame[0:300, 0:300]
        if ret:
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Convert BGR to HSV
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # # define range of blue color in HSV
            lower_blue = np.array([110, 50, 50])
            upper_blue = np.array([124, 255, 255])
            # HSV中黑色范围
            # lower_blue = np.array([0, 0, 0])
            # upper_blue = np.array([180, 255, 46])

            # 获得黑色区域的mask
            mask = cv2.inRange(frame, lower_blue, upper_blue)

            # Threshold the HSV image to get only blue colors
            # mask = cv2.inRange(frame, lower_blue, upper_blue)

            # Bitwise-AND mask and original image
            res = cv2.bitwise_and(frame, frame, mask=mask)
            # res = cv2.GaussianBlur(res, (5, 5), 0)
            # self.bmp.CopyFromBuffer(frame)
            self.bmp.CopyFromBuffer(res)
            self.Refresh()


capture = cv2.VideoCapture(0)
capture.set(cv.CV_CAP_PROP_FRAME_WIDTH, 1024)
capture.set(cv.CV_CAP_PROP_FRAME_HEIGHT, 780)

app = wx.App()
frame = wx.Frame(None)
cap = ShowCapture(frame, capture)
frame.Show()
app.MainLoop()
