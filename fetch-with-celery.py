from celery import Celery
import requests

# Create a Celery instance
app = Celery('fetch-with-celery', broker='redis://localhost:6379/0')

# A celery worker can run multiple processes parallely. We want to hit all our urls parallely and
# not sequentially.
# A celery task is just a function with decorator `app.task` applied to it.
@app.task
def fetch_url(url):
    resp = requests.get(url)
    print(resp.status_code)

# When we say `delay()`, the code is serialized and put in the message queue,
# which in our case is redis. Celery worker when running will read the serialized
# thing from queue, then deserialize it and then execute it.
def fetch_all(urls):
    for url in urls:
        fetch_url.delay(url)

        
if __name__ == "__main__":
    fetch_all(["http://google.com", "http://amazon.in", "https://facebook.com", "http://twitter.com"])

