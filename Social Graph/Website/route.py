import webapp2
import urllib2
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):

    def get(self):
        template_values = {}
        path = 'templates/index.html'
        self.response.out.write(template.render(path, template_values))



class followersHandler(webapp2.RequestHandler):

    def get(self):
        template_values = {}
        path = 'templates/followers.html'
        self.response.out.write(template.render(path, template_values))

class repovisHandler(webapp2.RequestHandler):

    def get(self):
        template_values = {}
        path = 'templates/repovis.html'
        self.response.out.write(template.render(path, template_values))

page_list = [('/', MainPage),
             ('/followersvis', followersHandler),
             ('/repovis', repovisHandler)
             ]
app = webapp2.WSGIApplication(page_list,
                              debug=True)
