# News Sources: RSS Feeds vs APIs

## Current Approach: RSS Feeds ✅

**You're already using the best method!**

RSS (Really Simple Syndication) feeds are:
- **Official publisher APIs** - News sites provide them for aggregators
- **No robots.txt issues** - Designed to be consumed
- **Free and unlimited** - No API keys or rate limits needed
- **Industry standard** - Used by Google News, Feedly, Apple News, etc.
- **Real-time** - Updates as soon as articles are published

### How RSS Feeds Work

1. News sites publish RSS/Atom feeds at URLs like:
   - `https://finance.yahoo.com/news/rssindex`
   - `https://www.wsj.com/xml/rss/...`

2. Your app fetches these feeds (using `atoma` library)

3. Extracts headlines, links, timestamps

4. Stores in database and displays

**This is exactly how professional news aggregators work!**

## Additional Free News APIs (Optional)

If you want to supplement RSS feeds with API data:

### 1. NewsAPI.org
- **Free tier**: 100 requests/day
- **Coverage**: 80,000+ sources worldwide
- **Best for**: Breaking news, keyword searches
- **Limitations**: 30-day archive limit on free tier
```python
# Example
import requests
response = requests.get(
    'https://newsapi.org/v2/top-headlines',
    params={'apiKey': 'YOUR_KEY', 'category': 'business'}
)
```

### 2. Finnhub (Financial News)
- **Free tier**: 60 calls/minute
- **Coverage**: Stock market news, company news
- **Best for**: Financial and market-specific news
- **Real-time**: Yes
```python
# Example
response = requests.get(
    'https://finnhub.io/api/v1/news',
    params={'category': 'general', 'token': 'YOUR_KEY'}
)
```

### 3. Mediastack
- **Free tier**: 500 requests/month
- **Coverage**: 7,500+ news sources
- **Best for**: Historical news data
- **Limitations**: No HTTPS on free tier
```python
# Example
response = requests.get(
    'http://api.mediastack.com/v1/news',
    params={'access_key': 'YOUR_KEY', 'categories': 'business'}
)
```

### 4. GNews API
- **Free tier**: 100 requests/day
- **Coverage**: Google News content
- **Best for**: International news
- **Languages**: 60+ languages supported
```python
# Example
response = requests.get(
    'https://gnews.io/api/v4/top-headlines',
    params={'token': 'YOUR_KEY', 'topic': 'business'}
)
```

### 5. Alpha Vantage (Financial)
- **Free tier**: 5 requests/minute, 500/day
- **Coverage**: Market news, stock-specific news
- **Best for**: Stock market and financial data
- **Real-time**: Yes
```python
# Example
response = requests.get(
    'https://www.alphavantage.co/query',
    params={
        'function': 'NEWS_SENTIMENT',
        'apikey': 'YOUR_KEY',
        'tickers': 'AAPL,MSFT'
    }
)
```

## Why RSS Feeds Are Better

| Feature | RSS Feeds | News APIs |
|---------|-----------|-----------|
| **Cost** | Free, unlimited | Free tier limited |
| **Rate Limits** | None | Yes (100-500/day) |
| **Setup** | No API key needed | Requires registration |
| **Blocked?** | Never | Can be rate limited |
| **Real-time** | Yes | Varies |
| **Official** | Publisher-provided | Third-party |
| **Reliability** | Very high | Depends on service |

## Best RSS Feeds for Financial News

### Premium Sources (Already Configured)
- Yahoo Finance: https://finance.yahoo.com/news/rssindex
- Wall Street Journal: https://feeds.a.dj.com/rss/RSSWorldNews.xml
- New York Times Business: https://rss.nytimes.com/services/xml/rss/nyt/Business.xml
- Financial Times: https://www.ft.com/?format=rss
- The Economist: https://www.economist.com/rss

### Additional Free RSS Feeds
- **Bloomberg Markets**: https://www.bloomberg.com/feed/podcast/etf-report.xml
- **Reuters Business**: https://www.reutersagency.com/feed/?taxonomy=best-topics&post_type=best
- **CNBC**: https://www.cnbc.com/id/100003114/device/rss/rss.html
- **MarketWatch**: http://feeds.marketwatch.com/marketwatch/topstories/
- **Forbes**: https://www.forbes.com/real-time/feed2/
- **Business Insider**: https://www.businessinsider.com/rss
- **Seeking Alpha**: https://seekingalpha.com/feed.xml
- **Barron's**: https://www.barrons.com/rss

### Crypto/Tech Finance
- **CoinDesk**: https://www.coindesk.com/arc/outboundfeeds/rss/
- **The Block**: https://www.theblockcrypto.com/rss.xml
- **TechCrunch Finance**: https://techcrunch.com/tag/fintech/feed/

## Finding More RSS Feeds

Most news sites have RSS feeds, even if not advertised:

1. **Look in page source** - Search for `<link rel="alternate" type="application/rss+xml"`
2. **Common patterns**:
   - `/rss`
   - `/feed`
   - `/rss.xml`
   - `/feed.xml`
3. **Use RSS discovery tools**:
   - https://rss.app/
   - Browser extensions like "RSS Feed Reader"

## Recommendation

**Stick with RSS feeds!** They're:
- More reliable than third-party APIs
- Free with no limits
- Official publisher channels
- Used by all major news aggregators

Only add APIs if you need features RSS doesn't provide (like sentiment analysis, keyword searches, or historical data).

## Implementation

Your current setup with `atoma` library for RSS parsing is perfect. The fetch_news command:

```bash
python manage.py fetch_news
```

Already handles:
- RSS and Atom feeds
- Deduplication (same article won't be added twice)
- Automatic scheduling based on fetch intervals
- Error handling for unavailable feeds

**Bottom line**: You're using the industry-standard approach. Don't change it!
