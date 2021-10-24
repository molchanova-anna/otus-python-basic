from sqlalchemy import func

from models.database import db
from datetime import datetime


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(4000), nullable=True)
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        server_default=func.now(),
    )
    posts = db.relationship('Post', back_populates='category')


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    text = db.Column(db.String, nullable=True)
    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        server_default=func.now(),
    )
    id_category = db.Column(db.Integer,
                            db.ForeignKey("category.id"),
                            nullable=True)
    category = db.relationship('Category', back_populates='posts')
