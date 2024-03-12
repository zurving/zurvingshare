import cherrypy
import psutil
import time
import os

class Status(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        u,p = self.getNetwork()
        data = {
            'temp': self.getTemp(),
            'load': self.getLoad(),
            'memory': self.getMemory(),
            'upload': u,
            'download': p
        }
        return data
    
    def getTemp(self):
        with open('/sys/devices/virtual/thermal/thermal_zone0/temp') as f:
            data = f.read()
        retval = float( data ) / 1000
        return retval

    def getLoad(self):
        load1, load5, load15 = psutil.getloadavg()
        cpu_usage = (load1/os.cpu_count())
        return cpu_usage
        
    def getMemory(self):
        return psutil.virtual_memory()[2]

    def getNetwork(self):
        iface = cherrypy.request.app.config['status']['interface']
        counter = psutil.net_io_counters(pernic=True)[iface]
        time.sleep( 1 )
        counter2 = psutil.net_io_counters(pernic=True)[iface]
        up = counter2.bytes_sent - counter.bytes_sent
        down = counter2.bytes_recv - counter.bytes_recv
        return up,down
        
    def getNetworkDown(self):
        return 0
