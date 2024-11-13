import requests
from bs4 import BeautifulSoup as bs

def scrapeAmazon(item):
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }
    baseURL = "https://www.amazon.in/s?k="
    url = baseURL + item
    response = requests.get(url, headers=headers)
    soup = bs(response.text, 'lxml')
    items = soup.findAll('div', class_="s-result-item", limit=15 )
    
    results = []
    for item in items[4:]:
        try:
            # LINK
            link_tag = item.find('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
            if not link_tag or 'href' not in link_tag.attrs:
                continue  
            link = "https://www.amazon.in/" + link_tag['href']
            
            # TITLE
            title = item.find('span', class_='a-size-base-plus a-color-base a-text-normal') or item.find('span', class_='a-size-medium a-color-base a-text-normal')
            if not title:
                continue  
            title_text = title.get_text()

            # IMAGE
            img_tag = item.find('img', class_='s-image')
            if not img_tag or 'src' not in img_tag.attrs:
                continue  
            img_src = img_tag['src']

            # PRICE
            price_tag = item.find('span', class_='a-price-whole')
            if not price_tag:
                continue  
            price = '₹' + price_tag.text

            results.append({"title": title_text, "price": price, "img": img_src, "link": link})

        except Exception as e:
            print(f"Error encountered in Amazon scraper: {e}")
            continue 

    return results

def scrapeFlipkart(item):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.google.com/",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }
    baseURL = "https://www.flipkart.com/search?q="
    url = baseURL + item
    response = requests.get(url, headers=headers)
    soup = bs(response.text, 'lxml')
    results = []

    items = soup.find_all('div', class_='slAVV4', limit=12)
    if not items:
        items = soup.find_all('div', class_='LFEi7Z', limit=12)
    
    if items:
        for item in items[2:]:
            try:
                title_link = item.find('a', class_='wjcEIp')
                if not title_link:
                    title_link = item.find('a', class_='WKTcLC')
                if not title_link or 'href' not in title_link.attrs:
                    continue  
                title = title_link.text
                link = "https://www.flipkart.com" + title_link['href']

                price_tag = item.find('div', class_='Nx9bqj')
                if not price_tag:
                    continue 
                price = price_tag.text

                img_tag = item.find('img', class_='DByuf4')
                if not img_tag:
                    img_tag = item.find('img', class_='_53J4C-')
                if not img_tag or 'src' not in img_tag.attrs:
                    continue  
                img_src = img_tag['src']
                
                results.append({"title": title, "price": price, "img": img_src, "link": link})

            except Exception as e:
                print(f"Error encountered in Flipkart scraper: {e}")
                continue  
    else:
        items = soup.find_all('div', class_='tUxRFH', limit=12)
        for item in items[2:]:
            try:
                title_div = item.find('div', class_='KzDlHZ')
                if not title_div:
                    continue  
                title = title_div.text

                link_tag = item.find('a', class_='CGtC98')
                if not link_tag or 'href' not in link_tag.attrs:
                    continue  
                link = baseURL + link_tag['href']

                price_tag = item.find('div', class_='Nx9bqj')
                if not price_tag:
                    continue  
                price = price_tag.text

                img_tag = item.find('img', class_='DByuf4')
                if not img_tag or 'src' not in img_tag.attrs:
                    continue  
                img_src = img_tag['src']
                
                results.append({"title": title, "price": price, "img": img_src, "link": link})

            except Exception as e:
                print(f"Error encountered in Flipkart scraper: {e}")
                continue 

    return results

# print(scrapeFlipkart('samsungCharger'))
