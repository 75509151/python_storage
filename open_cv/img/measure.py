import cv2
path = "/home/mm/code_dept/python/resource/img/"

img1 = cv2.imread(path + 'boy.jpg')

e1 = cv2.getTickCount()
for i in xrange(5, 49, 2):
    img1 = cv2.medianBlur(img1, i)
e2 = cv2.getTickCount()
t = (e2 - e1) / cv2.getTickFrequency()
print t
