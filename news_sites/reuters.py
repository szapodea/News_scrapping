from bs4 import BeautifulSoup
from get_html import *
LINK = 'https://www.reuters.com/world/us/'


def main_reuters():
    get_site_html(LINK, 'reuters')
