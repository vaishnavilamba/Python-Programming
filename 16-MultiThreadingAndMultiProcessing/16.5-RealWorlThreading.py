import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://www.geeksforgeeks.org/python/introduction-to-python/',
    'https://www.geeksforgeeks.org/python/input-and-output-in-python/',
    'https://www.geeksforgeeks.org/python/python-variables/'
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f"Fetched {len(soup.text)} characters from {url}")

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched")
        