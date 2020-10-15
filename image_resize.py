import cv2

i = 751
img = cv2.imread(r'C:\Users\ruchi\Downloads\Project\blank\IMG_20200928_125128.jpg', cv2.IMREAD_UNCHANGED)



resized = cv2.resize(img, (128,128), interpolation = cv2.INTER_AREA)
while i != 900:
    cv2.imwrite(str(i) + ".png", resized)
    i= i + 1
    
cv2.waitKey(0)
cv2.destroyAllWindows()
