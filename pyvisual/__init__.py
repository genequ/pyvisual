"""
This module provides convenience functions for screen and keyboard operations.
"""

from .core.screen import Screen
from .core.keyboard import Keyboard
from .core.app import App

# Convenience functions
find = Screen.find
wait = Screen.wait
click = Screen.click
type = Keyboard.type
