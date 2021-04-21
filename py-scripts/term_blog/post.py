#!/usr/bin/env python
from database import Database
import uuid
import datetime


class Post(object):

    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.date = date
        self.id = uuid.uuid4().hex if id is None else id

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'cdate': self.date
        }

    @classmethod
    def from_mongo(cls, id):
        posts_data = Database.find_one('posts', query={'id': id})
        return cls(blog_id=posts_data['blog_id'],
                   title=posts_data['title'],
                   content=posts_data['content'],
                   author=posts_data['author'],
                   date=posts_data['cdate'],
                   id=posts_data['id'])

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find('posts', {'blog_id': id})]
