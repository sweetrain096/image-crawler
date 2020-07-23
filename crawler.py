import os
from bs4 import BeautifulSoup
# 스크롤 기능
from selenium import webdriver
import urllib, urllib.request
import time



search_word = "식빵"
total_cnt = 100
url = "https://www.google.com/search?q="
url_source = "&source=lnms&tbm=isch"

Dir = "D:/rain/image-crawler/img/"

def search_image(word):
    # selenium으로 크롬 드라이버 열기
    driver = webdriver.Chrome('./chromedriver')
    # 모든 자원이 로드될 때까지 기다리는 시간을 임의 지정(안해도 됨)
    driver.implicitly_wait(1)
    driver.get(url+word+url_source)


    first_html = driver.page_source
    first_soup = BeautifulSoup(first_html, 'html.parser')
    # pprint.pprint(soup)
    imgs = first_soup.select("img.Q4LuWd")
    # print(imgs)
    img_cnt = len(imgs)
    # print(img_cnt)

    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    cnt = img_cnt
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

        if cnt > total_cnt * 3:
            break
        cnt += img_cnt

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.select("img.Q4LuWd")

    image_list = []
    for image in images:
        if image.get('data-src'):
            image_list.append(image.get('data-src'))

    print(len(image_list), image_list)
    save(image_list[:total_cnt])


def create_folder(save_dir):
    try:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
    except OSError:
        print("Error : Creating directory.")

def save(arr):
    save_dir = Dir+search_word
    create_folder(save_dir)

    for i, src in zip(range(len(arr)), arr):
        urllib.request.urlretrieve(src, save_dir + "/" + str(i) + ".jpg")
        # print(i, "saved")

search_image(search_word)
