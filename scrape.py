#scraping companies from Angel.co
from selenium import webdriver
from bs4 import BeautifulSoup
import time

def scrape(url,clickMoreTimes):
    """

    :param url:
    :return:
    """

    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(5) #wait 5 sec for website to response
    for i in range(clickMoreTimes):
        clickMore = browser.find_element_by_class_name("more")
        clickMore.click()
        time.sleep(5) #wait 5 sec for website to response
    html = browser.page_source
    return html

def results(html):
    """

    :param html:
    :return:
    """
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all("div",{"class","base startup"})
    return results