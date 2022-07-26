# 均方相似度
import cv2
import matplotlib.pyplot as plt


def getss(list):				     #計算方差
    avg=sum(list)/len(list)          #計算平均值
    ss=0
    for l in list:                   #計算方差
        ss+=(l-avg)*(l-avg)/len(list)
    return ss


def getdiff(img):                     #獲取每行像素平均值
    Sidelength=128                     #定義邊長
    img=cv2.resize(img,(Sidelength,Sidelength),interpolation=cv2.INTER_CUBIC)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    avglist=[]                        #avglist列表保存每行像素平均值
    for i in range(Sidelength):       #計算每行均值，保存到avglist列表
        avg=sum(gray[i])/len(gray[i])
        avglist.append(avg)
    return avglist

def main_diff(x1,x2):
#讀取測試圖片
    img1=x1
    diff1=getdiff(img1)
    print('img1 方均差:',getss(diff1))

    #讀取測試圖片
    img11=x2
    diff11=getdiff(img11)
    print('img11 方均差:',getss(diff11))

    x=range(128)

    plt.figure("avg")
    plt.plot(x,diff1,marker="*",label="$train$")
    plt.plot(x,diff11,marker="*",label="$test$")
    plt.title("avg")
    plt.legend()
    plt.show()
for k in range(len(test_1)):
    main_diff(train_x1[k].astype(np.uint8),test_1[k].astype(np.uint8))
