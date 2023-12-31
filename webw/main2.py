import time
import requests
import os
from bs4 import BeautifulSoup
import hashlib

SLEEPING_TIME = 2.5
URL_TO_MONITOR = (
    "https://outpostclimbing.sg/"  # change this to the URL you want to monitor
)


def process_html(string):
    soup = BeautifulSoup(string, features="lxml")

    # make the html look good
    soup.prettify()

    # remove script tags
    for s in soup.select("script"):
        s.extract()

    # remove meta tags
    for s in soup.select("meta"):
        s.extract()

    # convert to a string, remove '\r', and return
    results = str(soup).replace("\r", "")

    h = hashlib.new("sha256")
    h.update(results.encode("utf-8"))
    hashcode = h.hexdigest()

    return hashcode


def webpage_was_changed():
    """Returns true if the webpage was changed, otherwise false."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
    }
    response = requests.get(URL_TO_MONITOR, headers=headers)
    hashcode = process_html(response.text)
    print(f"{hashcode=}")

    # # create the previous_content.txt if it doesn't exist
    # if not os.path.exists("previous_content.txt"):
    #     open("previous_content.txt", "w+").close()

    # filehandle = open("previous_content.txt", "r")
    # previous_response_html = filehandle.read()
    # filehandle.close()

    # processed_response_html = process_html(response.text)

    # if processed_response_html == previous_response_html:
    #     return False
    # else:
    #     filehandle = open("previous_content.txt", "w")
    #     filehandle.write(processed_response_html)
    #     filehandle.close()
    #     return True


if __name__ == "__main__":
    while True:
        webpage_was_changed()
        time.sleep(SLEEPING_TIME)
