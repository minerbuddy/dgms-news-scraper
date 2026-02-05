import requests
from bs4 import BeautifulSoup
import json
import urllib3

# SSL Warnings ko silent karne ke liye
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scrape_dgms_news():
    # Aapka naya wala sahi link
    url = "https://www.dgms.gov.in/Home/News"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        # verify=False is important for government sites
        response = requests.get(url, headers=headers, verify=False, timeout=20)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            news_data = []

            # DGMS ki table mein news dhoondna
            # Hum saare rows (tr) dhoond rahe hain jinme data ho sakta hai
            rows = soup.find_all('tr')
            
            for row in rows:
                cols = row.find_all('td')
                if len(cols) >= 2:  # Kam se kam 2 columns hone chahiye
                    link_tag = row.find('a')
                    if link_tag:
                        title = link_tag.get_text(strip=True)
                        href = link_tag.get('href')
                        
                        # Full URL handle karna
                        full_url = href if href.startswith('http') else f"https://www.dgms.gov.in{href}"
                        
                        if title and href:
                            news_data.append({
                                "title": title,
                                "link": full_url
                            })

            # Data check aur write
            if news_data:
                # Sirf unique news rakhne ke liye (duplicates hatane ke liye)
                unique_news = [dict(t) for t in {tuple(d.items()) for d in news_data}]
                
                with open('news.json', 'w', encoding='utf-8') as f:
                    json.dump(unique_news, f, indent=4, ensure_ascii=False)
                print(f"Bhai, kaam ho gaya! {len(unique_news)} news items mil gayi.")
            else:
                print("Yaar, table toh mili par news nahi nikal payi. Tags check karne padenge.")
        else:
            print(f"Connection fail! Code: {response.status_code}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    scrape_dgms_news()