import views
import webapp2

app = webapp2.WSGIApplication([
        ('/', views.ShowAdds), 
        ('/comics', views.ShowAdds), 
        ('/new', views.NewAdd), 
        ('/edit/([\d]+)', views.EditAdd),
        ('/delete/([\d]+)', views.DeleteAdd),
        ],
        debug=True)
