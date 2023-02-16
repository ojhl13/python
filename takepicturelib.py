
import cv2
import time

def takepicture():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        print('error')
    k = cv2.waitKey(1)
    time.sleep(3)
    img_name = "opencv_frame.png"
    cv2.imwrite(img_name, frame)

    print("{} written!".format(img_name))
    cam.release()
    cv2.destroyAllWindows()

#takepicture()