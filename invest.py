import os
import anthropic
from news_sites.ap import get_article_names


# antrophic key =

def grade_headlines(site, check=False, keyword=''):
    headlines = get_article_names(site)

    for headline in headlines:
        # print(headline)
        lc_headline = headline.lower()

        # print(lc_headline)
        if not check:
            ask_claude(headline)
        else:
            if keyword in lc_headline:
               ask_claude(headline)




def ask_claude(headline):

    model = os.environ.get('CLAUDE_MODEL')
    key = os.environ.get('CLAUDE_API_KEY')

    client = anthropic.Anthropic(api_key=key)

    print(headline)

    message = client.messages.create(
        model=model,
        max_tokens=500,
        temperature=0.1,
        system="You are a stock broker for a Wall Street Firm. Determine if the following headline is likely "
               "to cause the stock market to increase, decrease or stay the same. Answer in one word ("
               "increase, decrease, same). The headline is \'{0}\'".format(headline),
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Is the stock market expected to go up, down, or stay the same based on the headline?"
                    }
                ]

            }
        ]
    )

    print(message.content[0].text)