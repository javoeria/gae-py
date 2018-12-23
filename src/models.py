from google.appengine.ext import db


class Comic(db.Model):

    author = db.UserProperty(auto_current_user=True)
    name = db.StringProperty(required=True)
    description = db.StringProperty(required=True)
    cover = db.URLProperty(required=True)
    create_date = db.DateTimeProperty(auto_now_add=True)
    update_date = db.DateTimeProperty(auto_now_add=True)
    
class Image(db.Model):

    comic = db.ReferenceProperty(Comic, collection_name='images_set')
    user = db.UserProperty(auto_current_user=True)
    link = db.URLProperty(required=True)
    text = db.StringProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    
class Comment(db.Model):

    comic = db.ReferenceProperty(Comic, collection_name='comments_set')
    user = db.UserProperty(auto_current_user=True)
    mark = db.BooleanProperty(required=True)
    text = db.StringProperty()
    date = db.DateTimeProperty(auto_now_add=True)
