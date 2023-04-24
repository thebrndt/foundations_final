from app.extensions.database import db, CRUDMixin
from datetime import datetime


class Author(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    surname = db.Column(db.String(128))
    email = db.Column(db.String(80))
    password = db.Column(db.String(16))
    articles = db.relationship("Article", backref="author", lazy=True)


class Article(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), unique=True)
    title = db.Column(db.String(80))
    text = db.Column(db.Text())
    dateTime = db.Column(
        db.DateTime, server_default=db.func.now(), default=datetime.utcnow
    )
    author_id = db.Column(
        db.Integer, db.ForeignKey("author.id", name="article_author_fk"), nullable=False
    )
