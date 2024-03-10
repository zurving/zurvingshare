
# Importing library
import qrcode
import cherrypy
import io

class PQR(object):

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

cherrypy.quickstart(PQR(), '/pqr/qr', 'static.conf' )
 
