import cv2

cap = cv2.VideoCapture("rtsp://192.168.0.211/Src/MediaInput/h264/stream_1")
# vcap = cv2.CaptureFromFile("rtsp://192.168.0.211/Src/MediaInput/h264/stream_1")
if not cap.isOpened():
    print "Can't open stream/file"
else:
    while True:
        # read one frame (and "return" status)
        ret, frame = cap.read()

        # exit if error
        if not ret:
            break

        # (open window and) display one frame
        cv2.imshow('frame', frame)

        # exit if pressed any key
        # (it doesn't wait for key so you can read next frame)
        # (you have to one window to catch pressed key)
        if cv2.waitKey(1) != -1:
            break
