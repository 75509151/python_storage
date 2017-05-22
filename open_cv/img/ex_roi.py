# coding: utf-8
import cv2
import numpy

path = "/home/mm/code_dept/python/resource/img/"

element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

ep_lg = cv2.imread(path + 'ex_empty_lg.jpg')
oc_lg = cv2.imread(path + 'ex_ocupity_lg.jpg')
oc_lg2 = cv2.imread(path + 'ex_ocupity_lg2.jpg')


kernel_size = 3
image = cv2.pyrMeanShiftFiltering(oc_lg, 10, 10)
# image = oc_lg
ep_lg_gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# ep_lg_erode = cv2.erode(ep_lg_gray_img, element)


# detected_edges = cv2.GaussianBlur(ep_lg_erode, (3, 3), 0)
detected_edges = cv2.Canny(ep_lg_gray_img, 20, 150, apertureSize=kernel_size)

cv2.imwrite(path + "ex_canny_edges.jpg", detected_edges)
# dst = cv2.bitwise_and(img, img, mask=detected_edges)  # just add some colours to edges from original image.
dst = cv2.bitwise_and(oc_lg, oc_lg, mask=detected_edges)  # just add some colours to edges from original image.
cv2.imwrite(path + "ex_canny_edges2.jpg", dst)

dst_gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(dst_gray, 25, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, 2, 1)


# for index, c in enumerate(contours):
#     if cv2.arcLength(c, True) > 600:

#         hull = cv2.convexHull(c, returnPoints=False)
#         defects = cv2.convexityDefects(c, hull)
#         for i in range(defects.shape[0]):
#             s, e, f, d = defects[i, 0]
#             start = tuple(c[s][0])
#             end = tuple(c[e][0])
#             far = tuple(c[f][0])
#             # cv2.line(dst, start, end, [0, 255, 0], 1)
#             # cv2.circle(dst, start, 5, [255, 0, 0], 2)
#             # cv2.circle(dst, far, 5, [255, 0, 0], 2)
#         cv2.drawContours(dst, contours, index, (0, 0, 255), 2)

# cv2.imwrite(path + "ex_canny_edges3.jpg", dst)

# ep_lg_gray_img = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)

# contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
