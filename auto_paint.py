import cv2
import numpy as np
import imutils
import os
import time
import pyautogui
import AppOpener

cv2.waitKey(2000)
if not os.path.exists('./images'): os.makedirs('./images')
if not os.path.exists('./Samples'): os.makedirs('./Samples')
if not os.path.exists('./Output'): os.makedirs('./Output')
#Take the mouse pointer to upper-left corner of the screen to stop GUI-Automation
image_path = './images/dog.jpg' # Add the image to images folder
image_name = os.path.basename(image_path)
full_path = os.path.abspath(image_path)
save_name = full_path.replace('images', 'Output')
print(image_name, image_path, save_name)
print(pyautogui.FAILSAFE, pyautogui.PAUSE)
screenWidth, screenHeight = pyautogui.size()
center_X,center_Y = int(screenWidth/2), int(screenHeight/2)
offset = int(screenHeight/5)
print(f'Screen size = ({screenWidth}X{screenHeight}), Offset={offset}')
sample_image = cv2.imread(image_path)
height, width, _ = sample_image.shape
print(height, width)
gray = cv2.cvtColor(sample_image, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray, (8, 8))
_, thresh = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY_INV) #white backgorund
#cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#cnts = cv2.findContours(thresh.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
#cnts = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
total_contours = len(cnts)
if total_contours >= 100: pyautogui.PAUSE = 0.001
elif total_contours >= 40: pyautogui.PAUSE = 0.002
else: pyautogui.PAUSE = 0.005
print(f'Number of countours={total_contours} {pyautogui.PAUSE}')

output_image = np.zeros((height, width, 3), np.uint8)
output_image[::] = [255, 255, 255]
cv2.drawContours(output_image, cnts, -1, (0, 0, 0), 3)
cv2.imwrite(f'./Samples/{image_name}', output_image)
sample_image = cv2.hconcat((sample_image, output_image))
cv2.imshow('sample_image', sample_image)
cv2.waitKey(5000)
cv2.destroyAllWindows()
try:
    #AppOpener.open("LS")
    pyautogui.hotkey('win', 'd') # Show desktop
    AppOpener.open('paint')
    time.sleep(2)
    window = pyautogui.getActiveWindow()
    print(window.left, window.top, window.width, window.height, window.title)
    pyautogui.hotkey('win', 'up')
    time.sleep(2)
    if window.title == 'Untitled - Paint':
        ready = True
        print('Start drawing')
        for mask in cnts:
            window = pyautogui.getActiveWindow()
            if window.title == 'Untitled - Paint':
                mask_list = mask.tolist()
                x0, y0, x1, y1, x2, y2 = 0, 0, 0, 0, 0, 0
                for a in mask_list:
                    b = str(a)
                    c = b.replace("[", "").replace("]", "").split(",")
                    if x0 == 0 and y0 == 0 and x2 == 0 and y2 == 0:
                        x0, y0 = int(c[0].strip()), int(c[1].strip())+offset
                        x2, y2 = x0, y0
                    else:
                        x1, y1 = x2, y2
                        x2, y2 = int(c[0].strip()), int(c[1].strip())+offset
                        rel_x, rel_y = x2 - x1, y2 - y1
                        pyautogui.click(x1, y1)
                        pyautogui.dragRel(rel_x, rel_y)
                x1, y1 = x2, y2
                x2, y2 = x0, y0
                rel_x, rel_y = x2 - x1, y2 - y1
                pyautogui.click(x1, y1)
                pyautogui.dragRel(rel_x, rel_y)
            else:
                ready = False
                print('Error drawing')
                break
        if ready is True:
            time.sleep(2)
            pyautogui.hotkey('ctrl', 's')
            time.sleep(2)
            pyautogui.write(save_name)
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('left')
            time.sleep(0.5)
            pyautogui.press('enter')
            time.sleep(3)
            pyautogui.hotkey('alt', 'f4')
            time.sleep(0.5)
            pyautogui.moveTo(center_X, center_Y, 2)
            print('Save drawing')
except:
    print('Error')