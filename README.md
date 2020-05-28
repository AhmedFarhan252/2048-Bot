# 2048-Bot

## A Python bot that plays the 2048 game itself

---

## Usage

This program will open the 2048 game link and will automatically start playing the game. It will send random inputs of "UP", "DOWN", "LEFT", "RIGHT" continuously and will also restart the game after one has ended.

---

## Used modules

1. [Selenium](https://selenium-python.readthedocs.io/)
2. [randint from Random](https://docs.python.org/3/library/random.html)

## Setup / Changing browsers

1. Install the required libraries.
2. Download and setup the web drivers according to the instructions [here](https://selenium-python.readthedocs.io/installation.html#drivers).
3. If a webdriver other than Chrome is installed, update line 6 in `2048bot.py` accordingly.
4. Execute the `2048bot.py` file.

## Reference

This idea was obtained from the book [Automating the boring stuff with Python](https://automatetheboringstuff.com/2e/chapter12/) by Al Sweigart.
