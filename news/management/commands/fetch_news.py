import requests
import atoma
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from news.models import NewsSource, Article, Category


class Command(BaseCommand):
    help = 'Fetch news articles from RSS feeds'

    def add_arguments(self, parser):
        parser.add_argument(
            '--source',
            type=str,
            help='Fetch from a specific source (by name or ID)',
        )
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force fetch even if recently fetched',
        )

    def handle(self, *args, **options):
        sources = NewsSource.objects.filter(is_active=True)

        if options['source']:
            source_filter = sources.filter(name__icontains=options['source'])
            if options['source'].isdigit():
                source_filter = source_filter | sources.filter(id=int(options['source']))
            sources = source_filter

        if not sources.exists():
            self.stdout.write(self.style.WARNING('No active news sources found'))
            return

        for source in sources:
            if not options['force']:
                if source.last_fetched:
                    time_diff = timezone.now() - source.last_fetched
                    if time_diff < timedelta(minutes=source.fetch_interval):
                        self.stdout.write(
                            self.style.WARNING(
                                f'Skipping {source.name} (fetched {time_diff.seconds//60} minutes ago)'
                            )
                        )
                        continue

            self.stdout.write(f'Fetching from {source.name}...')

            try:
                articles_created = self.fetch_from_source(source)
                source.last_fetched = timezone.now()
                source.save()

                self.stdout.write(
                    self.style.SUCCESS(
                        f'Successfully fetched {articles_created} new articles from {source.name}'
                    )
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error fetching from {source.name}: {str(e)}')
                )

    def fetch_from_source(self, source):
        response = requests.get(source.rss_url, timeout=30)
        response.raise_for_status()

        content_type = response.headers.get('content-type', '')

        articles_created = 0

        try:
            feed = atoma.parse_rss_bytes(response.content)
            articles_created = self.process_rss_feed(feed, source)
        except Exception:
            try:
                feed = atoma.parse_atom_bytes(response.content)
                articles_created = self.process_atom_feed(feed, source)
            except Exception as e:
                raise Exception(f"Could not parse feed as RSS or Atom: {str(e)}")

        return articles_created

    def process_rss_feed(self, feed, source):
        articles_created = 0

        for item in feed.items:
            try:
                published_at = item.pub_date
                if published_at is None:
                    published_at = timezone.now()
                elif published_at.tzinfo is None:
                    published_at = timezone.make_aware(published_at)

                article, created = Article.objects.get_or_create(
                    url=item.link,
                    defaults={
                        'title': item.title or 'No Title',
                        'source': source,
                        'description': getattr(item, 'description', '') or '',
                        'content': getattr(item, 'content', '') or '',
                        'author': getattr(item, 'author', '') or '',
                        'published_at': published_at,
                    }
                )

                if created:
                    if source.category:
                        article.categories.add(source.category)
                    articles_created += 1
            except Exception as e:
                self.stdout.write(
                    self.style.WARNING(f'Error processing item: {str(e)}')
                )
                continue

        return articles_created

    def process_atom_feed(self, feed, source):
        articles_created = 0

        for entry in feed.entries:
            try:
                published_at = entry.published
                if published_at is None:
                    published_at = entry.updated if entry.updated else timezone.now()
                elif published_at.tzinfo is None:
                    published_at = timezone.make_aware(published_at)

                link = entry.links[0].href if entry.links else ''

                article, created = Article.objects.get_or_create(
                    url=link,
                    defaults={
                        'title': entry.title.value if hasattr(entry.title, 'value') else str(entry.title),
                        'source': source,
                        'description': getattr(entry, 'summary', '') or '',
                        'content': getattr(entry, 'content', '') or '',
                        'author': ', '.join([a.name for a in entry.authors]) if entry.authors else '',
                        'published_at': published_at,
                    }
                )

                if created:
                    if source.category:
                        article.categories.add(source.category)
                    articles_created += 1
            except Exception as e:
                self.stdout.write(
                    self.style.WARNING(f'Error processing entry: {str(e)}')
                )
                continue

        return articles_created
