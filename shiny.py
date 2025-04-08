import time
import pyautogui
import cv2
import numpy as np
import tkinter as tk
import threading
import os

def press_keys(sequence):
    for key, duration, wait in sequence:
        pyautogui.keyDown(key)
        time.sleep(duration)
        pyautogui.keyUp(key)
        time.sleep(wait)

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

def mse(imageA, imageB):
    if imageA.shape != imageB.shape:
        print("Warning: Images have different shapes!")
        return float('inf')
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err
def identify_encounter_variant(region, normal_path, shiny_path, mse_threshold=300): 
    draw_debug_rectangle(region[0], region[1], region[2], region[3], duration=2)

    screen_width, screen_height = pyautogui.size()
    if (region[0] + region[2] > screen_width or 
        region[1] + region[3] > screen_height):
        print(f"Error: Region {region} is outside screen bounds {screen_width}x{screen_height}")
        return "no match"

    try:
        screenshot = pyautogui.screenshot(region=region)
        screenshot_np = np.array(screenshot)
        screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

      
        if not os.path.exists(normal_path) or not os.path.exists(shiny_path):
            print("Error: Reference images not found")
            return "no match"

        normal = cv2.imread(normal_path)
        shiny = cv2.imread(shiny_path)

        if normal is None or shiny is None:
            print("Error: Could not load reference images")
            return "no match"

        mse_normal = mse(screenshot_bgr, normal)
        mse_shiny = mse(screenshot_bgr, shiny)

        print(f"MSE vs normal: {mse_normal:.2f}, MSE vs shiny: {mse_shiny:.2f}")

        if mse_shiny < mse_normal and mse_shiny < mse_threshold:
            return "shiny"
        elif mse_normal < mse_threshold:
            return "normal"
        else:
            return "no match"
    except Exception as e:
        print(f"Error during comparison: {str(e)}")
        return "no match"


screen_region = (1, 2, 3, 4)
#Screen region is defined as a tuple (x coordinate of top-left corner, y coordinate of top-left corner, width, height)
#Replace 1,2,3,4 with the desired values


normal_image_path = r"your/path.jpg"
shiny_image_path = r"your/path.jpg"
#Enter path to the screenshots


sequence_1 = [
    ("z", 0.5, 0.2),
]
#Replace z with your A button

sequence_reset = [
    ("u", 0.2, 8),
    ("z", 0.1, 2),
    ("z", 0.1, 3),
    ("z", 0.1, 2),
    ("z", 0.1, 2),
    ("z", 0.1, 2),
]
#Customize according to the game. u is the reset shortcut on the emulator used for testing

while True:
    time.sleep(2)
    press_keys(sequence_1)
    time.sleep(13)

    result = identify__variant(screen_region, normal_image_path, shiny_image_path)
    print(f"Encounter result: {result}")

    if result == "shiny":
        print("Shiny found! Terminating program.")
        break
    elif result == "normal":
        print("Normal encounter. Resetting...")
        press_keys(sequence_reset)
        time.sleep(2)
    else:
        print("Encounter not detected. Resetting...")
        press_keys(sequence_reset)
        time.sleep(2)