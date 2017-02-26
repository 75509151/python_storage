import vlc
i = vlc.Instance('--verbose 2'.split())
p = i.media_player_new()
p.set_mrl('rtsp://192.168.0.211/Src/MediaInput/h264/stream_1')
p.play()
