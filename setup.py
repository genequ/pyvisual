from setuptools import setup, find_packages

setup(
    name="pyvisual",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyautogui>=0.9.53",
        "opencv-python>=4.5.0",
        "pywin32>=228;platform_system=='Windows'",
    ],
    author="geneq",
    author_email="qushuqin@gmail.com",
    description="A Sikuli-like automation package for Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/geneq/pyvisual",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)