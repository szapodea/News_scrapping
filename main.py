'''
This project will be a web scrapping tool initially scrapping the headlines of news sites.
Once the headlines are gotten, they will be passed into a LLM model with carefully crafted prompts
to determine characteristics about that article.

'''
from news_sites.reuters import main_reuters
from news_sites.ap import main_ap
from invest import grade_headlines
import os
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    #main_reuters()
    #main_ap()
    main_ap()
    grade_headlines('financial_ap')