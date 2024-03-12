import cherrypy
import time
import os

class Shares(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        sharelist = []
        data = { 'shares': sharelist }
        return data