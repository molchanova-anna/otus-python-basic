import logging
import os

from flask import Flask, request
from flask_migrate import Migrate

from models import Category
from models.database import db
from flask import Flask, request, render_template
from flask import Blueprint, request, render_template, redirect, url_for
from werkzeug.exceptions import NotFound, BadRequest, InternalServerError
from sqlalchemy.exc import IntegrityError, DatabaseError
log = logging.getLogger(__name__)

app = Flask(__name__)

SQLALCHEMY_DATABASE_URI = os.getenv("DB_CONN_URI", "postgresql+psycopg2://user:password@localhost:5432/blog")
app.config.update(
    SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)
db.init_app(app)
migrate = Migrate(app, db)



@app.route("/", endpoint="index")
def index():
    return render_template("index.html")


@app.route("/about/", endpoint="about")
def get_about():
    return render_template("about.html")


@app.route("/categories/", endpoint="categories")
def get_categories_list():
    categories = Category.query.all()
    return render_template("categories.html", cats=categories)


@app.route("/categories/add/", methods=["GET", "POST"], endpoint="add_category")
def create_category():
    if request.method == "GET":
        return render_template("add_category.html")

    category_name = request.form.get("category-name")
    if not category_name:
        raise BadRequest("Please provide category name!")

    category = Category(name=category_name)
    db.session.add(category)
    try:
        db.session.commit()
    except IntegrityError:
        log.exception("Could not add category, got integrity error")
        db.session.rollback()
        raise BadRequest("Error adding new category, probably the name is not unique")
    except DatabaseError:
        log.exception("Could not add category, got database error")
        db.session.rollback()
        raise InternalServerError("Error adding new category")
    return redirect(url_for("categories"))
    #return redirect(url_for("products_app.detail", category_id=category.id))
