import cv2
import numpy as np
from matplotlib import pyplot as plt

def result1():

    img_rgb = cv2.imread('res/trolley-1.jpg')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('res/person.jpg',0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)

    f = set()
    var1 = int(len(loc[0]))
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

        sensitivity = 100
        f.add((round(pt[0]/sensitivity), round(pt[1]/sensitivity)))

    cv2.imwrite('result-1.png',img_rgb)

    found_count = len(f)

    img_rgb = cv2.imread('res/trolley-2.jpg')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('res\person.jpg',0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)

    f = set()
    var2 = int(len(loc[0]))
    
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

        sensitivity = 100
        f.add((round(pt[0]/sensitivity), round(pt[1]/sensitivity)))

    cv2.imwrite('result-2.png',img_rgb)

    if var1 > var2:
        print('I would use first law as humans are precious to me.')
    elif var2 > var1:
        print('I would use second law as humans are precious to me.')
    

result1()