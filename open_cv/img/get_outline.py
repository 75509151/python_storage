# coding=utf-8
import cv2
import numpy
path = "/home/mm/code_dept/python/resource/img/"

image = cv2.imread(path + "ex.jpg")
ex_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 构造一个3×3的结构元素
element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
erode = cv2.erode(ex_gray, element)
dilate = cv2.dilate(erode, element)


# 将两幅图像相减获得边，第一个参数是膨胀后的图像，第二个参数是腐蚀后的图像
# result = cv2.absdiff(dilate, erode)


# 上面得到的结果是灰度图，将其二值化以便更清楚的观察结果
# retval, result = cv2.threshold(result, 40, 255, cv2.THRESH_BINARY)
result = cv2.adaptiveThreshold(dilate, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# 反色，即对二值图每个像素取反
# result = cv2.bitwise_not(result)


cv2.imwrite(path + "get_out.jpg", result)
