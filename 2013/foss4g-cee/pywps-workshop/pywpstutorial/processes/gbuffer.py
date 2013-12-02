"""
OGR Buffer process

Author: Jachym Cepicky (jachym@les-ejk.cz) 
"""

from pywps.Process import WPSProcess                                
import types

import subprocess

class Process(WPSProcess):
     def __init__(self):
          # init process
         WPSProcess.__init__(self,
              identifier = "grassbuffer",
              title="Buffer process using GRASS",
              version = "0.1",
              storeSupported = "true",
              statusSupported = "true",
              abstract="Process demonstrating how to work with GRASS inside PyWPS",
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
                                            formats=[{"mimeType":"text/xml"}])
     def execute(self):


        # import
        self.status.set("Importing data",5)
        subprocess.call(["v.in.ogr","-o","dsn=%s"%self.data.getValue(),"out=data"])

        # make buffer
        self.status.set("Buffering",50)
        subprocess.call(["v.buffer","in=data","out=buffer","distance=%s"%self.size.getValue()])

        # export
        self.status.set("Exporting",90)
        subprocess.call(["v.out.ogr","in=buffer","dsn=buffer.gml","type=boundary","format=GML"])

        self.output.setValue("buffer.gml")
        return
