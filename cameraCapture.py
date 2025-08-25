import cv2

cam = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(1)
cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    ret2, frame2 = cam2.read()
    if not ret:
        print("failed to grab frame")
        break


    k = cv2.waitKey(1)

    if k%256 == 32:
        # SPACE pressed

        cv2.imshow("test", frame2)

    else:
        cv2.imshow("test", frame)
cam.release()

cv2.destroyAllWindows()
