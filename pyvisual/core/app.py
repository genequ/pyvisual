import platform
import subprocess
import logging
from typing import Optional
import shutil

logger = logging.getLogger(__name__)

class App:
    def __init__(self, app_name: str):
        """
        Initialize App instance
        
        Args:
            app_name: Name of the application
        """
        self.app_name = app_name
        self.system = platform.system()
        self.process: Optional[subprocess.Popen] = None
        
        if self.system not in ["Darwin", "Windows"]:
            logger.warning(f"Unsupported operating system: {self.system}")

    def open(self, path: Optional[str] = None) -> bool:
        """
        Open the application
        
        Args:
            path: Optional path to file to open with the application
        Returns:
            True if successful, False otherwise
        """
        try:
            if self.system == "Darwin":  # macOS
                if path:
                    cmd = ["open", path]
                else:
                    cmd = ["open", "-a", self.app_name]
            elif self.system == "Windows":
                if path:
                    cmd = [path]
                else:
                    app_path = shutil.which(self.app_name)
                    if not app_path:
                        logger.error(f"Application not found: {self.app_name}")
                        return False
                    cmd = [app_path]
            else:
                logger.error(f"Unsupported operating system: {self.system}")
                return False
            
            self.process = subprocess.Popen(cmd)
            logger.debug(f"Opened application: {self.app_name}")
            return True
        except Exception as e:
            logger.error(f"Error opening application: {str(e)}")
            return False

    def close(self) -> bool:
        """
        Close the application
        
        Returns:
            True if successful, False otherwise
        """
        try:
            if self.process:
                self.process.terminate()
                logger.debug(f"Terminated process for: {self.app_name}")
                return True
            
            if self.system == "Darwin":
                subprocess.run(["osascript", "-e", f'quit app "{self.app_name}"'])
            elif self.system == "Windows":
                subprocess.run(["taskkill", "/F", "/IM", f"{self.app_name}.exe"])
            else:
                logger.error(f"Unsupported operating system: {self.system}")
                return False
            
            logger.debug(f"Closed application: {self.app_name}")
            return True
        except Exception as e:
            logger.error(f"Error closing application: {str(e)}")
            return False

    def focus(self) -> bool:
        """
        Bring application to front
        
        Returns:
            True if successful, False otherwise
        """
        try:
            if self.system == "Darwin":
                subprocess.run(["osascript", "-e", f'tell application "{self.app_name}" to activate'])
            elif self.system == "Windows":
                import win32gui
                import win32con
                hwnd = win32gui.FindWindow(None, self.app_name)
                if hwnd:
                    win32gui.SetForegroundWindow(hwnd)
                else:
                    logger.error(f"Window not found for: {self.app_name}")
                    return False
            else:
                logger.error(f"Unsupported operating system: {self.system}")
                return False
            
            logger.debug(f"Focused application: {self.app_name}")
            return True
        except Exception as e:
            logger.error(f"Error focusing application: {str(e)}")
            return False