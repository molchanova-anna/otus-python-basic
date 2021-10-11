"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base, joinedload, selectinload, relationship

from blog_project.config import POSTGRES_DB


engine = create_async_engine(
    POSTGRES_DB,
    echo=True,
)

async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)

Base = declarative_base(bind=engine)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False)
    email = Column(String(100), nullable=False)
    posts = relationship('Post', back_populates='user')

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    title = Column(String(255), nullable=False)
    body = Column(String, nullable=False)
    user = relationship('User', back_populates='posts')


#async def create_users_and_posts():
    #pass

