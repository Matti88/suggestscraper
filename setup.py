from codecs import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read() 

setup(
    name="suggestscraper",
    version="0.0.2",
    description="Yet another way to Web Scrape with Python, just a couple of suggestions!",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/Matti88/suggestscraper",
    author="Matteo Montanari",
    author_email="matteo.montanari25@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    keywords="scraping - scraper",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    python_requires=">=3.6",
    install_requires=[ "re", "lxml", "pandas" , "bs4", "json"],
)