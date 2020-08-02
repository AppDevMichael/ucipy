import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ucipy", # Replace with your own username
    version="0.0.1",
    author="Michael O'Connell",
    author_email="michael.dev012@gmail.com",
    description="For parsing OpenWRT UCI configs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AppDevMichael/ucipy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)