.. PyWPS Tutorial FOSS4G 2011 documentation master file, created by
   sphinx-quickstart on Fri Sep  9 12:14:21 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PyWPS Tutorial FOSS4G 2011
=====================================

This tutorial is not about WPS itself (check, if this is needed to go
trough).

About PyWPS
-----------
http://pywps.wald.intevation.org/documentation/course/introduction/index.html

* http://pywps.wald.intevation.de

Continue with http://pywps.wald.intevation.de/documentation/course/ or
file:///home/jachym/usr/src/pywps/docs/course/

Installation
------------
http://pywps.wald.intevation.org/documentation/course/installation/index.html

* Use version 3.2.1 or Trunk
* Install into `/home/jachym/usr/src/pywpstutorial`, backup is in
  `/home/jachym/Dokumenty/clanky/2011/foss4g/pywps-tutorial/pywpstutorial`

Configuration
-------------
http://pywps.wald.intevation.org/documentation/course/configuration/index.html

Sample configuration file in `/home/jachym/Dokumenty/clanky/2011/foss4g/pywps-tutorial/pywpstutorial`

Wrapper script
--------------
http://pywps.wald.intevation.org/documentation/course/server/index.html

Custom process
--------------
http://pywps.wald.intevation.org/documentation/course/process/index.html
http://pywps.wald.intevation.org/documentation/course/testing/index.html

* Deploy `__all__` in `__init__.py`
* Start with OGR process

GRASS Process
"""""""""""""
http://pywps.wald.intevation.org/documentation/pywps-3.2/special/grass.html

* Check the configuration file again
* Continue with GRASS
* Continue with GRASS-Python interface

Logging
"""""""
* logging package
* sys.stderr
* return value
* process.status.set(string, integer)

####################################
MAPSERVER, JAVA, QGIS or JAVASCRIPT?
####################################

Attendees have to make the choice

UMN MapServer
-------------
http://pywps.wald.intevation.org/documentation/pywps-3.2/special/mapserver.html

* In `gpbuffer.py` useMapscript
* Check the configuration file again
* Result can be viewed with http://briseide.localhost/map/index2.php in WFS
  client

QGIS
-----
http://pywps.wald.intevation.org/documentation/pywps-3.2/clients/qgis.html

Video example: http://underdark.wordpress.com/2011/01/28/qgis-with-wps-plugin-in-action/

Java
----
http://pywps.wald.intevation.org/documentation/pywps-3.2/special/java.html

.. code-block:: sh
   :linenos:

    cd ~/usr/tomcat/apache-tomcat-6.0.29/webapps
    mkdir wpstutorial
    cd wpstutorial

* Continue with http://pywps.wald.intevation.org/documentation/pywps-3.2/special/java.html

* Use trunk version of  PyWPS

.. code-block:: sh
   :linenos:

    ln -s /home/jachym/usr/src/pywps/trunk/pywps # in wpstutorial dir

* Jython is at `JYTHON_HOME` is `~/usr/lib/jython/jython2.5.1`

* Do *NOT* use the first example of PywpsServlet.py, but the *SECOND* one
* Use `os.environ["PYWPS_PROCESSES"] = "/home/jachym/usr/src/pywpstutorial/processes/"`

http://localhost:8080/tmpwps/PywpsServlet.py?service=wps&request=getcapabilities

*Note the _tmpwps_ directory*

JavaScript
==========

WPS.js
------
* /var/www/wpstutorial/
* http://localhost/wpstutorial/wps.html

CCSS.WPS
--------

* http://briseide.localhost/map/index2.php

Requests
========

**OGR buffer**
    http://localhost/cgi-bin/wpstutorial?service=wps&version=1.0.0&request=execute&identifier=buffer&datainputs=size=10;data=http://apps.esdi-humboldt.cz/classification/traning_areas/training_areas_en.gml

**GRASS buffer**
    http://localhost/cgi-bin/wpstutorial?service=wps&version=1.0.0&request=execute&identifier=gbuffer&datainputs=size=10;data=http://apps.esdi-humboldt.cz/classification/traning_areas/training_areas_en.gml

**GRASS-PYTHON buffer**
    http://localhost/cgi-bin/wpstutorial?service=wps&version=1.0.0&request=execute&identifier=pgbuffer&datainputs=size=10;data=http://apps.esdi-humboldt.cz/classification/traning_areas/training_areas_en.gml

**GRASS-PYTHON buffer asReference (MapServer demo)**
    http://localhost/cgi-bin/wpstutorial?service=wps&version=1.0.0&request=execute&identifier=pgbuffer&datainputs=size=50;data=http://apps.esdi-humboldt.cz/classification/traning_areas/training_areas_en.gml&responsedocument=buffer=@asreference=true

Data
====
* http://apps.esdi-humboldt.cz/classification/traning_areas/training_areas_en.gml Krovak-JTSK
* http://localhost/wps/datainputs/

  * roads.gml - EPSG:3035
  * lakes.gml - Unknown

* /home/jachym/data/turisticke_mapy/jicinsko/rykot_kolo.shp




Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

