from bs4 import BeautifulSoup
from get_html import *
LINK = 'https://apnews.com/us-news'

def main_ap():
    get_site_html(LINK, 'ap')
