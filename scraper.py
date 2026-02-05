import requests
from bs4 import BeautifulSoup
import json
import urllib3

# SSL warnings ko ignore karne ke liye
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scrape_dgms():
    url = "https://www.dgms.gov.in/Home/News"
    base_url = "https://www.dgms.gov.in"
    
    try:
        # User-Agent dalna zaroori hai taaki site ko lage browser se request aa rahi hai
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, verify=False, headers=headers, timeout=20)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        news_data = []
        table = soup.find('table') 
        
        if table:
            rows = table.find_all('tr')
            # Pehla row (header) chhod kar baaki 10 rows
            for row in rows[1:11]: 
                cols = row.find_all('td')
                if len(cols) >= 2:
                    date = cols[0].text.strip()
                    title_elem = cols[1]
                    title_text = title_elem.text.strip()
                    
                    # Link check aur Fix
                    link_tag = title_elem.find('a')
                    link = "#"
                    if link_tag and link_tag.get('href'):
                        link = link_tag.get('href')
                        # Agar link relative hai toh base_url jodo
                        if link.startswith('/'):
                            link = base_url + link
                    
                    news_data.append({
                        "date": date,
                        "title": title_text,
                        "link": link
                    })
        
        with open('news.json', 'w', encoding='utf-8') as f:
            json.dump(news_data, f, indent=4, ensure_ascii=False)
        print("Successfully updated news.json")

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    scrape_dgms()