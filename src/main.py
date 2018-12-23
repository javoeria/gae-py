from views import ShowComics, NewComic, EditComic, DeleteComic
import webapp2

app = webapp2.WSGIApplication([
        ('/', ShowComics), 
        ('/new', NewComic), 
        ('/edit/([\d]+)', EditComic),
        ('/delete/([\d]+)', DeleteComic),
        ],
        debug=True)
