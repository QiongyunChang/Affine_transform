'''
Main file
'''

import cv2
import sys
import numpy as np
import matplotlib.pylab as plt
a = []; b = []

#  滑鼠點擊選取點座標
def onmouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN :
        xy = "%d,%d" % (x, y)
        a.append(x) # x 軸
        b.append(y) # y 軸
        cv2.circle(img, (x, y), 1, (0, 0, 255), thickness=-1)
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (0, 0, 0), thickness=1)
        cv2.imshow("image", img)

        # print(x, y)


if __name__ == '__main__':
    img_path = "123.jpg"
    img = cv2.imread(img_path)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', onmouse)
    while 1:
        cv2.imshow('image', img)
        k = cv2.waitKey(1)
        # 判斷是否按下畫面的 X 來關閉、結束 click
        if cv2.getWindowProperty('image', cv2.WND_PROP_VISIBLE) < 1:
            break
    cv2.destroyAllWindows()
    # print(a,b)
    # 把選取的點放入
    p = np.array((a, b, [1, 1, 1]))
    p_prime = np.array(([65, 95, 80], [90, 90, 120], [1, 1, 1]))

    # B -> A
    from affine import rotate
    img = cv2.imread(img_path)
    trans = np.dot(p_prime, np.linalg.inv(p))
    pro = rotate(img,trans)
    # plt.imshow(pro)
    # plt.show()

    # A -> B
    trans = np.dot(p, np.linalg.inv(p_prime))
    pro = rotate(pro, trans)
    cv2.imshow('', pro)  # 有 resize 的
    cv2.waitKey(0)
    # plt.imshow(pro)
    # plt.show()

    # from  back import getaffine, turnback
    # img = cv2.imread(img_path)
    # getaffine(p, p_prime, img)
    # img_path = "output.jpg"
    # img = cv2.imread(img_path)
    # turnback(p, p_prime, img)







