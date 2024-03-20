# Python-Automation-Drawing-In-Microsoft-Paint-Application
Python Script to open MS-Paint in Windows10 and draw the image
PyAutoGUI to control keyboard and mouse movements
AppOpener to launch MS-Paint


Prerequisites
- pip install opencv-python==4.6.0.66
- pip install pyautogui
- pip install appopner
- pip install imutils


Steps
1. Place images into ./Images folder
2. Change the image path from code line 13 
3. Run python auto-paint.py
4. Load the image, convert it to grayscale and threshold
5. Find contours, draw contours on white background and save the graysacle image into ./Samples
6. Show desktop and AppOpener to launch MS-Paint
7. Maximize Microsoft Paint window, check the active window to ensure the MS-Paint is on top
8. Load coordinates from contours, click and drag to draw and check the active window
9. Save the sketch into ./Output and exit MS-Paint
10. Move the mouse cursor to the center of screen


Tips
- Take the mouse pointer to upper-left corner of the screen to stop GUI-Automation (Activating Failsafe feature of pyautogui)
- May require to change pyautogui.PAUSE to Specify to take a pause (in ssecond) between every function call for GUI-Automation


Examples from screen recorder

[screen-recorder-wed-mar-20-2024-11-38-13.webm](https://github.com/yongyewhon/Python-Automation-Drawing-In-Microsoft-Paint-Application/assets/151745867/ea23b2ca-a201-4259-860f-ac9118d184c0)
[screen-recorder-wed-mar-20-2024-11-39-59.webm](https://github.com/yongyewhon/Python-Automation-Drawing-In-Microsoft-Paint-Application/assets/151745867/bdba6fea-267f-4f86-b20b-bc2731a11dc3)
[screen-recorder-wed-mar-20-2024-11-43-29.webm](https://github.com/yongyewhon/Python-Automation-Drawing-In-Microsoft-Paint-Application/assets/151745867/50aa01e0-cc20-4952-b694-6bda217abff5)
[screen-recorder-wed-mar-20-2024-11-45-21.webm](https://github.com/yongyewhon/Python-Automation-Drawing-In-Microsoft-Paint-Application/assets/151745867/bfed71f7-adf6-49dd-9e83-1dd782443fad)
