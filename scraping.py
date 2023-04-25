import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {
    "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"}


def b_soup(url):
    soup = BeautifulSoup(url.text, "lxml")
    return soup


def download(url):
    r = requests.get(url, stream=True, headers=headers)
    r_o = open("D:\\Python\\Python (обучение)\\pars\\img_pars\\" +
               url.split('/')[-1], 'wb')
    for value in r.iter_content(1024*1024):
        r_o.write(value)
    r_o.close()


def get_url():
    for number in range(1, 8):
        url = f"https://scrapingclub.com/exercise/list_basic/?page={number}"
        response = requests.get(url, headers=headers)
        # soup = BeautifulSoup(response.text, "lxml")
        data = b_soup(response).find_all(
            'div', class_="col-lg-4 col-md-6 mb-4")
        for i in data:
            card_url = "https://scrapingclub.com" + i.find('a').get('href')
            yield card_url


def array():
    for link in get_url():
        response = requests.get(link, headers=headers)
        # soup = BeautifulSoup(response.text, "lxml")
        sleep(3)
        data = b_soup(response).find('div', class_="card mt-4 my-4")
        name = data.find('h3', class_="card-title").text
        price = data.find('h4').text
        img_url = "https://scrapingclub.com" + \
            data.find('img', class_="card-img-top img-fluid").get('src')
        text_card = data.find('p').text
        download(img_url)
        yield name, price, text_card, img_url
        # print(name, '\n', price, '\n', img_url, '\n', text_card, '\n\n')
