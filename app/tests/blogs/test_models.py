from app.extensions.database import db
from app.blogs.models import Article, Author
from datetime import datetime


def test_author_update(client):
    # updates cookie's properties
    ## Arrange Step
    author = Author(
        name="Testname",
        surname="Testsurname",
        email="test.name@email.com",
        password="testpassword",
        articles=[],
    )
    db.session.add(author)
    db.session.commit()
    ## Act Step
    author.name = "Nametest"
    author.save()
    ## Assess Step
    updated_author = Author.query.filter_by(surname="Testsurname").first()
    assert updated_author.name == "Nametest"


def test_author_delete(client):
    # deletes author
    ## Arrange
    author = Author(
        name="Testname",
        surname="Testsurname",
        email="test.name@email.com",
        password="testpassword",
        articles=[],
    )
    db.session.add(author)
    db.session.commit()
    ## Act
    author.delete()
    ## Assert
    deleted_author = Author.query.filter_by(name="Testname").first()
    assert deleted_author is None


def test_article_update(client):
    # updates article's properties
    ## Arrange Step
    article = Article(
        slug="test-article",
        title="Test Title",
        text="this is some Test or whatever.",
        dateTime=datetime.utcnow(),
        author_id=2,
    )
    db.session.add(article)
    db.session.commit()
    ## Act Step
    article.slug = "test-article"
    article.save()
    ## Assess Step
    updated_article = Article.query.filter_by(slug="test-article").first()
    assert updated_article.slug == "test-article"


def test_article_delete(client):
    # deletes article
    ## Arrange
    article = Article(
        slug="test-article",
        title="Test Title",
        text="this is some Test or whatever.",
        dateTime=datetime.utcnow(),
        author_id=2,
    )
    db.session.add(article)
    db.session.commit()
    ## Act
    article.delete()
    ## Assert
    deleted_article = Article.query.filter_by(slug="test-article").first()
    assert deleted_article is None
