# Financial News Aggregator

A Django web application for monitoring and aggregating financial and business news from premium sources including Yahoo Finance, Wall Street Journal, New York Times, Financial Times, and The Economist into a single, unified interface.

## Features

- **Multi-source Financial News Aggregation**: Fetch articles from premium financial sources via RSS/Atom feeds
- **Categorization**: Organize news by categories (Finance, Business, Markets, Economics, World News)
- **Premium Sources**: Pre-configured with Yahoo Finance, WSJ, NYT, Financial Times, and The Economist
- **Search Functionality**: Full-text search across article titles, descriptions, and content
- **Source Management**: Easy management of news sources through Django admin
- **Responsive Design**: Clean, modern interface that works on all devices
- **Automated Fetching**: Management command to fetch news articles automatically
- **Pagination**: Efficient browsing of large numbers of articles

## Installation

1. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

2. **Run Migrations**:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. **Create Admin User**:
```bash
python manage.py createsuperuser
```

4. **Run the Development Server**:
```bash
python manage.py runserver
```

5. **Access the Application**:
   - Frontend: http://localhost:8000/
   - Admin Panel: http://localhost:8000/admin/

## Usage

### Adding News Sources

1. Go to the admin panel at http://localhost:8000/admin/
2. Log in with your superuser credentials
3. Navigate to "News Sources"
4. Click "Add News Source"
5. Fill in the details:
   - **Name**: The name of the news source (e.g., "BBC News")
   - **URL**: The main website URL
   - **RSS URL**: The RSS/Atom feed URL
   - **Category**: Select or create a category
   - **Country**: Optional country of origin
   - **Language**: Default is "en" for English
   - **Is Active**: Check to enable fetching
   - **Fetch Interval**: Minutes between fetches (default: 60)

### Pre-configured Financial Sources

The app comes pre-loaded with these premium financial news sources:

1. **Yahoo Finance** - Stock market news and financial analysis
2. **Wall Street Journal** - Business and financial news
3. **New York Times Business** - Business and economy coverage
4. **Financial Times** - Global business and financial news
5. **The Economist** - Global news, politics, business and finance

### Additional RSS Feeds You Can Add

**More Financial News:**
- Bloomberg Markets: https://www.bloomberg.com/feeds/podcasts/etf_report.xml
- Reuters Business: https://www.reutersagency.com/feed/?taxonomy=best-topics&post_type=best
- CNBC Top News: https://www.cnbc.com/id/100003114/device/rss/rss.html
- MarketWatch: http://feeds.marketwatch.com/marketwatch/topstories/

**Business & Tech:**
- Forbes: https://www.forbes.com/real-time/feed2/
- Business Insider: https://www.businessinsider.com/rss
- TechCrunch: https://techcrunch.com/feed/

### Fetching News

To fetch news articles from all active sources:

```bash
python manage.py fetch_news
```

**Options**:
- `--source <name>`: Fetch from a specific source only
- `--force`: Force fetch even if recently fetched

**Examples**:
```bash
# Fetch from all active sources
python manage.py fetch_news

# Fetch from a specific source
python manage.py fetch_news --source "Yahoo Finance"

# Force fetch regardless of interval
python manage.py fetch_news --force
```

### Automating News Fetching

You can set up a cron job or scheduled task to automatically fetch news:

**Linux/Mac (using cron)**:
```bash
# Edit crontab
crontab -e

# Add this line to fetch news every hour
0 * * * * cd /path/to/worldView && python manage.py fetch_news
```

**Windows (using Task Scheduler)**:
Create a task that runs `python manage.py fetch_news` at your desired interval.

## Project Structure

```
worldView/
├── worldnews/           # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── news/                # News app
│   ├── models.py        # Database models (Category, NewsSource, Article)
│   ├── views.py         # View functions
│   ├── admin.py         # Admin interface configuration
│   ├── urls.py          # URL patterns
│   ├── templates/       # HTML templates
│   │   └── news/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── category.html
│   │       ├── source.html
│   │       ├── article_detail.html
│   │       └── search.html
│   └── management/      # Management commands
│       └── commands/
│           └── fetch_news.py
├── manage.py
└── requirements.txt
```

## Models

### Category
- Name and slug for URL-friendly paths
- Description
- Related articles and sources

### NewsSource
- Name, URL, and RSS feed URL
- Country and language
- Active status and fetch interval
- Last fetched timestamp

### Article
- Title, URL, author
- Description and content
- Image URL
- Published and fetched timestamps
- Many-to-many relationship with categories

## Features Explained

### Search
- Full-text search across article titles, descriptions, content, and authors
- Results are paginated for easy browsing

### Categories
- Organize news by topics (e.g., Politics, Technology, Sports)
- Each category shows article count
- Filter articles by category

### Sources
- View articles from specific news sources
- See source metadata (country, category, last fetched time)
- Deactivate sources without deleting them

### Admin Interface
- Comprehensive admin panel for managing all content
- Bulk actions for managing multiple articles
- Filtering and search capabilities

## Tips

1. **Start with a few sources**: Don't add too many sources at once. Start with 3-5 sources and expand.

2. **Set appropriate intervals**: News sources update at different frequencies. Major news sites might update every 15-30 minutes, while smaller blogs might update daily.

3. **Monitor fetch times**: Check the admin panel to see when sources were last fetched and ensure they're updating properly.

4. **Use categories wisely**: Create broad categories rather than too many specific ones for better organization.

5. **Regular maintenance**: Periodically review and clean up old articles to keep the database manageable.

## Development

To extend this application, you might want to add:

- User accounts and personalized feeds
- Bookmarking/favoriting articles
- Email notifications for new articles
- API endpoints for mobile apps
- Advanced filtering (by date, source, etc.)
- Social media sharing
- Article recommendations based on reading history

## License

This project is open source and available for educational and personal use.
