# Getting Started with Celery and Redis
------------------

This repo is a demonstration of the use case for celery in python.

Agenda:
- when to use Celery
- Why to use Celery
- A simple celery program
- Having a slow script and making it faster using celery

To run the program without celery
```
python3 fetch-without-celery.py
```

Make sure you have redis installed and you are able to run redis-server

Make sure you have celery installed

Start three terminals
- On the first terminal, run redis using ```redis-server```
- On the second terminal, run celery worker using ```celery worker -A fetch-with-celery -l info -c 5```
- On the third, run your script, ```python3 fetch-with-celery.py```
