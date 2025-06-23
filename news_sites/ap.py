from bs4 import BeautifulSoup
from get_html import *
LINK = 'https://apnews.com/us-news'
FINANCIAL_LINK = 'https://apnews.com/hub/financial-markets'
source = 'ap'
financial_source = 'financial_ap'

def main_ap():
    get_site_html(LINK, source)
    get_site_html(FINANCIAL_LINK, financial_source)
    #get_article_names(source)


def get_article_names(source):
    with open('html_files/{}.html'.format(source), 'r') as file:
        # 'PagePromo'
        soup = BeautifulSoup(file, 'html.parser')
        #print(soup.get_text)

        page_promos = soup.find_all('div', class_='PagePromo')
        headlines = []
        for page in page_promos:
            #print("News Title: ", page['data-gtm-region'])
            headlines.append(page['data-gtm-region'])

        return headlines






