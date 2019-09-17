import cv2
print(cv2.__version__)

countVideo = 7
count = 0

for i in range(countVideo):
	vidcap = cv2.VideoCapture(str(i+1)+'.mp4')
	print ("LOADING VIDEO: "+str(i+1)+'.mp4')

	success,image = vidcap.read()
	success = True
	while success:
	  if(count % 10)==0:
	  	cv2.imwrite("SAVE/frame%d.png" % count, image)     # save frame as PNG file
	  success,image = vidcap.read()
	  count += 1
	print ("SUCESS IN SAVE VIDEO: "+str(i+1)+'.mp4')

