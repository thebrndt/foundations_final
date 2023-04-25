# Import necessary modules and functions
from flask import Blueprint, render_template, request, current_app, redirect, url_for
from .models import Article, Author
from datetime import datetime

blueprint = Blueprint("blogs", __name__)


# displays a list of all the articles, and paginates
@blueprint.route("/blogpage")
def blogpage():
    page_number = request.args.get("page", 1, type=int)
    articles_pagination = Article.query.paginate(
        page=page_number, per_page=current_app.config["ARTICLES_PER_PAGE"]
    )
    return render_template("blogs/index.html", articles_pagination=articles_pagination)


# display a single article in a template
@blueprint.route("/blogpage/<slug>")
def blog(slug):
    article = Article.query.filter_by(slug=slug).first_or_404()
    return render_template("blogs/show.html", article=article)


# displays form for creating a new aritcle,
@blueprint.get("/post")
def get_newpost():
    authors = Author.query.all()
    return render_template("blogs/newpost.html", authors=authors)


# creates a new article if it's slug does not already exist
@blueprint.post("/post")
def post_newpost():
    authors = Author.query.all()
    # Return an error message if slug already exists
    slug = request.form.get("slug")
    if Article.query.filter_by(slug=slug).first() is not None:
        return render_template(
            "blogs/newpost.html",
            authors=authors,
            error="Error: A post with this slug already exists!",
        )

    # Create new post with form data
    post = Article(
        slug=request.form.get("slug"),
        title=request.form.get("title"),
        text=request.form.get("text"),
        dateTime=datetime.utcnow(),
        author_id=int(request.form.get("author_id", 0)),
    )
    post.save()

    return redirect(url_for("blogs.blogpage"))


# deletes a post from the database
@blueprint.post("/delete_post")
def delete_post():
    target = request.form.get("id")
    article = Article.query.filter_by(id=target).first()
    article.delete()
    return redirect(url_for("blogs.blogpage"))


# displays form for editing a specific article
@blueprint.get("/edit_post/<id>")
def show_edit_post(id):
    blog = Article.query.filter_by(id=id).first()
    authors = Author.query.all()

    return render_template("blogs/edit.html", blog=blog, authors=authors)


# retrieves article from the databse and updates it based on attributes from the form
@blueprint.post("/edit_post")
def edit_post():
    target = request.form.get("id")
    article = Article.query.filter_by(id=target).first()

    slug = request.form.get("slug")
    title = request.form.get("title")
    text = request.form.get("text")

    article.slug = slug
    article.title = title
    article.text = text

    article.save()

    return redirect(url_for("blogs.blogpage"))


# route request to seed the database with sample data
# used once during deployment and not again
# @blueprint.route("/run-seed")
# def run_seed():
#     if not Article.query.filter_by(slug="article-1").first():
#         import app.scripts.seed

#         return "Database seed completed!"
#     else:
#         return "Nothing to run."
