import time
import ploting_data as pld

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Firefox(
    executable_path=r'C:\Users\nanda\AppData\Local\Programs\Python\Python38\get_firefox_driver\geckodriver.exe')


def writing_down(price_text, website):
    price_list = list(filter(str.isdigit, price_text))
    price = ""
    price = price.join(price_list)
    insert = [str(time.localtime().tm_mday), str(time.localtime().tm_mon), str(time.localtime().tm_year)]
    final_format = "/"
    final_format = final_format.join(insert) + f" {price}" + f" {website}"

    note = open("preços.txt", "a")
    note.write(final_format + "\n")
    note.close()


def scraping():
    links = ['https://www.viajanet.com.br/busca/passagens/voos#/FLN/LAX/RT/25-03-2021/02-04-2021/-/-/-/1/0/0/-/-/-/-',
             'https://www.kayak.com.br/flights/FLN-LAX/2021-03-25/2021-04-02?sort=price_a']
    websites = ["viajanet", "kayak"]
    contents_box = ["content-price-recommendation__wrap",
                    "Common-Booking-MultiBookProvider layover-connection featured-provider multi-row Theme-featured-large"]
    tags = ["div", "div"]
    prices_labels = ["content-price-recommendation__price--mobile ng-binding", "price-text"]

    for x in range(len(links)):
        driver.get(links[x])
        time.sleep(20)

        try:
            driver.find_element_by_css_selector("#DkjA-covid-loading-dialog-close").click()
        except:
            pass

        source_html = driver.page_source
        soup = BeautifulSoup(source_html, "lxml")

        content_box = soup.find(tags[x], class_=contents_box[x])
        price = content_box.find("span", class_=prices_labels[x]).text
        writing_down(price, websites[x])


if __name__ == "__main__":
    scraping()
    driver.quit()
    pld.ploting_results()
