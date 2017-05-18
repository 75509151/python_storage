# coding=utf-8
import cv2
import numpy as np
path = "/home/mm/code_dept/python/resource/img/"

img = cv2.imread(path + "ex.jpg")
ex_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mask = cv2.adaptiveThreshold(ex_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# OpenCV定义的结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# 腐蚀图像
eroded = cv2.erode(img, kernel)
# 显示腐蚀后的图像
cv2.imwrite(path + "ex_erode.jpg", eroded)

# 膨胀图像
dilated = cv2.dilate(img, kernel)
# 显示膨胀后的图像
cv2.imwrite(path + "ex_dilate.jpg", dilated)


# 腐蚀图像
eroded = cv2.erode(ex_gray, kernel)
# 显示腐蚀后的图像
cv2.imwrite(path + "ex_erode_mask.jpg", eroded)

# 膨胀图像
dilated = cv2.dilate(ex_gray, kernel)
# 显示膨胀后的图像
cv2.imwrite(path + "ex_dilate_mask.jpg", dilated)
