from bs4 import BeautifulSoup
from get_html import *
LINK = 'https://apnews.com/us-news'
source = 'ap'

def main_ap():
    #get_site_html(LINK, source)
    get_article_names(source)


def get_article_names(source):
    with open('html_files/{}.html'.format(source), 'r') as file:
        # 'PagePromo'
        soup = BeautifulSoup(file, 'html.parser')
        #print(soup.get_text)

        page_promos = soup.find_all('div', class_='PagePromo')
        for page in page_promos:
            print("News Title: ", page['data-gtm-region'])




