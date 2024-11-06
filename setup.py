from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyvisual",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyautogui>=0.9.53",
        "opencv-python>=4.5.0",
        "Pillow>=8.0.0",
        "mouse>=0.7.1",
        "pywin32>=228;platform_system=='Windows'",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A Sikuli-like automation package for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/genequ/pyvisual",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Topic :: Desktop Environment",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
    ],
    python_requires=">=3.6",
)