from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q, Count
from .models import Article, Category, NewsSource


def home(request):
    articles = Article.objects.select_related('source').prefetch_related('categories').all()
    categories = Category.objects.annotate(article_count=Count('articles')).all()
    sources = NewsSource.objects.filter(is_active=True).annotate(article_count=Count('articles')).all()

    paginator = Paginator(articles, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'categories': categories,
        'sources': sources,
        'total_articles': articles.count(),
    }
    return render(request, 'news/home.html', context)


def category_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(categories=category).select_related('source').prefetch_related('categories')

    paginator = Paginator(articles, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'category': category,
        'page_obj': page_obj,
    }
    return render(request, 'news/category.html', context)


def source_view(request, source_id):
    source = get_object_or_404(NewsSource, id=source_id)
    articles = Article.objects.filter(source=source).select_related('source').prefetch_related('categories')

    paginator = Paginator(articles, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'source': source,
        'page_obj': page_obj,
    }
    return render(request, 'news/source.html', context)


def article_detail(request, article_id):
    article = get_object_or_404(
        Article.objects.select_related('source').prefetch_related('categories'),
        id=article_id
    )

    related_articles = Article.objects.filter(
        source=article.source
    ).exclude(id=article.id).select_related('source')[:5]

    context = {
        'article': article,
        'related_articles': related_articles,
    }
    return render(request, 'news/article_detail.html', context)


def search(request):
    query = request.GET.get('q', '')
    articles = Article.objects.none()

    if query:
        articles = Article.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(content__icontains=query) |
            Q(author__icontains=query)
        ).select_related('source').prefetch_related('categories')

    paginator = Paginator(articles, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'query': query,
        'page_obj': page_obj,
    }
    return render(request, 'news/search.html', context)
