import cv2 #for image processing
import numpy as np #to store image
import sys
import os
from pathlib import Path

def color_quantization(img, k):
# Transform the image
  data = np.float32(img).reshape((-1, 3))

# Determine criteria
  criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)

# Implementing K-Means
  ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
  center = np.uint8(center)
  result = center[label.flatten()]
  result = result.reshape(img.shape)
  return result

def edge_mask(img, line_size, blur_value):
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  gray_blur = cv2.medianBlur(gray, blur_value)
  edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, blur_value)
  return edges


def cartoonify(ImagePath, ImageName):
    originalmage = cv2.imread(ImagePath)
    originalmage = cv2.cvtColor(originalmage, cv2.COLOR_BGR2RGB)
    line_size = 7
    blur_value = 7
    edges = edge_mask(originalmage, line_size, blur_value)

    total_color = 9
    originalmage = color_quantization(originalmage, total_color)

    blurred = cv2.bilateralFilter(originalmage, d=7, sigmaColor=200, sigmaSpace=200)
    cartoon = cv2.bitwise_and(blurred, blurred, mask=edges)

    return save(cartoon, ImagePath, ImageName)

def save(ReSized6, ImagePath, ImageName):
    # path1 = os.path.dirname(ImagePath)
    # extension=os.path.splitext(ImagePath)[1]
    BASE_DIR = Path(__file__).resolve().parent.parent
    # path = os.path.join(path1, extension)
    #
    # cv2.imwrite(path, cv2.cvtColor(ReSized6, cv2.COLOR_RGB2BGR))

    path1 = os.path.dirname(ImagePath)
    # extension=os.path.splitext(ImagePath)[1]
    extension = '.jpeg'
    path = os.path.join(path1, extension)
    newName="cartoonified_Image"
    STATIC_DIR = os.path.join(BASE_DIR, 'cartoon\\static', newName+extension)
    print(STATIC_DIR)
    cv2.imwrite(STATIC_DIR, cv2.cvtColor(ReSized6, cv2.COLOR_RGB2BGR))

output = cartoonify(sys.argv[1], sys.argv[2])
# cv2.imshow('img', org)
# originalmage = cv2.cvtColor(org, cv2.COLOR_BGR2RGB)