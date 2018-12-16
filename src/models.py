from google.appengine.ext import db


class Adds(db.Model):

    author = db.EmailProperty()
    text = db.StringProperty()
    priority = db.IntegerProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    
class Comic(db.Model):
    
    creador = db.UserProperty(auto_current_user=True)
    nombre = db.StringProperty(required=True)
    descripcion = db.StringProperty(required=True)
    fecha_creacion = db.DateTimeProperty(auto_now_add=True)
    fecha_modificacion = db.DateTimeProperty(auto_now_add=True)
     
class Imagen(db.Model):
    comic = db.ReferenceProperty(Comic, collection_name='imagenes_set')
    usuario = db.UserProperty(auto_current_user=True)
    url = db.StringProperty(
    texto = db.StringProperty())
    fecha = db.DateTimeProperty(auto_now_add=True)
   
class Comentario(db.Model):
    
    evento = db.ReferenceProperty(Comic, collection_name='comentarios_set')
    usuario = db.UserProperty(auto_current_user=True)
    texto = db.StringProperty()
    nota = db.BooleanProperty(required=True)
    fecha = db.DateTimeProperty(auto_now_add=True)
