from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint

# Setup chrome webdriver
browser = webdriver.Chrome()

# Open the 2048 website
browser.get('https://play2048.co/')

# Select the body element where the game is played
game = browser.find_element_by_tag_name('body')

# Generate random number between 0 and 3
i = randint(0, 3)

while True:
    # Send different keys to the game according to random number generated
    if i == 0:
        game.send_keys(Keys.UP)
    elif i == 1:
        game.send_keys(Keys.DOWN)
    elif i == 2:
        game.send_keys(Keys.LEFT)
    elif i == 3:
        game.send_keys(Keys.RIGHT)
    else:
        i = 0
        continue

    try:
        # If game ends, a new class "retry-button" is added.
        # Incase this class is found, restart game.
        restart = browser.find_element_by_class_name('retry-button')
        restart.click()
    except:
        i = randint(0, 3)
