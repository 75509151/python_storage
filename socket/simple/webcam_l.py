import urllib2
import sys
import base64


class ipCamera(object):

    def __init__(self, url, user=None, password=None):
        self.url = url
        auth_encoded = base64.encodestring('%s:%s' % (user, password))[:-1]

        self.req = urllib2.Request(self.url)
        self.req.add_header('Authorization', 'Basic %s' % auth_encoded)
        self.req.add_header("User-Agent", "Mozilla/5.0")

    def get_frame(self):
        response = urllib2.urlopen(self.req)
        frame = response.read()
        # img_array = np.asarray(bytearray(response.read()), dtype=np.uint8)
        # frame = cv2.imdecode(img_array, 1)
        return frame


if __name__ == '__main__':
    # cam = ipCamera("http://192.168.2.211/cgi-bin/mjpeg?resolution=640x360&quality=1&page=1487663244526&Language=12", user="1", password="a12345678")
    cam = ipCamera("http://192.168.2.211:5000", user="1", password="a12345678")
    print cam.get_frame()
