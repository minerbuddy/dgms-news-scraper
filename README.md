# 🚀 DGMS News Scraper & Dashboard

An automated news tracking system designed for mining students and professionals. This tool scrapes the official DGMS (Directorate General of Mines Safety) website to deliver the latest announcements in real-time.

<p align="left">
  <a href="https://www.buymeacoffee.com/k.vinitkarmkar">
    <img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me A Coffee">
  </a>
</p>

## ✨ Features
- **Auto-Scraping:** Powered by GitHub Actions to fetch data from the DGMS site daily.
- **JSON API:** Scraped data is structured and stored in `news.json`, making it easy to integrate into any application.
- **Live Dashboard:** Displays real-time updates through the DGMS Buddy web interface.

## 🛠️ Tech Stack
- **Language:** Python (BeautifulSoup)
- **Automation:** GitHub Actions (CI/CD)
- **Frontend:** HTML5, CSS3, JavaScript (Fetch API)

## 📡 API Usage
To integrate this live data into your own project, use the following endpoint:
`https://raw.githubusercontent.com/minerbuddy/dgms-news-scraper/main/news.json`

### 💡 JavaScript Integration (Bypass Caching)
To ensure your application always displays the most recent data and avoids browser caching, use the following implementation:

```javascript
const NEWS_URL = '[https://raw.githubusercontent.com/minerbuddy/dgms-news-scraper/main/news.json?v=](https://raw.githubusercontent.com/minerbuddy/dgms-news-scraper/main/news.json?v=)' + new Date().getTime();

### Developed with ❤️ by **[K Vinit Karmkar]**(https://kvinitkarmkar.github.io/Website/)
