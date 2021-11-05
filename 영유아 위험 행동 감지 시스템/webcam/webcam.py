import cv2
import time
capture = cv2.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 480)
img_counter = 0
frame_set = []
start_time = time.time()
while True:
    ret, image = capture.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if time.time() - start_time >= 0.2: #<---- Check if 0.2 sec passed
        image = cv2.resize(image, (64, 64))
        frame_set.append(image)
        print("{} written!".format(img_counter))
        start_time = time.time()
    img_counter += 1
    if len(frame_set)>=17:
        del frame_set[0]

print(frame_set)
