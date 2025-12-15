# Quick Start Guide

Get your World News Aggregator up and running in minutes!

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

Load sample categories and news sources:

```bash
python manage.py loaddata news/fixtures/initial_data.json
```

This will create:
- 5 categories (World News, Technology, Business, Politics, Science)
- 6 news sources (BBC, Al Jazeera, TechCrunch, Ars Technica, Reuters, Science Daily)

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

### Popular RSS Feeds to Add

**World News:**
- BBC World: http://feeds.bbci.co.uk/news/world/rss.xml
- CNN World: http://rss.cnn.com/rss/edition_world.rss
- The Guardian: https://www.theguardian.com/world/rss
- NPR News: https://feeds.npr.org/1001/rss.xml

**Technology:**
- TechCrunch: https://techcrunch.com/feed/
- The Verge: https://www.theverge.com/rss/index.xml
- Ars Technica: https://feeds.arstechnica.com/arstechnica/index
- Hacker News: https://hnrss.org/frontpage

**Science:**
- Science Daily: https://www.sciencedaily.com/rss/all.xml
- NASA: https://www.nasa.gov/rss/dyn/breaking_news.rss
- Nature News: http://feeds.nature.com/nature/rss/current

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
