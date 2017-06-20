import wx
import vlc
import numpy as np
import time
import os
import user
import cv2
import cv
import datetime


class MainWindow(wx.Panel):

    def __init__(self, parent, capture):
        wx.Panel.__init__(self, parent)
        mainSizer = wx.BoxSizer(wx.VERTICAL)

# video
        videoWarper = wx.StaticBox(self, size=(640, 480))
        videoBoxSizer = wx.StaticBoxSizer(videoWarper, wx.VERTICAL)
        videoFrame = wx.Panel(self, -1, size=(640, 480))
        videoBoxSizer.Add(videoFrame, 0)
        ShowCapture(videoFrame, capture)
        self.p = capture
        mainSizer.Add(videoBoxSizer, 0)

        parent.Centre()
        self.Show()
        self.SetSizerAndFit(mainSizer)

# Panels
# The first panel holds the video and it's all black
        self.videopanel = wx.Panel(self, -1)
        self.videopanel.SetBackgroundColour(wx.BLACK)

# The second panel holds controls
        ctrlpanel = wx.Panel(self, -1)
        self.timeslider = wx.Slider(ctrlpanel, -1, 0, 0, 1000)
        self.timeslider.SetRange(0, 1000)
        record = wx.Button(ctrlpanel, label="Record")

# Bind controls to events
        self.Bind(wx.EVT_BUTTON, self.OnRecord, record)

# Give a pretty layout to the controls
        ctrlbox = wx.BoxSizer(wx.VERTICAL)
        box = wx.BoxSizer(wx.HORIZONTAL)

# box contains some buttons
        box.Add(record)

# Merge box to the ctrlsizer
        ctrlbox.Add(box, flag=wx.EXPAND, border=10)
        ctrlpanel.SetSizer(ctrlbox)

# Put everything togheter
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(ctrlpanel, flag=wx.EXPAND | wx.BOTTOM | wx.TOP, border=10)
        self.SetSizer(sizer)
        self.SetMinSize((350, 300))

# VLC player controls
        self.Instance = vlc.Instance()
        self.player = self.Instance.media_player_new()

# -------begin capturing and saving video
    def OnRecord(self, evt):
        fps = 8
        size = (640, 480)

        writer = cv2.VideoWriter('video.avi', cv2.cv.CV_FOURCC('D', 'I', 'V', 'X'), fps, size)
        i = 0
        frame2 = cv.CreateImage(size, 8, 3)
        while i < 1000:
            ret, frame = self.p.read()
            if ret:

                frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                writer.write(frame2)

            # cv.WaitKey(1000/fps)


class ShowCapture(wx.Panel):

    def __init__(self, parent, capture, fps=9):
        wx.Panel.__init__(self, parent, wx.ID_ANY, (0, 0), (640, 480))

        self.capture = capture
        ret, frame = self.capture.read()

        height, width = frame.shape[:2]

        parent.SetSize((width, height))

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        self.bmp = wx.BitmapFromBuffer(width, height, frame)

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
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.bmp.CopyFromBuffer(frame)
            self.Refresh()


capture = cv2.VideoCapture(0)

app = wx.App(False)
frame = wx.Frame(None, title='CamGUI')
panel = MainWindow(frame, capture)
frame.Show()
app.MainLoop()
