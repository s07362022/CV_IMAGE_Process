import cv2
import numpy as np
import matplotlib.pyplot as plt

img =train_x1[0]

# 畫出 RGB 三種顏色的分佈圖
color = ('b','g','r')
for i, col in enumerate(color):
  histr = cv2.calcHist([img],[i],None,[256],[0, 256])
  plt.plot(histr,label="x", color = col)
  plt.xlim([0, 256])
plt.show()
