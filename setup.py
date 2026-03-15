from setuptools import setup, find_packages

setup(
    name="computer_vision_architectures",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "opencv-python",
        "torch",
        "torchvision",
    ],
    author="Krishna Pandey",
    description="Enterprise-grade Computer Vision Architectures",
)