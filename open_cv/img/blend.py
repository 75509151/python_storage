import cv2
# Load two images

path = "/home/mm/code_dept/python/resource/img/"

img1 = cv2.imread(path + 'boy.jpg')
img2 = cv2.imread(path + 'opencv_logo.png')
print img2.shape
img3 = img1[:113, :107]

dst = cv2.addWeighted(img3, 0.7, img2, 0.3, 0)
cv2.imwrite(path + "blend.jpg", dst)
