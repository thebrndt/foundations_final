# Import necessary modules and functions
from app.app import create_app
from app.blogs.models import Author, Article
from app.extensions.database import db
from datetime import datetime

# Check if this file is being run as the main program and create a flask app and push the application context for the flask app
if __name__ == "__main__":
    app = create_app()
    app.app_context().push()

# Define lists of dictionaries containing author and article data
authors_data = [
    {
        "name": "John",
        "surname": "Doe",
        "email": "johndoe@example.com",
        "password": "pass1234",
        "articles": [],
    },
    {
        "name": "Jane",
        "surname": "Doe",
        "email": "janedoe@example.com",
        "password": "pass5678",
        "articles": [],
    },
    {
        "name": "Bob",
        "surname": "Smith",
        "email": "bobsmith@example.com",
        "password": "pass9876",
        "articles": [],
    },
]
articles_data = [
    {
        "slug": "article-1",
        "title": "My First Article",
        "text": "This is the text of my first article.",
        "dateTime": datetime.utcnow(),
        "author_id": 1,
    },
    {
        "slug": "article-2",
        "title": "My Second Article",
        "text": "This is the text of my second article.",
        "dateTime": datetime.utcnow(),
        "author_id": 2,
    },
    {
        "slug": "article-3",
        "title": "My Third Article",
        "text": "This is the text of my third article.",
        "dateTime": datetime.utcnow(),
        "author_id": 3,
    },
]

# Loop through the authors data and create new Author objects, adding them to the database
for author_data in authors_data:
    new_author = Author(
        name=author_data["name"],
        surname=author_data["surname"],
        email=author_data["email"],
        password=author_data["password"],
        articles=author_data["articles"],
    )
    db.session.add(new_author)
# Commit the new authors to the database
db.session.commit()

# Loop through the articles data and create new Article objects, adding them to the database
for article_data in articles_data:
    new_article = Article(
        slug=article_data["slug"],
        title=article_data["title"],
        text=article_data["text"],
        dateTime=article_data["dateTime"],
        author_id=article_data["author_id"],
    )
    db.session.add(new_article)
# Commit the new articles to the database
db.session.commit()
