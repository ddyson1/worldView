# Quick Start Guide

Get your Financial News Aggregator up and running in minutes!

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Setup (5 minutes)

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Database Setup

The migrations have already been run, but if you need to reset:

```bash
python manage.py migrate
```

### 3. Load Sample Data

Load sample categories and financial news sources:

```bash
python manage.py loaddata news/fixtures/initial_data.json
```

This will create:
- 5 categories (Finance, Business, Markets, Economics, World News)
- 5 premium news sources (Yahoo Finance, Wall Street Journal, New York Times, Financial Times, The Economist)

### 4. Create Admin User

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### 5. Fetch Some News!

```bash
python manage.py fetch_news
```

This will fetch the latest articles from all active news sources. The first fetch might take a minute or two.

### 6. Start the Server

```bash
python manage.py runserver
```

### 7. Visit the App

Open your browser and go to:
- **Main site**: http://localhost:8000/
- **Admin panel**: http://localhost:8000/admin/

## Next Steps

### Add More News Sources

1. Go to http://localhost:8000/admin/
2. Click "News Sources" → "Add News Source"
3. Fill in the RSS/Atom feed URL and other details
4. Run `python manage.py fetch_news` to fetch from the new source

### Pre-configured Sources

The app comes with these premium financial news sources:

1. **Yahoo Finance** - Stock market and financial analysis
2. **Wall Street Journal** - Business and financial news
3. **New York Times Business** - Business and economy coverage
4. **Financial Times** - Global business and financial news
5. **The Economist** - Global economics and business

### Additional Financial RSS Feeds to Add

**More Financial News:**
- Bloomberg: https://www.bloomberg.com/feeds/podcasts/etf_report.xml
- Reuters Business: https://www.reutersagency.com/feed/?taxonomy=best-topics&post_type=best
- CNBC: https://www.cnbc.com/id/100003114/device/rss/rss.html
- MarketWatch: http://feeds.marketwatch.com/marketwatch/topstories/

**Business & Tech:**
- Forbes: https://www.forbes.com/real-time/feed2/
- Business Insider: https://www.businessinsider.com/rss

### Automate News Fetching

**Option 1: Cron Job (Linux/Mac)**
```bash
# Run every hour
0 * * * * cd /path/to/worldView && python manage.py fetch_news
```

**Option 2: Windows Task Scheduler**
- Create a batch file that runs `python manage.py fetch_news`
- Schedule it to run at your desired interval

**Option 3: Django Background Task**
Consider using django-crontab or celery for production deployments.

## Troubleshooting

**No articles showing up?**
- Make sure you've run `python manage.py fetch_news`
- Check the admin panel to ensure sources are marked as "Active"
- Check the RSS URL is correct and accessible

**Fetch command fails?**
- Verify you have internet connection
- Some RSS feeds may be temporarily unavailable
- Try fetching from a specific source: `python manage.py fetch_news --source "BBC"`

**Categories not working?**
- Make sure you've loaded the fixtures: `python manage.py loaddata news/fixtures/initial_data.json`
- Or create categories manually in the admin panel

## Tips

1. **Start small**: Begin with 3-5 news sources, then expand
2. **Check fetch intervals**: Major news sites update frequently (30 min), blogs less so (2-4 hours)
3. **Monitor database size**: Consider archiving old articles periodically
4. **Customize**: Edit templates in `news/templates/news/` to customize the look

Enjoy your personalized news aggregator!
