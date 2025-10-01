import random, string, os
SECRET_KEY = "2lzUl{$*D6#`8uXqlU."
ABOUT = "Bienvenue sur la page à propos de Flask !"
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'monApp.db')
BOOTSTRAP_SERVE_LOCAL = True