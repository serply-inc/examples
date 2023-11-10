import time
import urllib
import requests

import grequests

# set the api key in headers
headers = {"apikey": "YOUR_API_KEY"}


# build 5 urls
def build_urls():
    query = {"q": "intel", "hl": "en", "start": 0}
    urls = []
    for x in range(5):
        query["start"] = x * 10  # step the search results by 10
        urls.append("https://api.serply.io/v1/search/" + urllib.parse.urlencode(query))

    return urls


def single_treaded():
    for url in build_urls():
        resp = requests.get(url, headers=headers)


def exception_handler(request, exception):
    print("Request failed: ".format(exception))


def async_threaded():
    rs = (grequests.get(u, headers=headers) for u in build_urls())
    grequests.map(rs, exception_handler=exception_handler)


def main():
    # print("Running Single Threaded")
    # start = time.time()
    # single_treaded()
    # print("Time for single thread: {}".format(time.time() - start))

    print("Running Async Threaded")
    start = time.time()
    async_threaded()
    print("Time for async thread: {}".format(time.time() - start))


if __name__ == "__main__":
    main()

    # example output
    """
    Running Single Threaded
    Time for single thread: 72.7473838329315
    Running Async Threaded
    Time for async thread: 39.56458115577698
    
    Backend logs
    [28/Sep/2020:23:41:49 +0000] "GET /v1/search/start=0&q=intel&hl=en HTTP/1.1" 200 1972 "-" "-"
    [28/Sep/2020:23:41:49 +0000] "GET /v1/search/start=10&q=intel&hl=en HTTP/1.1" 200 2802 "-" "-"
    [28/Sep/2020:23:41:49 +0000] "GET /v1/search/start=40&q=intel&hl=en HTTP/1.1" 200 2642 "-" "-"
    [28/Sep/2020:23:41:49 +0000] "GET /v1/search/start=20&q=intel&hl=en HTTP/1.1" 200 3019 "-" "-"
    [28/Sep/2020:23:41:49 +0000] "GET /v1/search/start=30&q=intel&hl=en HTTP/1.1" 200 2983 "-" "-"
    """
