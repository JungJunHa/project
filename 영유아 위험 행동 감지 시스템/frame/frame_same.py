vidcap = cv2.VideoCapture(video_path)
total_frames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
frames_step = total_frames//n
for i in range(n):
    #here, we set the parameter 1 which is the frame number to the frame (i*frames_step)
    vidcap.set(1,i*frames_step)
    success,image = vidcap.read()  
    #save your image
    cv2.imwrite(path,image)
vidcap.release()
