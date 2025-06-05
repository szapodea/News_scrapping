from urllib.request import Request, urlopen
from urllib import request
import certifi
import ssl

# This restores the same behavior as before.


# Paramaters:
#           url: the url to the website we want to scrap
#           output_file_name: the name of the output html file in html_files
def get_site_html(url, output_file_name):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    req = Request(
        url=url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    html_data = urlopen(req, context=ssl_context).read()
    html_string = html_data.decode('utf-8')

    with open('html_files/{0}.html'.format(output_file_name), "w") as file:
        file.write(html_string)



