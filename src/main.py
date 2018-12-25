from views import ShowComics, NewComic, NewImage, ViewComic, EditComic, DeleteComic, DeleteComment, DeleteImage
import webapp2

app = webapp2.WSGIApplication([
        ('/', ShowComics),
        ('/new', NewComic),
        ('/set/([\d]+)', NewImage),
        ('/show/([\d]+)', ViewComic),
        ('/edit/([\d]+)', EditComic),
        ('/delete/([\d]+)', DeleteComic),
        ('/out', DeleteComment),
        ('/out2', DeleteImage),
        ],
        debug=True)
