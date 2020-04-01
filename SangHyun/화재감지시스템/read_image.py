import PIL.Image as pilimg
import numpy as np
import matplotlib.pyplot as plt
 
# 이미지 읽어오기
YOUR_IMAGE_PATH = "C:\\TEST\\적외선영상.png"
im = pilimg.open(YOUR_IMAGE_PATH)

# 이미지픽셀데이터를 array로 바꿈
pix = np.array(im)
pix.shape

from PIL import Image
im = Image.fromarray(pix)
im.save("C:\\TEST\\적외선영상2.png")