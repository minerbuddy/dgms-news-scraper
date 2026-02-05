import requests
from bs4 import BeautifulSoup
import json

url = "https://www.dgms.gov.in/writereaddata/LatestNews.html" # DGMS News URL
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def scrape_news():
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        news_list = []
        
        # Yahan apna scraping logic check karein (Example)
        # Agar wo purane tags dhoond raha hai toh use update karein
        for item in soup.find_all('a'): # Example tag
            text = item.get_text(strip=True)
            if text:
                news_list.append({"title": text, "link": item.get('href')})
        
        if not news_list:
            print("Koi news nahi mili!")
            
        with open('news.json', 'w') as f:
            json.dump(news_list, f, indent=4)
            
    except Exception as e:
        print(f"Error: {e}")

scrape_news()