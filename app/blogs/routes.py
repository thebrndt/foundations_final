from flask import Blueprint, render_template, request, current_app, redirect, url_for
from .models import Article, Author
from datetime import datetime

blueprint = Blueprint("blogs", __name__)


@blueprint.route("/blogpage")
def blogpage():
    page_number = request.args.get("page", 1, type=int)
    articles_pagination = Article.query.paginate(
        page=page_number, per_page=current_app.config["ARTICLES_PER_PAGE"]
    )
    return render_template("blogs/index.html", articles_pagination=articles_pagination)


@blueprint.route("/blogpage/<slug>")
def blog(slug):
    article = Article.query.filter_by(slug=slug).first_or_404()
    return render_template("blogs/show.html", article=article)


@blueprint.get("/post")
def get_newpost():
    authors = Author.query.all()
    return render_template("blogs/newpost.html", authors=authors)


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


@blueprint.post("/delete_post")
def delete_post():
    target = request.form.get("id")
    article = Article.query.filter_by(id=target).first()
    article.delete()
    return redirect(url_for("blogs.blogpage"))


@blueprint.get("/edit_post/<id>")
def show_edit_post(id):
    blog = Article.query.filter_by(id=id).first()
    authors = Author.query.all()

    return render_template("blogs/edit.html", blog=blog, authors=authors)


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
