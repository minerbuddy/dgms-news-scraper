import requests
from bs4 import BeautifulSoup
import json
import urllib3

# SSL warning hide karne ke liye
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scrape_dgms_news():
    url = "https://www.dgms.gov.in/writereaddata/LatestNews.html"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        # verify=False zaroori hai DGMS ke liye
        response = requests.get(url, headers=headers, verify=False, timeout=20)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            news_data = []

            # DGMS website par news aksar <a> tags mein hoti hai jo <li> ke andar hote hain
            # Ek baar tags check kar lena, main general scrap likh raha hoon:
            links = soup.find_all('a')
            
            for link in links:
                title = link.get_text(strip=True)
                href = link.get('href')
                
                # Filter: Sirf news wali links uthao (jo .pdf ho ya LatestNews se judi ho)
                if href and ('.pdf' in href.lower() or 'latestnews' in href.lower()):
                    # Full URL banana agar relative path ho
                    full_url = href if href.startswith('http') else f"https://www.dgms.gov.in/{href}"
                    news_data.append({
                        "title": title,
                        "link": full_url
                    })

            # Sirf tabhi write karein jab data mile
            if news_data:
                with open('news.json', 'w', encoding='utf-8') as f:
                    json.dump(news_data, f, indent=4, ensure_ascii=False)
                print(f"Success! {len(news_data)} news items found.")
            else:
                print("Website se data fetch nahi ho paya (List empty hai).")
        else:
            print(f"Failed to connect. Status code: {response.status_code}")

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    scrape_dgms_news()