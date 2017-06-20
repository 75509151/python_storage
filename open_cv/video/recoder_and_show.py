# coding:utf-8
import wx
import numpy as np
import cv2
import cv
import time

import threading

G_VIDEO_WIDTH = 300
G_VIDEO_HEIGHT = 300


class Recorder(threading.Thread):
    """docstring for Camera"""

    def __init__(self, cap):
        super(Recorder, self).__init__()
        self.cap = cap
        self.out = None
        self.frame = None
        self.diff = False
        self._stop = threading.Event()

    def join(self):
        if self.cap:
            self.cap.release()
        if self.out:
            self.out.release()
        super(Recorder, self).join()

    def read(self):
        if self.diff:
            self.diff = False
            return True, self.frame
        else:
            return None, None

    def stop(self):
        self._stop.set()

    def record(self):
        path = "/home/mm/jay_test"
        fourcc = cv2.cv.CV_FOURCC(*'DIVX')
        self.out = cv2.VideoWriter(path + ".avi", fourcc, 20.0, (G_VIDEO_HEIGHT, G_VIDEO_HEIGHT))
        self._stop.clear()

    def run(self):
        while True:
            while self.cap.isOpened() and not self._stop.is_set():
                ret, frame = self.cap.read()
                if ret == True:
                    self.frame = frame[100: 100 + G_VIDEO_WIDTH, 100: 100 + G_VIDEO_HEIGHT]
                    # frame = cv2.flip(frame, 0)

                    self.diff = True
                    # write the flipped frame
                    if self.out:
                        self.out.write(self.frame)

            time.sleep(1)


class VideoPanel(wx.Panel):

    def __init__(self, parent, recorder, fps=15):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        self._stop = threading.Event()
        self._stop.set()
        self.recorder = recorder

        self.video_with = 800
        self.video_height = 600
        print "hhe", self.video_with, self.video_height

        self.bmp = wx.Bitmap(self.video_with, self.video_height)

        self.timer = wx.Timer(self)
        self.timer.Start(1000. / fps)

        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_TIMER, self.NextFrame)

    def OnPaint(self, evt):
        if self.bmp:
            dc = wx.BufferedPaintDC(self)
            dc.DrawBitmap(self.bmp, 0, 0)

    def stop(self):
        self._stop.set()
        self.recorder.stop()

    def play(self):
        self._stop.clear()
        self.recorder.record()

    def NextFrame(self, event):
        if self._stop.is_set():
            return
        ret, frame = self.recorder.read()
        if ret:

            frame = cv2.resize(frame, (self.video_with, self.video_height))
            self.bmp.CopyFromBuffer(frame)
            self.Refresh()


class PlayerFrame(wx.Frame):
    """docstring for  PlayerFrame"""

    def __init__(self, parent, capture, size):
        super(PlayerFrame, self).__init__(
            parent, -1, style=0, size=size)
        self.show_panel = VideoPanel(self, capture)

    def OnPlay(self):
        self.show_panel.play()

    def OnStop(self):
        self.show_panel.stop()


if __name__ == '__main__':
    cap = cv2.VideoCapture(1)

    recorder = Recorder(cap)
    recorder.start()
    app = wx.App()
    frame = PlayerFrame(None, recorder, size=(640, 480))

    frame.Show()
    frame.OnPlay()
    app.MainLoop()
