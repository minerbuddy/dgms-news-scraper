import requests
from bs4 import BeautifulSoup
import json
import urllib3

# SSL Certificate errors ko ignore karne ke liye
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scrape_dgms():
    url = "https://www.dgms.gov.in/Home/News"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        print("Scraping shuru ho rahi hai...")
        response = requests.get(url, headers=headers, verify=False, timeout=20)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            news_list = []

            # Screenshot ke hisaab se news list item rows mein hoti hai
            # Hum saare 'tr' (table rows) ya 'li' check karenge jo list mein hain
            items = soup.find_all(['tr', 'li'])

            for item in items:
                link_tag = item.find('a', href=True)
                if link_tag:
                    title = item.get_text(separator=" ", strip=True)
                    # Title ko saaf karna (dates aur unwanted text hatana)
                    clean_title = title.split("size")[0].strip() # 'size' word se pehle ka text le lo
                    
                    href = link_tag['href']
                    full_url = href if href.startswith('http') else f"https://www.dgms.gov.in{href}"

                    if clean_title and ".pdf" in full_url.lower():
                        news_list.append({
                            "title": clean_title,
                            "link": full_url
                        })

            if news_list:
                # Duplicates hatane ke liye
                seen = set()
                final_news = []
                for n in news_list:
                    if n['title'] not in seen:
                        final_news.append(n)
                        seen.add(n['title'])

                with open('news.json', 'w', encoding='utf-8') as f:
                    json.dump(final_news, f, indent=4, ensure_ascii=False)
                print(f"Bhai, {len(final_news)} news items mil gayi hain!")
            else:
                print("Yaar, list khali reh gayi. Tags check karne padenge.")
        else:
            print(f"Error: Status code {response.status_code}")

    except Exception as e:
        print(f"Galti ho gayi: {e}")

if __name__ == "__main__":
    scrape_dgms()