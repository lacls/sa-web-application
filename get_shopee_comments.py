from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv
import urllib
from selenium.webdriver.common.action_chains import ActionChains
import requests
import json
import re
import urllib.request
import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException,StaleElementReferenceException,InvalidArgumentException,ElementClickInterceptedException,WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pickle5 as pickle
from tqdm import tqdm

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600')
driver = webdriver.Chrome(options=options)


def get_shopee_comments_in_pickle_file(link):
    driver.get(link)
    comments={}
    sleep(1)
    try:
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, 'shop-page__all-products-section')))
    except TimeoutError:
        print("blalb")
    products_url=[]
    i=0
    for _ in range(1):
        if i==5:
            break
        for products in driver.find_element_by_class_name('shop-page__all-products-section').find_element_by_class_name("row").find_elements_by_tag_name("a"):
            products_url.append(products.get_attribute("href"))
        ##click to the next page
        for _ in range(5):
            try:
                driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/div[3]").find_elements_by_tag_name("button")[-1].click()
                i=0
                break
            except:
                i+=1
                continue
    for url in tqdm(products_url,total=len(products_url)):
        if len(comments)==500:
            break
        driver.get(url)
        driver.find_element_by_tag_name("body").send_keys(Keys.END)
        i=0
        for _ in tqdm(range(15)):
            if i==2:
                break
            driver.find_element_by_tag_name("body").send_keys(Keys.END)
            sleep(1)         
            for element in driver.find_elements_by_class_name("shopee-product-rating__main"):
                if element.find_element_by_class_name("shopee-product-rating__content").text:
                    comments[element.find_element_by_class_name("shopee-product-rating__time").text]=element.find_element_by_class_name("shopee-product-rating__content").text
            for _ in range(10):
                try:
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[3]/div[2]").find_elements_by_tag_name("button")[-1].click()
                    i=0
                    break
                except:
                    print("cannot click on")
                    if i==2:
                        break
                    i+=1
                    continue
    file_name=link.split("/")[-1]
    pickle.dump(comments,open(f"shopee_crawling_comments/{file_name}.pickle","wb"))

    