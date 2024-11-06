# PyVisual

A Sikuli-like automation package for Python that works on both Windows and macOS.

## Features

- Image recognition and interaction (`find()`, `wait()`, `click()`)
- Keyboard automation (`type()`, `hotkey()`, `press()`)
- Application management (`open()`, `close()`, `focus()`)
- Cross-platform support (Windows and macOS)

## Installation
bash
pip install git+https://github.com/genequ/pyvisual.git

## Usage
python
from pyvisual import find, wait, click, type, App
Open an application
app = App("notepad")
app.open()
Wait for a specific image to appear and type
if wait("notepad_window.png", timeout=5):
type("Hello, World!")
Find and click on elements
if find("save_button.png"):
click("save_button.png")
Close the application
app.close()

## Requirements

- Python 3.6+
- pyautogui
- opencv-python
- pywin32 (Windows only)

## License

MIT License