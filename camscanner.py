import cv2
import numpy as np

point = np.zeros((4,2),np.int64)
count = 0

def Coordinates(event,x,y,flags,params):
    global count
    if event == cv2.EVENT_LBUTTONDOWN:
        point[count] = x,y
        count = count + 1
        
path = input("enter the path of your picture : \n")
img = cv2.imread(path, 1)

while True :
    
    if count == 4:
        height = 500
        width = 500
        p1 = np.float32([point[0],point[1],point[2],point[3]])
        p2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(p1,p2)
        camscanner = cv2.warpPerspective(img,matrix,(width,height))
        cv2.destroyWindow("input")
        cv2.imshow("camscanner",camscanner)
        break
    
    for x in range(0,4):
       cv2.circle(img,(point[x][0],point[x][1]),2,(255,0,0),cv2.FILLED)
       
    cv2.imshow("input",img)
    cv2.setMouseCallback("input",Coordinates)
    cv2.waitKey(1)

