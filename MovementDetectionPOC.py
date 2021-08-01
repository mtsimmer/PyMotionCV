#Messing with OPENCV
import cv2
import imutils

#vs = cv2.VideoCapture(r"C:\Proj\PyMotionCv\Sample\out.mp4")
vs = cv2.VideoCapture(r"C:\Users\Mtsimmer\Downloads\AccordanceSystemVideoLe165Night.mp4")

firstFrame = None

while True:
    frame = vs.read()
    frame = frame if r"C:\Users\Mtsimmer\Downloads\AccordanceSystemVideoLe165Night.mp4" == None else frame[1]
    text = "static"
    #
    #
    if frame is None:
        break
    #
    frame = imutils.resize(frame, width=1080)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    #
    #
    if firstFrame is None:
        firstFrame = gray
        continue
    #
    #
    #
    frameDelta = cv2.absdiff(firstFrame,gray)
    thresh = cv2.threshold(frameDelta, 140, 255, cv2.THRESH_BINARY)[1]
    #
    #
    thresh = cv2.dilate(thresh, None, iterations=2)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    #
    #
    for c in cnts:
        if cv2.contourArea(c) < 1000:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        text = "Dynamic"
    cv2.putText(frame, text,(10,20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
    cv2.imshow("ORGINAL",frame)
    cv2.imshow("Thresh", thresh)
    cv2.imshow("Delat", frameDelta)
    key = cv2.waitKey(1), 0xFF
    #
    if key == ord("q"):
        break
vs.release()
