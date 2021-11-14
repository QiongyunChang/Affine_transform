# Affine_transform
### 將提供的人臉影像，利用affine transform，將人臉的位置轉換到固定位置的 template 上。 output 一張影像，大小為 160 x 190，左右眼位置分別位於這張影像上的 (65, 90) 與 (95, 90)。  鼻尖位於 (80, 120)。


## getcoordinate.py - 取得點座標
選取的點p :

![image](https://user-images.githubusercontent.com/51444652/141680336-a0d54784-ed31-4cb5-8d9f-2ef66945bd90.png)

## 目標位置p_prime : [65, 95, 80], [90, 90, 120], [1, 1, 1]  

 ![image](https://user-images.githubusercontent.com/51444652/141680326-e8043012-47b7-4664-9ed9-986200f34bf1.png)

## affine.py - 取得點座標
### 想法:  

![image](https://user-images.githubusercontent.com/51444652/141680378-e61e2d62-9a05-442e-bade-3c1a5ed432ac.png)


## B -> A : 利用 inverse matrix 找 Transform matrix 的值 
 ![image](https://user-images.githubusercontent.com/51444652/141680387-957dc18c-fce0-4a2e-b224-332129c0d3bf.png)



## 找到Transform matrix後再看每個pixel 移動過後對照原本圖片的值為多少 
並使用 np.where 處理圖片範圍 

![image](https://user-images.githubusercontent.com/51444652/141680396-df22435b-feac-4266-a752-fe0776214488.png)


## 因應題目需求將圖片存為160 * 190  
 ![image](https://user-images.githubusercontent.com/51444652/141680402-6b60aa04-d8bb-4c4a-9103-f717ff9aa1f3.png)
 ![image](https://user-images.githubusercontent.com/51444652/141680404-f7e32826-719e-4cf7-a077-de983f643f52.png)



## A -> B : 使用相同的概念一樣利用 inverse matrix 找 Transform matrix 的值 
 ![image](https://user-images.githubusercontent.com/51444652/141680408-d6182a23-dbdc-4103-94ca-9c96a1cf5632.png)
 ![image](https://user-images.githubusercontent.com/51444652/141680412-eebbab7f-693d-4cf3-8d42-2772daf09fb2.png)







