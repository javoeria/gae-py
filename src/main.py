from views import ShowComics, NewComic, ViewComic, EditComic, DeleteComic
import webapp2

app = webapp2.WSGIApplication([
        ('/', ShowComics),
        ('/new', NewComic),
        ('/show/([\d]+)', ViewComic),
        ('/edit/([\d]+)', EditComic),
        ('/delete/([\d]+)', DeleteComic),
        ],
        debug=True)
