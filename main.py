'''
This project will be a web scrapping tool initially scrapping the headlines of news sites.
Once the headlines are gotten, they will be passed into a LLM model with carefully crafted prompts
to determine characteristics about that article.

The vague use case that inspired this project is given an article that mentions tariffs and Donald Trump,
can a LLM determine if that article would be good or bad for stock market short-term?
'''
from news_sites.reuters import main_reuters
from news_sites.ap import main_ap
from invest import grade_headlines

if __name__ == '__main__':
    #main_reuters()
    #main_ap()
    main_ap()
    grade_headlines('ap', trump=True)
    grade_headlines('financial_ap')