"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from blog_project.base.models import User, Post, async_session
from blog_project.config import DO_CLEAR_TABLES, POSTGRES_DB
from jsonplaceholder_requests import fetch_json, USERS_DATA_URL, POSTS_DATA_URL


async def clear_tables():
    async with async_session() as session:
        posts = session.query(Post).all()
        session.delete(posts)

        users = session.query(User).all()
        session.delete(users)

        await session.commit()


async def load_users(users: list):
    async with async_session() as session:

        for user in users:
            user_db = User(id=user.get('id'),
                           name=user.get('name'),
                           username=user.get('username'),
                           email=user.get('email'))
            session.add(user_db)
        await session.commit()


async def load_posts(posts: list):
    async with async_session() as session:

        for post in posts:
            post_db = Post(id=post.get('id'),
                           user_id=post.get('userId'),
                           title=post.get('title'),
                           body=post.get('body'))
            session.add(post_db)
        await session.commit()


async def async_main():
    users, posts = await asyncio.gather(fetch_json(url = USERS_DATA_URL),
                                        fetch_json(url = POSTS_DATA_URL))
    if DO_CLEAR_TABLES:
        await clear_tables()
    await load_users(users)
    await load_posts(posts)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
