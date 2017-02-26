import vlc
import time
player = vlc.MediaPlayer('rtsp://192.168.0.211/Src/MediaInput/h264/stream_1')
player.play()
while 1:
    time.sleep(1)
    player.video_take_snapshot(0, '.snapshot.tmp.png', 0, 0)
