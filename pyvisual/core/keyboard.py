import pyautogui
import logging

logger = logging.getLogger(__name__)

class Keyboard:
    @staticmethod
    def type(text: str, interval: float = 0.1) -> bool:
        """
        Type text with specified interval between keystrokes
        
        Args:
            text: Text to type
            interval: Delay between keystrokes in seconds
        Returns:
            True if successful, False otherwise
        """
        try:
            pyautogui.write(text, interval=interval)
            logger.debug(f"Typed text: {text}")
            return True
        except Exception as e:
            logger.error(f"Error typing text: {str(e)}")
            return False
    
    @staticmethod
    def hotkey(*args) -> bool:
        """
        Press multiple keys simultaneously
        
        Args:
            *args: Key names to press
        Returns:
            True if successful, False otherwise
        """
        try:
            pyautogui.hotkey(*args)
            logger.debug(f"Pressed hotkey combination: {args}")
            return True
        except Exception as e:
            logger.error(f"Error pressing hotkey: {str(e)}")
            return False
    
    @staticmethod
    def press(key: str) -> bool:
        """
        Press a single key
        
        Args:
            key: Key name to press
        Returns:
            True if successful, False otherwise
        """
        try:
            pyautogui.press(key)
            logger.debug(f"Pressed key: {key}")
            return True
        except Exception as e:
            logger.error(f"Error pressing key: {str(e)}")
            return False