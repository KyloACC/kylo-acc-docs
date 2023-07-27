import pyautogui
import time
import sys
import math

# Start by being in the cockpit view and before you want to record like so:
# https://cdn.discordapp.com/attachments/1015611698348036096/1134087411006177440/lGXguhSBSyloJM08yEM7lulWsxITvpM4uZev5LwRRZBzi3uEeBY9Wkppl14eEFdDxXjlO.png
# Wait for a few seconds before starting the key presses

def print_countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"\r{i:2}", end='', flush=True)  # Print with a width of 2 characters and flush the output
        time.sleep(1)  # Wait for 1 second
    print("\rCountdown complete!")  # Clear the line and print the final message

def recording(wait_time, skip_back_amount, recording_time):
    pyautogui.press('up')    # Arrow Up
    print("Arrow Up")
    time.sleep(wait_time)    # Wait 100ms
    pyautogui.press('up')    # Arrow Up
    print("Arrow Up")
    time.sleep(wait_time)    # Wait 100ms
    pyautogui.press('enter') # Simulate pressing the Enter key
    print("Enter")
    print(f"Recording for {recording_time} seconds")
    print_countdown(recording_time)
    time.sleep(wait_time)    # Wait 100ms
    pyautogui.press('enter') # Simulate pressing the Enter key
    print("Enter")
    pyautogui.press('left')  # Arrow Left
    print("Left")
    time.sleep(wait_time)    # Wait 100ms
    for i in range(skip_back_amount):      
        pyautogui.press('enter') # Simulate pressing the Enter key
        print("Enter")
        time.sleep(wait_time)    # Wait 100ms
        
    for i in range(6):      
        pyautogui.press('f1') # Simulate pressing the Enter key
        print("F1")
        time.sleep(wait_time)    # Wait 100ms

    pyautogui.press('right')  # Arrow right
    print("Arrow Right")
    time.sleep(wait_time)    # Wait 100ms
    pyautogui.press('enter') # Simulate pressing the Enter key
    print("Enter")
    print(f"Recording for {recording_time} seconds")
    print_countdown(recording_time)
    pyautogui.press('enter') # Simulate pressing the Enter key
    print("Enter")
    time.sleep(wait_time)    # Wait 100ms
    pyautogui.press('left')  # Arrow Left
    print("Left")
    time.sleep(wait_time)    # Wait 100ms
    for i in range(skip_back_amount):      
        pyautogui.press('enter') # Simulate pressing the Enter key
        print("Enter")
        time.sleep(wait_time)    # Wait 100ms
        
    pyautogui.press('f1') # Simulate pressing the Enter key
    print("F1")
    time.sleep(wait_time)    # Wait 100ms
    pyautogui.press('right')  # Arrow right
    time.sleep(wait_time)    # Wait 100ms
    print("Arrow Right")

def swap_car_behind(wait_time):
    for i in range(5):
        pyautogui.press('right')  # Arrow right
        time.sleep(wait_time)    # Wait 100ms
        print("Arrow Right")
    pyautogui.press('enter')
    time.sleep(wait_time)    # Wait 100ms
    print("Enter")
    for i in range(5):
        pyautogui.press('left')  # Arrow right
        time.sleep(wait_time)    # Wait 100ms
        print("Arrow Left")

def swap_car_front(wait_time):
    for i in range(4):
        pyautogui.press('right')  # Arrow right
        time.sleep(wait_time)    # Wait 100ms
        print("Arrow Right")
    pyautogui.press('enter')
    time.sleep(wait_time)    # Wait 100ms
    print("Enter")
    for i in range(4):
        pyautogui.press('left')  # Arrow right
        time.sleep(wait_time)    # Wait 100ms
        print("Arrow Left")

def heli_cam(wait_time, skip_back_amount, recording_time):
    for i in range(2):
        pyautogui.press("f6") # f6 for heli cam, with camera.json
        time.sleep(wait_time)    # Wait 100ms
    pyautogui.press('up')    # Arrow Up
    print("Arrow Up")
    time.sleep(wait_time)    # Wait 100ms
    pyautogui.press('up')    # Arrow Up
    print("Arrow Up")
    time.sleep(wait_time)    # Wait 100ms
    pyautogui.press('enter') # Simulate pressing the Enter key
    print("Enter")
    print(f"Recording for {recording_time} seconds")
    print_countdown(recording_time)
    time.sleep(wait_time)    # Wait 100ms
    pyautogui.press('enter') # Simulate pressing the Enter key
    print("Enter")



def main():
    if len(sys.argv) < 2:
        print("Please provide a recording time argument.")
        sys.exit(1)

    try:
        recording_time = math.ceil(int(sys.argv[1]) / 5) * 5
    except ValueError:
        print("Invalid time argument. Please provide an integer.")
        sys.exit(1)

    # Define the global wait time in milliseconds (100ms = 0.1 seconds)
    wait_time = 0.1
    skip_back_amount = int(recording_time / 5)
    
    print_countdown(10)
    recording(wait_time, skip_back_amount, recording_time)
    swap_car_behind(wait_time)
    recording(wait_time, skip_back_amount, recording_time)
    swap_car_front(wait_time)
    heli_cam(wait_time, skip_back_amount, recording_time)
    print("Done recording")

if __name__ == "__main__":
    main()
