# coding:utf-8
import numpy as np
import cv2
path = "/home/mm/code_dept/python/resource/img/"


img = cv2.imread(path + "counter.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 0, 255), 3)

cv2.imwrite(path + "outline.jpg", img)
