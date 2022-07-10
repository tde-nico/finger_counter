import cv2
import time
import Hand_Tracking_Module as htm


WCAM, HCAM = 640, 480


cap = cv2.VideoCapture(0) # 1 ?
cap.set(3, WCAM)
cap.set(4, HCAM)

pTime = 0

detector = htm.HandDetector(detection_con=0.7)

while 1:
	success, img = cap.read()
	img = detector.find_hands(img)
	lm_list = detector.find_position(img, draw=False)

	count = 0

	if lm_list:
		if lm_list[4][1] < lm_list[2][1]: # only left hand
				count += 1
		for id in range(8,21,4):
			if lm_list[id][2] < lm_list[id - 2][2]:
				count += 1

	cv2.putText(img, str(count), (10,HCAM-30),
		cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0), 3)

	cTime = time.time()
	fps = 1/(cTime - pTime)
	pTime = cTime

	cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
	cv2.imshow("Image", img)
	cv2.waitKey(1)
