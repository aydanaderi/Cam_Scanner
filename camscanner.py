import cv2
import numpy as np

circles = np.zeros((4,2),np.int64)
counter = 0

def point_camscanner(event,x,y,flags,params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x,y
        counter = counter + 1
path = input("enter the path of your picture : \n")
img = cv2.imread(path, 1)
while True :
    if counter == 4:
        height , width = 500 , 600
        points = np.float32([circles[0],circles[1],circles[2],circles[3]])
        new_points = np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(points,new_points)
        perspective = cv2.warpPerspective(img,matrix,(width,height))
        cv2.destroyWindow("original")
        cv2.imshow("camscanner",perspective)
        break
    for x in range(0,4):
       cv2.circle(img,(circles[x][0],circles[x][1]),3,(255,0,0),cv2.FILLED)
    cv2.imshow("original",img)
    cv2.setMouseCallback("original",point_camscanner)
    cv2.waitKey(1)

