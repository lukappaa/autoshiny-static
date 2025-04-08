import time
import pyautogui
import cv2
import numpy as np
import tkinter as tk
import threading
import os

def draw_debug_rectangle(x, y, width, height, duration=2):
    def overlay():
        root = tk.Tk()
        root.overrideredirect(True)
        root.attributes("-topmost", True)
        root.attributes("-transparentcolor", "white")
        root.geometry(f"{width}x{height}+{x}+{y}")

        canvas = tk.Canvas(root, width=width, height=height, bg='white', highlightthickness=0)
        canvas.pack()
        canvas.create_rectangle(0, 0, width, height, outline="red", width=3)

        root.after(int(duration * 1000), root.destroy)
        root.mainloop()

    threading.Thread(target=overlay).start()

    screen_region = (1, 2, 3, 4)
    #Screen region is defined as a tuple (x coordinate of top-left corner, y coordinate of top-left corner, width, height)
    #Replace 1,2,3,4 with the desired values


    time.sleep(5)
    draw_debug_rectangle(region[0], region[1], region[2], region[3], duration=2)
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save("debug_screenshot.jpg")
    screenshot_np = np.array(screenshot)
    screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
    print("Screenshot successfully saved.\n")

    return True