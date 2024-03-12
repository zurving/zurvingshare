import cherrypy

class Redirector(object):
    @cherrypy.expose
    def index(self, code='QR Code using make() function'):
        # redirect slash to the right place
        raise cherrypy.HTTPRedirect('/z/s/r/')