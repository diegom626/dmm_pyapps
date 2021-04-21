#!/usr/bin/env python
from blog import Blog
from database import Database


class Menu(object):
    def __init__(self):
        self.user = input("Ingrese su nombre de usuario para publicar: ")
        self.user_blog = None
        if self._user_has_account():
            print("Bienvenido de nuevo {}".format(self.user))
        else:
            self._prompt_user_account()

    def _user_has_account(self):
        blog = Database.find_one(collection='blogs', query={'author': self.user})
        if blog is not None:
            self.user_blog = Blog.get_from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_account(self):
        title = input("Ingrese el titulo del blog: ")
        description = input("Ingrese descripcion: ")
        blog = Blog(author=self.user, title=title, description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        read_or_write = input("Desea escribir (W) o leer (R)? (Cualquiera para salir): ")
        if read_or_write == 'R':
            blogs = Database.find('blogs', {})
            for blog in blogs:
                print("ID: {}, 'Title: {}, Author: {}".format(blog['id'], blog['title'], blog['author']))
            poner_id = input("copie el id listado de los blogs y pequelo para visualizar posts: ")
            blog = Blog.get_from_mongo(poner_id)
            posts = blog.get_posts()
            for post in posts:
                print("Date: {}, title: {}\n\n{}\n\n".format(post['cdate'], post['title'], post['content']))
        elif read_or_write == 'W':
            self.user_blog.new_post()
            self.run_menu()
        else:
            print("Gracias por tu visita, {}".format(self.user))

    
