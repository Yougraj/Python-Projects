from ctypes import resize
import cv2

img=cv2.imread("anime.jpg",0)

print(type(img))
print(img)
print(img.shape)

resized_image = cv2.resize(img,(int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Anime", resized_image)
cv2.imwrite("Anime_resized.jpg", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()