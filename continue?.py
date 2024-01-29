import Quartz
from AppKit import NSWorkspace
import pyautogui
import time

def get_window_list():
    window_list = []
    window_info_list = Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListOptionOnScreenOnly, Quartz.kCGNullWindowID)
    for window_info in window_info_list:
        window_list.append(window_info)
    return window_list

def get_window_with_title(title):
    for window in get_window_list():
        window_title = window.get('kCGWindowName', 'No Title')
        if window_title == title:
            return window
    return None

def similar_colors(col1, col2, tolerance):
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(col1, col2))

def click_color_in_window(window_title, target_color, color_tolerance):
    window = get_window_with_title(window_title)
    if window:
        print(f"Found window: {window_title}")
        window_bounds = window['kCGWindowBounds']
        x = int(window_bounds['X'])
        y = int(window_bounds['Y'] + 80) 
        width = int(window_bounds['Width'])
        height = int(window_bounds['Height'] - 80) # Allow for speaker button to be blue by removing top banner of the window
        
        print(f"Window position and size: x={x}, y={y}, width={width}, height={height}")
        
        print(f"Target color: {target_color}")
        
        # Take a screenshot of the window
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
         #screenshot.save('./data/screenshot.png')
        print("Screenshot taken")

        # Search for the color with tolerance
        color_found = False
        for i in range(screenshot.width):
            for j in range(screenshot.height):
                current_color = screenshot.getpixel((i, j))
                if similar_colors(current_color, target_color, color_tolerance):
                    color_found = True
                    # Save current mouse position
                    original_mouse_position = pyautogui.position()
                    # Click on the color
                    click_x = x + i
                    click_y = y + j
                    pyautogui.click(click_x, click_y)
                    print(f"Clicked at: x={click_x}, y={click_y}")
                    # Return mouse to original position
                    pyautogui.moveTo(original_mouse_position)
                    pyautogui.click()
                    print(f"Clicked at original position: {original_mouse_position}")
                    break
            if color_found:
                break

        if not color_found:
            print("Target color not found in the window.")
    else:
        print("No window with the specified title found.")

# Replace 'Blink' with the title of the window you're looking for
window_title = "Blink"
# Define the color you want to find (RGB format) and the tolerance
target_color = (69, 175, 228)  # Replace with your target color
color_tolerance = 25  # Define how much the color can vary

while True:
    click_color_in_window(window_title, target_color, color_tolerance)
    time.sleep(10)  # Wait