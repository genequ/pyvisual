import pyautogui
from pathlib import Path
from typing import Union, Tuple, Optional
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Screen:

    @staticmethod
    def _validate_confidence(confidence: float) -> float:
        """Validate confidence value is between 0 and 1"""
        if not 0 <= confidence <= 1:
            logger.warning(f"Confidence value {confidence} not in range [0,1], clamping")
            return max(0, min(confidence, 1))
        return confidence

    @staticmethod
    def _validate_timeout(timeout: int) -> int:
        """Validate timeout value is positive or -1"""
        if timeout < -1:
            logger.warning(f"Invalid timeout value {timeout}, using -1")
            return -1
        return timeout

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
        confidence = Screen._validate_confidence(confidence)
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
        confidence = Screen._validate_confidence(confidence)
        timeout = Screen._validate_timeout(timeout)
        try:
            image_path = Path(image).resolve()
            if not image_path.exists():
                logger.error(f"Image file not found: {image_path}")
                return None
                
            location = pyautogui.locateCenterOnScreen(
                str(image_path), 
                confidence=confidence, 
                timeout=timeout
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
    
    @staticmethod
    def doubleClick(target: Union[str, Path, Tuple[int, int]], confidence: float = 0.9) -> bool:
        """
        Double click on an image or coordinates
        
        Args:
            target: Image path or (x, y) coordinates
            confidence: Match confidence (0-1) when using image
        Returns:
            True if double click was successful, False otherwise
        """
        try:
            if isinstance(target, (str, Path)):
                location = Screen.find(target, confidence)
                if location:
                    pyautogui.doubleClick(location)
                    logger.debug(f"Double clicked on image at: {location}")
                    return True
                logger.debug("Double click failed: image not found")
                return False
            else:
                pyautogui.doubleClick(target)
                logger.debug(f"Double clicked at coordinates: {target}")
                return True
        except Exception as e:
            logger.error(f"Error during double click operation: {str(e)}")
            return False
    
    @staticmethod
    def rightClick(target: Union[str, Path, Tuple[int, int]], confidence: float = 0.9) -> bool:
        """
        Right click on an image or coordinates
        
        Args:
            target: Image path or (x, y) coordinates
            confidence: Match confidence (0-1) when using image
        Returns:
            True if right click was successful, False otherwise
        """
        try:
            if isinstance(target, (str, Path)):
                location = Screen.find(target, confidence)
                if location:
                    pyautogui.rightClick(location)
                    logger.debug(f"Right clicked on image at: {location}")
                    return True
                logger.debug("Right click failed: image not found")
                return False
            else:
                pyautogui.rightClick(target)
                logger.debug(f"Right clicked at coordinates: {target}")
                return True
        except Exception as e:
            logger.error(f"Error during right click operation: {str(e)}")
            return False

    @staticmethod
    def exists(image: Union[str, Path], timeout: float = 3.0, confidence: float = 0.9) -> bool:
        """
        Check if an image exists on screen within the specified timeout period (Sikuli-style)
        
        Args:
            image: Path to the image file
            timeout: Maximum time to wait in seconds (default 3.0)
            confidence: Match confidence (0-1)
        Returns:
            True if the image is found on screen within timeout, False otherwise
        """
        location = Screen.wait(image, timeout=int(timeout), confidence=confidence)
        found = location is not None
        logger.debug(f"Image exists on screen: {image} - {found}")
        return found
    
    @staticmethod
    def highlight(target: Union[str, Path, Tuple[int, int]], duration: float = 0.5, confidence: float = 0.9) -> bool:
        """
        Temporarily highlight a region on screen around the target location
        
        Args:
            target: Image path or (x, y) coordinates
            duration: How long to show the highlight in seconds (default 0.5)
            confidence: Match confidence (0-1) when using image
        Returns:
            True if highlighting was successful, False otherwise
        """
        try:
            if isinstance(target, (str, Path)):
                location = Screen.find(target, confidence)
                if not location:
                    logger.debug("Highlight failed: image not found")
                    return False
            else:
                location = target

            # Create a temporary box around the target
            x, y = location
            box_size = 50  # Size of highlight box
            box_positions = [
                (x - box_size//2, y - box_size//2),  # Top-left
                (x + box_size//2, y - box_size//2),  # Top-right
                (x + box_size//2, y + box_size//2),  # Bottom-right
                (x - box_size//2, y + box_size//2),  # Bottom-left
                (x - box_size//2, y - box_size//2)   # Back to start
            ]
            
            # Draw the box using mouse movements
            original_pos = pyautogui.position()
            pyautogui.moveTo(*box_positions[0], duration=0)
            for pos in box_positions[1:]:
                pyautogui.moveTo(*pos, duration=duration/4)
            pyautogui.moveTo(*original_pos, duration=0)  # Return to original position
            
            logger.debug(f"Highlighted region at: {location}")
            return True
            
        except Exception as e:
            logger.error(f"Error during highlight operation: {str(e)}")
            return False
    
    @staticmethod
    def onAppears(image: Union[str, Path], handler: callable, timeout: int = -1, confidence: float = 0.9) -> None:
        try:
            start_time = time.time()
            while True:
                if timeout > 0 and (time.time() - start_time) > timeout:
                    logger.debug(f"onAppears timeout reached for: {image}")
                    break
                    
                if Screen.exists(image, timeout=1, confidence=confidence):
                    logger.debug(f"Image appeared, calling handler: {image}")
                    handler()
                    break
                    
                time.sleep(0.5)
        except Exception as e:
            logger.error(f"Error in onAppears: {str(e)}")

    @staticmethod
    def onVanish(image: Union[str, Path], handler: callable, timeout: int = -1, confidence: float = 0.9) -> None:
        try:
            start_time = time.time()
            while True:
                if timeout > 0 and (time.time() - start_time) > timeout:
                    logger.debug(f"onVanish timeout reached for: {image}")
                    break
                    
                if not Screen.exists(image, timeout=1, confidence=confidence):
                    logger.debug(f"Image vanished, calling handler: {image}")
                    handler()
                    break
                    
                time.sleep(0.5)
        except Exception as e:
            logger.error(f"Error in onVanish: {str(e)}")

    @staticmethod
    def onChange(image: Union[str, Path], handler: callable, timeout: int = -1, confidence: float = 0.9) -> None:
        try:
            start_time = time.time()
            initial_state = Screen.exists(image, timeout=1, confidence=confidence)
            
            while True:
                if timeout > 0 and (time.time() - start_time) > timeout:
                    logger.debug(f"onChange timeout reached for: {image}")
                    break
                    
                current_state = Screen.exists(image, timeout=1, confidence=confidence)
                if current_state != initial_state:
                    logger.debug(f"Image state changed, calling handler: {image}")
                    handler()
                    break
                    
                time.sleep(0.5)
        except Exception as e:
            logger.error(f"Error in onChange: {str(e)}")