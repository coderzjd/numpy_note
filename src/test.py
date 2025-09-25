import cv2
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(BASE_DIR, 'info.png')
# 1. 读图
img = cv2.imread(img_path)
if img is None:
    raise FileNotFoundError('info.png 不在当前目录！')
print('图像尺寸：', img.shape)  # (高, 宽, 通道数)
h, w = img.shape[:2]
h2, w2 = h , w // 2         # 1/4 尺寸

# 2. 截取左上 1/4
top_left = img[:h2, :w2].copy()      # .copy() 让子图连续内存，后面画框不影晌原图
cv2.imshow('top-left 1/4', top_left)

# 3. 把原图对应区域染成纯白
img[:h2, :w2] = (255, 255, 255)      # BGR 顺序
cv2.imshow('after fill white', img)

cv2.waitKey(0)
cv2.destroyAllWindows()