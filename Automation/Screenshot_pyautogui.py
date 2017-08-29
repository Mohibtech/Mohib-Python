import pyautogui,time

for i in range(3):
    im2 = pyautogui.screenshot('./pics/screenshot_{}.png'.format(i))
    time.sleep(3)
