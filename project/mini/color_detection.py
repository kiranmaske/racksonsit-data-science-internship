import numpy as np
import pandas as pd
import cv2
import argparse

#crerating argumenrt parser to take image path from command line
ap =argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image")
args=vars(ap.parse_args())
# load the image and display it to our screen
img_path=(args["image"])
img=cv2.imread(img_path)

clicked=False
r=g=b=xpos=ypos=0
index=['color','color_name','hex','R','G','B']
csv=pd.read_csv('colors.csv',names=index,header=None)
def getColorName(R,G,B):
    minimum=10000
    for i in range(len(csv)):
        d=abs(R-int(csv.loc[i,"R"]))+abs(G-int(csv.loc[i,"G"]))+abs(B-int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum=d
            cname = csv.loc[i,"color_name"]
    return cname

#function to get x, y coordinate of mouse click
def draw_function(event,x,y,flags,param):
    if event == cv2.EVENT_FLAG_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos,clicked
        clicked=True
        xpos=x
        ypos=y
        b,g,r=img[y,x]
        b=int(b)
        g= int(g)
        r=int(r)

cv2.namedWindow('image')
cv2.setMouseCallback("image",draw_function)

while(1):
    cv2.imshow("image",img)
    if (clicked):
        cv2.rectangle(img,(20,20),(750,60),(b,g,r),-1)
        text = getColorName(r,g,b)+'R =  '+str(r) + 'G = '+str(g) + 'B = '+str(b)
        cv2.putText(img,text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
        clicked=False
    if cv2.waitKey(20) & 0xFF ==27:
        break
cv2.destroyAllWindows()
