import requests
import time

def fetch_all(urls):
    start = time.time()
    for url in urls:
        resp = requests.get(url)
        print(resp.status_code)
    print("It took {} seconds".format(
        time.time() - start))

if __name__ == "__main__":
    fetch_all(["http://google.com", "http://amazon.in", "https://facebook.com", "http://twitter.com"])
