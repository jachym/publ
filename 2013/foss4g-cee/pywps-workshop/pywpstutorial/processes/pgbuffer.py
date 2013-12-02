"""
OGR Buffer process

Author: Jachym Cepicky (jachym@les-ejk.cz) 
"""

from pywps.Process import WPSProcess                                
import types

import logging


class Process(WPSProcess):
     def __init__(self):
          # init process
         WPSProcess.__init__(self,
              identifier = "pgbuffer",
              title="Buffer process using GRASS-Python interface",
              version = "0.1",
              storeSupported = "true",
              statusSupported = "true",
              abstract="""Process demonstrating how to work with GRASS-Python
              interface inside PyWPS""",
              grassLocation=True)
              
         self.data = self.addComplexInput(identifier = "data",
                                            title = "Input vector file",
                                            formats=[{"mimeType":"text/xml"}]
                                            )
         self.size = self.addLiteralInput(identifier="size", 
                                           title="Buffer area size",
                                           allowedValues = [[-10000,10000]],
                                           type=types.FloatType)
         self.output =self.addComplexOutput(identifier="buffer", 
                                            title="Buffered data",
                                            formats=[{"mimeType":"text/xml"},
                                                     {"mimeType":"application/wfs-collection-1.1"}],
                                            useMapscript=True)
     def execute(self):

        # must be here, we need at least GISBASE to be set
        import sys
        sys.path.append("/home/jachym/usr/src/grass/grass6_devel/dist.x86_64-unknown-linux-gnu/etc/python/")
        from grass.script import core as grass

        # import
        self.status.set("Importing data",5)
        retCode = grass.run_command("v.in.ogr",flags="o", dsn=self.data.getValue(),out="data")
        logging.debug("v.in.ogr returned [%s]" % retCode)

        # make buffer
        self.status.set("Buffering",50)
        grass.run_command("v.buffer",input="data",out="buffer",distance=self.size.getValue())

        # export
        self.status.set("Exporting",90)
        grass.run_command("v.out.ogr",input="buffer",dsn="buffer.gml",type="boundary",format="GML")

        self.output.setValue("buffer.gml")
        self.output.projection="+init=epsg:102067"
        return
