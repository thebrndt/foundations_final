from flask import Blueprint, render_template, redirect, url_for, request, current_app
from app.blogs.models import Article, Author

blueprint = Blueprint("simple_pages", __name__)


@blueprint.route("/")
def index():
    return render_template("simple_pages/index.html")


@blueprint.route("/joinpage")
def joinpage():
    return render_template("simple_pages/joinpage.html")


# adds new user/author to database if email from fomr does not exist in database
@blueprint.post("/joinpage")
def post_joinpage():
    email = request.form.get("email")

    if Author.query.filter_by(email=email).first() is not None:
        return render_template(
            "simple_pages/joinpage.html",
            error="Error: A user with this email address already exists!",
        )

    author = Author(
        name=request.form.get("name"),
        surname=request.form.get("surname"),
        email=request.form.get("email"),
        password=request.form.get("password"),
    )
    author.save()

    return redirect(url_for("blogs.blogpage"))
