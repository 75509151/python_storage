# coding: utf-8
import cv2
import numpy

path = "/home/mm/code_dept/python/resource/img/"

element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

ep_lg = cv2.imread(path + 'ex_empty_lg.jpg')
oc_lg = cv2.imread(path + 'ex_ocupity_lg.jpg')
oc_lg2 = cv2.imread(path + 'ex_ocupity_lg2.jpg')

ep_lg_gray_img = cv2.cvtColor(ep_lg, cv2.COLOR_BGR2RGB)
ep_lg_gray_img = cv2.GaussianBlur(ep_lg_gray_img, (21, 21), 0)
ep_lg_element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
ep_lg_erode = cv2.erode(ep_lg_gray_img, ep_lg_element)

oc_lg_gray_img = cv2.cvtColor(oc_lg, cv2.COLOR_BGR2RGB)
oc_lg_gray_img = cv2.GaussianBlur(oc_lg_gray_img, (21, 21), 0)
element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
oc_lg_erode = cv2.erode(oc_lg_gray_img, element)

oc_lg2_gray_img = cv2.cvtColor(oc_lg2, cv2.COLOR_BGR2RGB)
oc_lg2_gray_img = cv2.GaussianBlur(oc_lg2_gray_img, (21, 21), 0)

oc_lg2_erode = cv2.erode(oc_lg2_gray_img, element)

ep = cv2.imread(path + 'ex_empty.jpg')
oc = cv2.imread(path + 'ex_ocupity.jpg')


ep_gray_img = cv2.cvtColor(ep, cv2.COLOR_BGR2RGB)
ep_gray_img = cv2.GaussianBlur(ep_gray_img, (21, 21), 0)
ep_erode = cv2.erode(ep_lg_gray_img, element)

oc_gray_img = cv2.cvtColor(oc, cv2.COLOR_BGR2RGB)
oc_gray_img = cv2.GaussianBlur(oc_gray_img, (21, 21), 0)
oc_erode = cv2.erode(oc_gray_img, element)


diff_img = cv2.absdiff(ep_lg_erode, oc_lg_erode)
cv2.imwrite(path + "ex_el_ol_diff.jpg", diff_img)
gray = cv2.cvtColor(diff_img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    if cv2.contourArea(c) < 2000:  # 设置敏感度
        continue
    else:
        # print(cv2.contourArea(c))
        print("el ol 前一帧和当前帧不一样了, 有什么东西在动!")

        break


diff_img = cv2.absdiff(ep_erode, ep_lg_erode)
cv2.imwrite(path + "ex_ep_el_diff.jpg", diff_img)
gray = cv2.cvtColor(diff_img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    if cv2.contourArea(c) < 2000:  # 设置敏感度
        continue
    else:
        # print(cv2.contourArea(c))
        print("el ep_lg 前一帧和当前帧不一样了, 有什么东西在动!")

        break


diff_img = cv2.absdiff(ep_erode, oc_erode)

gray = cv2.cvtColor(diff_img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    if cv2.contourArea(c) < 2000:  # 设置敏感度
        continue
    else:
        img = ep_erode.copy()
        cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
        cv2.imwrite(path + "ex_ep_oc_diff.jpg", img)
        print("ep oc 前一帧和当前帧不一样了, 有什么东西在动!")

        break


diff_img = cv2.absdiff(ep_erode, oc_lg_erode)

gray = cv2.cvtColor(diff_img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    if cv2.contourArea(c) < 2000:  # 设置敏感度
        continue
    else:
        # print(cv2.contourArea(c))
        img = oc_lg_erode.copy()
        cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
        cv2.imwrite(path + "ex_ep_ol_diff.jpg", img)
        print("el oc_lg 前一帧和当前帧不一样了, 有什么东西在动!")

        break


diff_img = cv2.absdiff(oc_lg2_erode, oc_lg_erode)

gray = cv2.cvtColor(diff_img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    if cv2.contourArea(c) < 2000:  # 设置敏感度
        continue
    else:
        # print(cv2.contourArea(c))
        img = oc_lg_erode.copy()
        cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
        cv2.imwrite(path + "ex_ol2_ol_diff.jpg", img)
        print("oc_lg2 oc_lg 前一帧和当前帧不一样了, 有什么东西在动!")

        break


diff_img = cv2.absdiff(ep_lg_erode, oc_erode)

gray = cv2.cvtColor(diff_img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)
# mask = cv2.adaptiveThreshold(ex_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
    if cv2.contourArea(c) < 2000:  # 设置敏感度
        continue
    else:
        # print(cv2.contourArea(c))
        img = oc_lg_erode.copy()
        cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
        cv2.imwrite(path + "ex_epl_oc_diff.jpg", img)
        print("eplg  oc 前一帧和当前帧不一样了, 有什么东西在动!")

        break
