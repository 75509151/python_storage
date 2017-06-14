# coding:utf-8
import wx
import cv
import cv2
import numpy as np
import threading


class Camera(object):
    """docstring for Camera"""

    def __init__(self, port, width=480, height=320):
        super(Camera, self).__init__()
        self.port = port
        self.width = width
        self.height = height
        self.open()

    def open(self):
        try:
            self.dev = cv2.VideoCapture(self.port)
            self.dev.set(cv.CV_CAP_PROP_FRAME_WIDTH, self.width)
            self.dev.set(cv.CV_CAP_PROP_FRAME_HEIGHT, self.height)
        except Exception as e:
            self.dev = None
            raise e

    def read(self):
        if self.dev:
            return self.dev.read()
        else:
            self.open()
            if self.dev:
                return self.dev.read()
        return None, None


class VideoPanel(wx.Panel):

    def __init__(self, parent, capture, fps=15):
        wx.Panel.__init__(self, parent)

        self._stop = threading.Event()
        self.capture = capture
        ret, frame = self.capture.read()

        height, width = frame.shape[:2]
        parent.SetSize((width, height))
        # height, width = 300, 300
        print height, width
        self.bmp = wx.BitmapFromBuffer(width, height, frame)

        self.timer = wx.Timer(self)
        self.timer.Start(1000. / fps)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_TIMER, self.NextFrame)

        self.c = 0

    def OnPaint(self, evt):
        dc = wx.BufferedPaintDC(self)
        dc.DrawBitmap(self.bmp, 0, 0)

    def stop(self):
        self._stop.set()

    def play(self):
        self._stop.clear()

    def NextFrame(self, event):
        if self.c >= 200:
            self.stop()
            self.c += 1
        if self.c >= 400:
            self.c = 0
            self.play()
        if self._stop.is_set():
            return

        ret, frame = self.capture.read()
        # frame = frame[0:300, 0:300]
        if ret:
            self.c += 1
            self.bmp.CopyFromBuffer(frame)
            self.Refresh()


capture = Camera(0, 480, 320)

app = wx.App()
frame = wx.Frame(None)
cap = VideoPanel(frame, capture)
frame.Show()
app.MainLoop()
