# 🚀 DGMS News Scraper & Dashboard

Mining students aur professionals ke liye ek automatic news tracking system jo DGMS ki official website se latest announcements nikalta hai.

<p align="left">
  <a href="https://www.buymeacoffee.com/k.vinitkarmkar">
    <img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me A Coffee">
  </a>
</p>

## ✨ Features
- **Auto-Scraping:** GitHub Actions har roz DGMS site se data fetch karta hai.
- **JSON API:** Scrap kiya gaya data `news.json` mein store hota hai, jise kisi bhi app mein use kiya ja sakta hai.
- **Live Dashboard:** DGMS Buddy dashboard par real-time updates dikhata hai.

## 🛠️ Tech Stack
- **Language:** Python (BeautifulSoup)
- **Automation:** GitHub Actions
- **Frontend:** HTML, CSS, JavaScript (Fetch API)

## 📡 Usage (API)
Agar aap is data ko apne project mein use karna chahte hain, toh is URL ko fetch karein:
`https://raw.githubusercontent.com/minerbuddy/dgms-news-scraper/main/news.json`

### 💡 JavaScript Integration (Avoid Caching)
Browser cache se bachne ke liye aur hamesha fresh data dikhane ke liye niche wala tarika use karein:
```javascript
const NEWS_URL = '[https://raw.githubusercontent.com/minerbuddy/dgms-news-scraper/main/news.json?v=](https://raw.githubusercontent.com/minerbuddy/dgms-news-scraper/main/news.json?v=)' + new Date().getTime();

Developed with ❤️ by K Vinit Karmkar
