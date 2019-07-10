import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade= cv2.CascadeClassifier('haarcascade_smile.xml')

def detect(frame,gray):
	faces=face_cascade.detectMultiScale(gray,1.3,5);
	for(x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		roi_frame=frame[y:y+h,x:x+h]
		roi_gray=gray[y:y+h,x:x+h]
		eyes=eye_cascade.detectMultiScale(roi_gray,1.1,22)
		smile=smile_cascade.detectMultiScale(roi_gray,1.7,22)
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_frame,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		for(sx,sy,sw,sh) in smile:
			cv2.rectangle(roi_frame,(sx,sy),(sx+sw,sy+sh),(0,0,255),2)
	return frame
video_capture= cv2.VideoCapture(0)
while True:
	_,frame=video_capture.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	canvas=detect(frame,gray)
	cv2.imshow('Video',canvas)
	if cv2.waitKey(1) & 0xFF == ord('1'):
		break 
video_capture.release()
cv2.destroyAllWindows()		
