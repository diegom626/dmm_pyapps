#!/usr/bin/env python
from src.common.database import Database
from src.models.blog import Blog
from src.models.user import User

Database.initialize()

blog = Blog("test", "hola", "una descripcion", "3d1a10e1c5ee48b8aaf838a2acb4127b", "5a94357d59ba551796f87b65")
user = User.get_by_email("erikbeat98@gmail.com")
# user.new_blog('titulo2222', 'description3000')

posts = blog.get_posts()

print(user.get_blogs())
