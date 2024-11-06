import pyautogui
import platform
from pathlib import Path
from typing import Union, Tuple, Optional

class Screen:
    @staticmethod
    def find(image: Union[str, Path], confidence: float = 0.9) -> Optional[Tuple[int, int]]:
        """Find an image on screen and return its coordinates"""
        try:
            location = pyautogui.locateCenterOnScreen(str(image), confidence=confidence)
            return location if location else None
        except:
            return None
    
    @staticmethod
    def wait(image: Union[str, Path], timeout: int = 10, confidence: float = 0.9) -> Optional[Tuple[int, int]]:
        """Wait for an image to appear on screen"""
        try:
            location = pyautogui.locateCenterOnScreen(str(image), confidence=confidence, timeout=timeout)
            return location if location else None
        except:
            return None

    @staticmethod
    def click(target: Union[str, Path, Tuple[int, int]], confidence: float = 0.9):
        """Click on an image or coordinates"""
        if isinstance(target, (str, Path)):
            location = Screen.find(target, confidence)
            if location:
                pyautogui.click(location)
        else:
            pyautogui.click(target)