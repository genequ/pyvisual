from pyvisual import find, wait, click, type, App
import logging

logging.basicConfig(level=logging.DEBUG)

def test_notepad():
    # Open Notepad
    notepad = App("notepad")
    if not notepad.open():
        print("Failed to open Notepad")
        return

    # Type some text
    if type("Hello, World!"):
        print("Successfully typed text")
    else:
        print("Failed to type text")

    # Try to find and click something
    if find("save_button.png"):
        if click("save_button.png"):
            print("Successfully clicked save button")
    else:
        print("Save button not found")

    # Close Notepad
    if not notepad.close():
        print("Failed to close Notepad")

if __name__ == "__main__":
    test_notepad()