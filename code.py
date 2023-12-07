import requests
from bs4 import BeautifulSoup
import json

def scrape_ebay_product(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        title_tag = soup.find('h1', {'class': 'x-item-title__mainTitle'})
        title = title_tag.text.strip() if title_tag else None

        description_tag = soup.find('div', {'class': 'vim d-vi-region x-atf-center-river--bottom'})
        description = description_tag.text.strip() if description_tag else None

        price_tag = soup.find('div', {'class': 'x-price-primary'})
        price = price_tag.text.strip() if price_tag else None

        product_info = {
            'title': title,
            'description': description,
            'price': price,
            'url': url
        }

        return product_info

    else:
        print(f"Failed to fetch data from {url}. Status Code: {response.status_code}")
        return None


def main():
    with open('input.txt', 'r') as file:
        urls = file.read().splitlines()

    scraped_data = []

    for url in urls:
        product_info = scrape_ebay_product(url)
        if product_info:
            scraped_data.append(product_info)

    with open('output.json', 'w') as json_file:
        json.dump(scraped_data, json_file, indent=2)

if __name__ == "__main__":
    main()
