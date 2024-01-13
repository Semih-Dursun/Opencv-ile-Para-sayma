# -*- coding: utf-8 -*- semihdursun
import cv2 
import numpy as np 
resim=cv2.imread("paralar.jpg")

imgGRAY = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
imgBlurred = cv2.blur(imgGRAY,(7,7))


cv2.imshow("paralar gri ",imgGRAY)




kernel = np.ones((7,7), dtype=np.uint8)
imgCanny = cv2.Canny(imgBlurred,50,60) 
cv2.imshow("canny hali",imgCanny)
_,thresh = cv2.threshold(imgBlurred,75,255,cv2.THRESH_BINARY)
 
opening = cv2.morphologyEx(imgBlurred,cv2.MORPH_OPEN,kernel,iterations=2)


circles = cv2.HoughCircles(opening, cv2.HOUGH_GRADIENT, 1, 20, 
                           minRadius=30, maxRadius=150,param1=60, param2=30)

circles = np.uint16(np.around(circles)) 
for circle in circles:
    for x,y,r in circle:
        
        cv2.circle(resim, (x,y), r, [0,0,255], 2) 
        cv2.circle(resim, (x,y), 2, [0,0,0], 2)
        
        








# birlikler 60tan sonra 150 arası, 50 krş 55 ile 60 arası, 25 krş da 50 ile 55 arsı ,10 krş da 45 ile 48 arası




birlik=cv2.HoughCircles(opening, cv2.HOUGH_GRADIENT, 1, 20, 
                           minRadius=60, maxRadius=150,param1=60, param2=30) 

birlik = np.uint16(np.around(birlik))


    

ellilik=cv2.HoughCircles(opening, cv2.HOUGH_GRADIENT, 1, 20, 
                           minRadius=55, maxRadius=60,param1=60, param2=30)

ellilik = np.uint16(np.around(ellilik))


yirmibes=cv2.HoughCircles(opening, cv2.HOUGH_GRADIENT, 1, 20, 
                           minRadius=50, maxRadius=55,param1=60, param2=30) 

yirmibes = np.uint16(np.around(yirmibes))



onluk=cv2.HoughCircles(opening, cv2.HOUGH_GRADIENT, 1, 20, 
                           minRadius=45, maxRadius=48,param1=60, param2=30) 

onluk = np.uint16(np.around(onluk))


bes=cv2.HoughCircles(opening, cv2.HOUGH_GRADIENT, 1, 20, 
                           minRadius=30, maxRadius=42,param1=60, param2=30) 

bes = np.uint16(np.around(bes))

 


a=len(birlik[0])*1
b=len(ellilik[0])*0.5
c=len(yirmibes[0])*0.25
d=len(onluk[0])*0.1
e=len(bes[0])*0.05
toplam=a+b+c+d +e
print("resimde gözüken bozuk paaların toplamı {} TL'dir ".format(toplam) ) 




x="Toplam="+str(toplam)
cv2.putText(resim,x,(400,590),cv2.FONT_HERSHEY_SCRIPT_COMPLEX ,1,[0,0,0])


cv2.imshow("resim",resim ) 

if cv2.waitKey(0)==27 & 0xFF == ord("q"): # veya'dan sonra yazdığım şey ise q ya basılır ise de çıkış yap demek için
     
    cv2.destroyAllWindows() 






cv2.destroyAllWindows() 
