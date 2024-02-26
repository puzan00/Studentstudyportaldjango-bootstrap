from django.shortcuts import render
from newsapi import NewsApiClient
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required


@login_required
def news(request):
    # Initialize NewsApiClient with your API key
    newsApi = NewsApiClient(api_key="9ac32bbe3f4e43b09422b7e71abf0868")

    # Fetch news articles using NewsApiClient
    response = newsApi.get_everything(
        q="tech",
        sources="techcrunch,ars-technica,cnn,news24",
        language="en",
        sort_by="publishedAt",
        page_size=39,
    )

    articles = response.get("articles", [])

    # Get the current date and calculate the date one week ago
    current_date = datetime.now()
    one_week_ago = current_date - timedelta(days=7)

    mylist = []
    unique_articles = set()

    for article in articles:
        published_date = datetime.strptime(
            article.get("publishedAt", ""), "%Y-%m-%dT%H:%M:%SZ"
        )
        url_to_image = article.get("urlToImage")
        article_title = article.get("title")

        # Use the article title and image URL as a unique identifier
        article_identifier = (article_title, url_to_image)

        # Check if the article is within the last week, has an image, and is unique
        if (
            published_date >= one_week_ago
            and url_to_image
            and article_identifier not in unique_articles
        ):
            mylist.append(
                {
                    "desc": article.get("description", ""),
                    "news": article_title,
                    "img": url_to_image,
                    "published_at": article.get("publishedAt", ""),
                    "url": article.get("url", ""),
                }
            )
            # Add the article identifier to the set to mark it as processed
            unique_articles.add(article_identifier)

    return render(request, "news.html", context={"mylist": mylist})
