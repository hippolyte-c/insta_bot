
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random_words import RandomWords
import re
import time
import argparse

driver = webdriver.Firefox()
driver.get("https://www.instagram.com/")

driver.implicitly_wait(15)


def login():
    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("povimo6760@lywenw.com")
    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("*1HhdDzh%A" + Keys.ENTER)


def getAccess():                   # "activer les notifications"
    driver.implicitly_wait(5)
    driver.find_element_by_class_name("cmbtv").click()
    driver.implicitly_wait(5)
    driver.find_element_by_class_name("mt3GC").click()


def goToTag(tag):
    print(tag)
    driver.get("https://www.instagram.com/explore/tags/" + tag)


def goToPhoto():
    driver.implicitly_wait(5)

    photos = []

    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        if(re.search("https://www.instagram.com/p/", elem.get_attribute("href"))):
            photos.append(elem.get_attribute("href"))

    for photo in photos:
        driver.get(photo)
        time.sleep(5)

        if(len(driver.find_element_by_tag_name('svg').get_attribute("aria-label")) == len("J'aime")):
            print("j'aime")
            driver.find_element_by_class_name("_8-yf5 ").click()   #click sur j'aime
        time.sleep(10)

    rw = RandomWords()
    goToTag(rw.random_word())
    goToPhoto()



if __name__ == '__main__':
    rw = RandomWords()
    parser = argparse.ArgumentParser(description='Ajoutez un tag')
    parser.add_argument('--tag', type=str, default=rw.random_word())
    args = parser.parse_args()
    login()
    getAccess()
    goToTag(args.tag)
    goToPhoto()
