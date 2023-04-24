from app.blogs.models import Article, Author
from datetime import datetime


def test_articles_renders_articles(client):
    # Page loads and renders articles
    new_article = Article(
        slug="test-article-1",
        title="Test Article 1",
        text="This is a test article and stuff.",
        dateTime=datetime.utcnow(),
        author_id=4,
    )
    new_article.save()

    response = client.get("/blogpage")

    assert b"Test Article 1" in response.data


def test_get_newpost_renders(client):
    # Page Loads and Renders new post
    response = client.get("/post")
    assert b"New Post" in response.data


def test_post_newpost_creates_article(client):
    # Create a post record
    response = client.post(
        "/post",
        data={
            "slug": "test-article-2",
            "title": "A Test Article Title",
            "text": "Test Article text stuff.",
            "dateTime": datetime.utcnow(),
            "author_id": 1,
        },
    )

    assert Article.query.filter_by(text="Test Article text stuff.").first() is not None


def test_joinpage_creates_author(client):
    # Create an author record
    response = client.post(
        "/joinpage",
        data={
            "name": "TDDName",
            "surname": "TDDSurname",
            "email": "tdd@email.com",
            "password": "tddpassword",
            # "articles": [1],
        },
    )

    assert Author.query.filter_by(name="TDDName").first() is not None
