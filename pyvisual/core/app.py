import platform
import subprocess
from typing import Optional

class App:
    def __init__(self, app_name: str):
        self.app_name = app_name
        self.system = platform.system()
        self.process: Optional[subprocess.Popen] = None

    def open(self, path: Optional[str] = None):
        """Open the application"""
        if self.system == "Darwin":  # macOS
            if path:
                cmd = ["open", path]
            else:
                cmd = ["open", "-a", self.app_name]
        elif self.system == "Windows":
            cmd = [self.app_name] if path is None else [path]
        
        self.process = subprocess.Popen(cmd)

    def close(self):
        """Close the application"""
        if self.process:
            self.process.terminate()
        else:
            if self.system == "Darwin":
                subprocess.run(["osascript", "-e", f'quit app "{self.app_name}"'])
            elif self.system == "Windows":
                subprocess.run(["taskkill", "/F", "/IM", f"{self.app_name}.exe"])

    def focus(self):
        """Bring application to front"""
        if self.system == "Darwin":
            subprocess.run(["osascript", "-e", f'tell application "{self.app_name}" to activate'])
        elif self.system == "Windows":
            import win32gui
            import win32con
            hwnd = win32gui.FindWindow(None, self.app_name)
            if hwnd:
                win32gui.SetForegroundWindow(hwnd)