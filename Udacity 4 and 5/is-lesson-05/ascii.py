#!/usr/bin/env python

import os
import re
import sys
import webapp2
import jinja2
import urllib2
from xml.dom import minidom 
from string import letters

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

IP_URL = "http://api.hostip.info/?ip="
def get_coords(ip):
    ip = "
    url = IP_URL + ip
    content = None
    try:
        content = urllib2.urlopen(url).read()
    except URLError:
        return

    if content:
        d = minidom.parseString(content)
        coords = d.getElementsByTagName("gml:coordinates")
        if coords and coords[0].childNodes[0].nodeValue:
            lon, lat = coords[0].childNodes[0].nodeValue.split(',')
            return db.GeoPt(lat, lon)

class Art(db.Model):
    title = db.StringProperty(required = True)
    art = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    coords = db.GeoPtProperty()

class MainPage(Handler):
    def render_front(self, title="", art="", error=""):
        arts = db.GqlQuery("SELECT * "
                           "FROM Art "
                           "where ANCESTORS IS :1 "
                           "ORDER BY created DESC "
                           "LIMIT 10",
                           art_key)
        
        self.render("front.html",
                    title=title,
                    art=art,
                    error=error,
                    arts=arts)
        
    
    def get(self):
        self.write(repr(get_coords(self.request.remote_addr)))
        return self.render_front()

    def post(self):
        title = self.request.get("title")
        art = self.request.get("art")

        if title and art:
            a = Art(parent = art_key, title = title, art = art)
            coords = get_coords(self.request.remote_addr)
            if coords:
                p.coords = coords
            #lookup the user's coordinates from their IP
            #if coordinates, add the to Art
            a.put()

            self.redirect("/")
        else:
            error = "we need both a title and some artwork!"
            self.render_front(title = title,
                              art = art,
                              error = error)
        

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
