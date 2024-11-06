import pyautogui
import platform
from pathlib import Path
from typing import Union, Tuple, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Screen:
    @staticmethod
    def find(image: Union[str, Path], confidence: float = 0.9) -> Optional[Tuple[int, int]]:
        """
        Find an image on screen and return its coordinates
        
        Args:
            image: Path to the image file
            confidence: Match confidence (0-1)
        Returns:
            Tuple of (x, y) coordinates or None if not found
        """
        try:
            image_path = Path(image).resolve()
            if not image_path.exists():
                logger.error(f"Image file not found: {image_path}")
                return None
                
            location = pyautogui.locateCenterOnScreen(str(image_path), confidence=confidence)
            if location:
                logger.debug(f"Found image at coordinates: {location}")
            else:
                logger.debug(f"Image not found: {image_path}")
            return location
        except Exception as e:
            logger.error(f"Error finding image: {str(e)}")
            return None
    
    @staticmethod
    def wait(image: Union[str, Path], timeout: int = 10, confidence: float = 0.9) -> Optional[Tuple[int, int]]:
        """
        Wait for an image to appear on screen
        
        Args:
            image: Path to the image file
            timeout: Maximum time to wait in seconds
            confidence: Match confidence (0-1)
        Returns:
            Tuple of (x, y) coordinates or None if not found
        """
        try:
            image_path = Path(image).resolve()
            if not image_path.exists():
                logger.error(f"Image file not found: {image_path}")
                return None
                
            location = pyautogui.locateCenterOnScreen(
                str(image_path), 
                confidence=confidence, 
                minSearchTime=timeout
            )
            if location:
                logger.debug(f"Found image at coordinates: {location}")
            else:
                logger.debug(f"Image not found after waiting {timeout} seconds")
            return location
        except Exception as e:
            logger.error(f"Error waiting for image: {str(e)}")
            return None

    @staticmethod
    def click(target: Union[str, Path, Tuple[int, int]], confidence: float = 0.9) -> bool:
        """
        Click on an image or coordinates
        
        Args:
            target: Image path or (x, y) coordinates
            confidence: Match confidence (0-1) when using image
        Returns:
            True if click was successful, False otherwise
        """
        try:
            if isinstance(target, (str, Path)):
                location = Screen.find(target, confidence)
                if location:
                    pyautogui.click(location)
                    logger.debug(f"Clicked on image at: {location}")
                    return True
                logger.debug("Click failed: image not found")
                return False
            else:
                pyautogui.click(target)
                logger.debug(f"Clicked at coordinates: {target}")
                return True
        except Exception as e:
            logger.error(f"Error during click operation: {str(e)}")
            return False