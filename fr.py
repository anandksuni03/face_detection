import cv2
face_cap = cv2.CascadeClassifier("path to haarcascade_frontalface_default.xml file in your pc")

video_cap = cv2.VideoCapture(0) # to run the camera in run time
while True :
   
    ret , video_data = video_cap.read()
    video_data = cv2.flip(video_data , 2)
    col = cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)
    faces= face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30 , 30),
        flags=cv2.CASCADE_SCALE_IMAGE 
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("video_live",video_data)
    if cv2.waitKey(10) == ord("q"): # when q is pressed the camera will turn off
        break
      
video_cap.release()
    
# heloloo