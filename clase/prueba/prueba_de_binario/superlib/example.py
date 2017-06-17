import requests
import os


def get_google():
    return requests.get('https://google.com')

def open_hello():
    os.system('ls -hal /tmp')
    return open('superlib/hello.txt', 'rb').read()

