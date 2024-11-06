import pyautogui

class Keyboard:
    @staticmethod
    def type(text: str, interval: float = 0.1):
        """Type text with specified interval between keystrokes"""
        pyautogui.write(text, interval=interval)
    
    @staticmethod
    def hotkey(*args):
        """Press multiple keys simultaneously"""
        pyautogui.hotkey(*args)
    
    @staticmethod
    def press(key: str):
        """Press a single key"""
        pyautogui.press(key)