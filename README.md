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
5. Find contours, draw contours and save the graysacle image into ./Samples
6. Show desktop and AppOpener to launch MS-Paint
7. Maximize Microsoft Paint window, check the active window to ensure the MS-Paint is on top
8. Load coordinates from contours, click and drag to draw and check the active window
9. Save the sketch into ./Output and exit MS-Paint
10. Move the mouse cursor to the center of screen


Tips
- Take the mouse pointer to upper-left corner of the screen to stop GUI-Automation (Activating Failsafe feature of pyautogui)
- May require to change pyautogui.PAUSE to Specify to take a pause (in ssecond) between every function call for GUI-Automation


Examples
[screen-recorder-wed-mar-20-2024-10-12-48.webm](https://github.com/yongyewhon/Python-Automation-Drawing-In-Microsoft-Paint-Application/assets/151745867/dc200fdb-5190-45c7-beaf-4b9c4bb78182)

[screen-recorder-wed-mar-20-2024-10-48-50.webm](https://github.com/yongyewhon/Python-Automation-Drawing-In-Microsoft-Paint-Application/assets/151745867/b15feeee-9f50-416e-92f8-c8efdf59a185)
