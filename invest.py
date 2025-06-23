import anthropic
from news_sites.ap import get_article_names


def grade_headlines(site, trump=False):
    client = anthropic.Anthropic()

    headlines = get_article_names(site)

    for headline in headlines:
        #print(headline)
        lc_headline = headline.lower()

        #print(lc_headline)
        if trump:
            if 'trump' in lc_headline:
                print(headline)
        else:
            print(headline)


           # message = client.messages.create(
           #     model="claude-sonnet-4-20250514",
           #     max_tokens=10000,
           #     temperature=0.1,
           #     system="You are a stock broker for a Wall Street Firm. Determine if the following headline is likely to cause the stock market to increase, decrease or stay the same. Answer in one word (increase, decrease, same). The following is the headline: {{headline}}",
           #    messages=[]
           # )
           # print(message.content)

