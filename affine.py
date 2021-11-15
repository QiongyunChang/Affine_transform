'''
Affine transform
'''

import numpy as np
import cv2

def rotate(image,matrix):
    h = np.shape(image)[0]
    w = np.shape(image)[1]
    imageLen_X = w
    imageLen_Y = h
    x = np.arange(imageLen_X)  # create coordinate system centered at (x,y = 0,0)
    y = np.arange(imageLen_Y)
    X, Y = np.meshgrid(x, y)
    matrix = np.linalg.inv(matrix)
    Xrot = matrix[0,0]*X + matrix[0,1]* Y + matrix[0,2]
    Yrot =  matrix[1,0]*X + matrix[1,1]* Y + matrix[1,2]
    # shift back to original image coordinates, round values to make indices
    XrotCor = np.round(Xrot)
    XrotCor = XrotCor.astype('int')
    YrotCor = np.round(Yrot)
    YrotCor = YrotCor.astype('int')
    projMatrix = np.zeros((h, w,3), dtype=np.uint8)
    # after rotating, you'll inevitably have new coordinates that exceed the size of the original
    m0, m1 = np.where((XrotCor >= 0) & (XrotCor <= (imageLen_X - 1)) & (YrotCor >= 0) & (YrotCor <= (imageLen_Y - 1)))  # 返回符合條件的item位置(m0,m1)
    projMatrix[m0, m1, :] = image[YrotCor[m0, m1], XrotCor[m0, m1], :]
    # projMatrix = projMatrix[:160,:190,:]
    cv2.imshow('', projMatrix[:160,:190,:]) # 有 resize 的
    # cv2.imshow('', projMatrix)
    cv2.waitKey(0)
    cv2.imwrite('fe.jpg', projMatrix[:160,:190,:]) # 有 resize 的
    # cv2.imwrite('outg_TomHanksApr09.jpg', projMatrix)
    return projMatrix




