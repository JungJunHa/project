import cv2

vidcap = cv2.VideoCapture('C:\\Users\\user\\Desktop\\high1.mp4')

count = 0

while(vidcap.isOpened()):
    ret, image = vidcap.read()
    image = cv2.resize(image, (238, 158))


    # 20프레임당 하나씩 이미지 추출
    if(int(vidcap.get(1)) % 5 == 0):
        print('Saved frame number : ' + str(int(vidcap.get(1))))
        cv2.imwrite("C:\\Users\\user\\high\\02\\%d.jpg" % count, image)

        count += 1

vidcap.release()
