import cv2
import numpy as np
'''
        created on Tues jan 08:28:51 2018
        @author: ren_dong
        
        contour detection
        cv2.findContours()    尋找輪廓
        cv2.drawContours()    繪製輪廓


'''
#載入影象img
img = cv2.imread('smoke_1.jpg',-1)
img = cv2.resize(img,(400,400))
cv2.imshow('origin', img)
'''

灰度化處理,注意必須呼叫cv2.cvtColor(),
如果直接使用cv2.imread('1.jpg',0),會提示影象深度不對,不符合cv2.CV_8U


'''
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

#呼叫cv2.threshold()進行簡單閾值化,由灰度影象得到二值化影象
#  輸入影象必須為單通道8位或32位浮點型
ret, thresh = cv2.threshold(gray, 200, 255, 0)
cv2.imshow('thresh', thresh)

#呼叫cv2.findContours()尋找輪廓,返回修改後的影象,輪廓以及他們的層次
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#cv2.imshow('image', image)


print('contours[0]:',contours[0])
print('len(contours):',len(contours))
print('hierarchy.shape:',hierarchy.shape)
print('hierarchy:',hierarchy)

#呼叫cv2.drawContours()在原圖上繪製輪廓
img = cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
cv2.imshow('contours', img)



cv2.waitKey()
cv2.destroyAllWindows()