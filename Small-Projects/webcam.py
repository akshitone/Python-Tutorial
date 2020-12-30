import cv2

img_capture = cv2.VideoCapture(0)
result = True

while result:
    ret, frame = img_capture.read()
    cv2.imwrite("test.jpg", frame)
    result = False
    print("Image captured!")

img_capture.release()
