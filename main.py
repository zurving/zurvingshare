
# Importing library
import qrcode
import cherrypy
import io
import redirector
import status
import shares

class zurving_share(object):

    config = {
        '/r':
            {
            'tools.gzip.on': True,
            'tools.staticdir.on': True,
            'tools.staticdir.dir': '/ssd/workspace/zurvingshare/data',
            'tools.staticdir.index': 'index.html'
            },
        'status':
            {
            'interface': 'eth0'
            },
        'global':
            {
            'server.socket_host': '0.0.0.0',
            'server.socket_port': 8081
            }
    }

    @cherrypy.expose
    def index(self, code='QR Code using make() function'):
        # Data to be encoded
        data = code
        # Encoding data using make() function
        img = qrcode.make(data)
        # Saving as an image file0
        cherrypy.response.headers['Content-Type'] = 'image/png'
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr)
        img_byte_arr = img_byte_arr.getvalue()
        return img_byte_arr

cherrypy.tree.mount(redirector.Redirector(),'/')
cherrypy.tree.mount(shares.Shares(), '/z/shares', zurving_share.config)
cherrypy.tree.mount(status.Status(),'/z/status', zurving_share.config)
cherrypy.quickstart(zurving_share(), '/z/s', zurving_share.config)
 
