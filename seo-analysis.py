from bs4 import BeautifulSoup
import pandas as pd
import requests

def main():

    url = input("Paste URL here: ")
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'html.parser')

    bad = []
    good = []
    keywords = []

    # title
    title = soup.find('title')
    if title:
        good.append(f"Title Exists: {title}")
    else:
        bad.append("No Title!")
    
    # meta
    meta_d = soup.find('meta', attrs={'name':'description'})['content']
    if meta_d:
        good.append(f"Meta Description Exists: {meta_d}")
    else:
        bad.append("No Meta Description!")

    # headings
    hs = ['h1', 'h2', 'h3']
    h_tags = []
    for h in soup.find_all(hs):
        good.append(f"{h.name}--->{h.text.strip()}")
        h_tags.append(h.name)

    if 'h1' not in h_tags:
        bad.append("No H1 found!")

    # image alt
    for i in soup.find_all('img', alt=''):
        bad.append(f"No Alt: {i}")
    
    for j in good:
        print(j)
    print('-----------')
    for k in bad:
        print(k)
    
    return

if __name__ == "__main__":
    main()
