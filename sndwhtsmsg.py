import pywhatkit as pwk
import pyautogui
import time

try:
    # Send message instantly
    pwk.sendwhatmsg_instantly("+919001002886", "Hi, this is an instant message!", wait_time=15, tab_close=True)

    # Wait for WhatsApp Web to load and message to be typed
    time.sleep(10)

    # Press Enter to send the message
    pyautogui.press("enter")

    print("Message sent successfully!")

except Exception as e:
    print("Error:", e)
