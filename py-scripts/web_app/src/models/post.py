#!/usr/bin/env python
from src.common.database import Database
import uuid
import datetime


class Post(object):

    def __init__(self, blog_id, title, content, author, cdate=datetime.datetime.utcnow(), _id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.cdate = cdate
        self._id = uuid.uuid4().hex if _id is None else _id

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    def json(self):
        return {
            '_id': self._id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'cdate': self.cdate
        }

    @classmethod
    def from_mongo(cls, id):
        posts_data = Database.find_one('posts', query={'_id': id})
        return cls(**posts_data)

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find('posts', {'blog_id': id})]
