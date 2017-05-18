import cv2
# Load two images

path = "/home/mm/code_dept/python/resource/img/"

img1 = cv2.imread(path + 'boy.jpg')
img2 = cv2.imread(path + 'opencv_logo.png')
ex_img = cv2.imread(path + 'ex.jpg')

ex_gray = cv2.cvtColor(ex_img, cv2.COLOR_BGR2GRAY)
cv2.imwrite(path + "ex_gray.jpg", ex_gray)
mask = cv2.adaptiveThreshold(ex_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imwrite(path + "ex_raw_mask.jpg", mask)
# ret, mask = cv2.threshold(ex_gray, 20, 255, cv2.THRESH_BINARY)

ex_bil = cv2.bilateralFilter(ex_img, 9, 75, 75)
cv2.imwrite(path + "ex_bilater.jpg", ex_bil)

ex_gau = cv2.GaussianBlur(ex_img, (3, 3), 0)
cv2.imwrite(path + "ex_gau.jpg", ex_gau)
ex_media = cv2.medianBlur(ex_img, 3)
cv2.imwrite(path + "ex_median.jpg", ex_media)


ex_gau = cv2.GaussianBlur(mask, (3, 3), 0)
cv2.imwrite(path + "ex_gau_mask.jpg", ex_gau)
ex_media = cv2.medianBlur(mask, 3)
cv2.imwrite(path + "ex_median_mask.jpg", ex_media)
ex_bil = cv2.bilateralFilter(mask, 9, 75, 75)
cv2.imwrite(path + "ex_bilater_mask.jpg", ex_bil)

# I want to put logo on top-left corner, So I create a ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
print mask
print "-------------------"
print mask_inv
# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imwrite(path + "mask.png", mask)

cv2.imwrite(path + 'blending2.png', img1)
cv2.imwrite(path + "bg.jpg", img1_bg)
cv2.imwrite(path + "fg.jpg", img2_fg)
cv2.imwrite(path + "mask_inv.png", mask_inv)
cv2.imwrite(path + "img2gray.png", img2gray)
