from datetime import datetime
import os
import webapp2
import jinja2

from google.appengine.ext import db
from google.appengine.api import users

from models import Comic, Image, Comment

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = \
    jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))


class BaseHandler(webapp2.RequestHandler):

    def render_template(
        self,
        filename,
        template_values,
        **template_args
        ):
        template = jinja_environment.get_template(filename)
        self.response.out.write(template.render(template_values))

class ShowComics(BaseHandler):
    
    def get(self):
        user = users.get_current_user()
        if user:
            comics = Comic.all()
            self.response.out.write(
                "%s (%s) <a href='%s'>Salir</a>" % 
                (user.nickname(), users.is_current_user_admin(), users.create_logout_url('/'))
            )
            self.render_template('adds.html', {'comics': comics, 'user': user})
        else:
            self.redirect(users.create_login_url(self.request.uri))
        
class NewComic(BaseHandler):

    def post(self):
        comic = Comic(name=self.request.get('inputName'),
                      description=self.request.get('inputDescription'),
                      cover=self.request.get('inputURL'))
        comic.put()
        return webapp2.redirect('/')

    def get(self):
        self.render_template('new.html', {})


class ViewComic(BaseHandler):

    def get(self, comic_id):
        iden = int(comic_id)
        comic = db.get(db.Key.from_path('Comic', iden))
        self.render_template('show.html', {'comic': comic, 'id': comic_id})

class EditComic(BaseHandler):

    def post(self, comic_id):
        iden = int(comic_id)
        comic = db.get(db.Key.from_path('Comic', iden))
        comic.name = self.request.get('inputName')
        comic.description = self.request.get('inputDescription')
        comic.cover = self.request.get('inputURL')
        comic.update_date = datetime.now()
        comic.put()
        return webapp2.redirect('/')

    def get(self, comic_id):
        iden = int(comic_id)
        comic = db.get(db.Key.from_path('Comic', iden))
        self.render_template('edit.html', {'comic': comic})


class DeleteComic(BaseHandler):

    def get(self, comic_id):
        iden = int(comic_id)
        comic = db.get(db.Key.from_path('Comic', iden))
        db.delete(comic)
        return webapp2.redirect('/')


