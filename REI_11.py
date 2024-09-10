import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL for size 11 used shoes at REI
url = 'https://www.rei.com/used/shop/all?size=11&department=Men%27s%20Footwear'

# Mimic a browser request with headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Fetch the page
response = requests.get(url, headers=headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract information based on tags and classes
    shoes = []
    for item in soup.find_all('div', class_='your-shoe-class'):
        title = item.find('h2').text.strip()
        price = item.find('span', class_='your-price-class').text.strip()
        size = item.find('span', class_='your-size-class').text.strip()

        if 'Size 11' in size:
            shoes.append({'Title': title, 'Price': price, 'Size': size})

    # Store the data in a pandas DataFrame
    df = pd.DataFrame(shoes)
    df.to_csv('rei_used_size11_shoes.csv', index=False)

    print("Scraping complete! Data saved to rei_used_size11_shoes.csv")
else:
    print(f"Failed to retrieve page: {response.status_code}")
