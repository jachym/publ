PyWPS
=====

PyWPS je projekt vyvíjený od roku 2006, jedná se o implementaci standardu OGC
WPS na straně serveru v jazyce Python. Stávající verze je vyvíjena pod licencí
GNU/GPL, nová verze pod licencí BSD

* Čím je výjimečný

Už jsem zmínil to, že PyWPS je vyvíjen v jazyce Python. Mezi ostatními
implementacemi vyniká především rychlostí instalace a konfigurace. Instalace
proběhne během několika minut. Psaní skriptů je také velice jednoduché. 

PyWPS obsahuje od začátku podporu pro skripty v GRASS GIS, uživatelé ale
zapojují celou řadu dalších knihoven, jako je GDAL/OGR, R.

* Proč přepsání

K tomu, že jsme začali pracovat na zcela nové verzi PyWPS nás vedlo několik
důvodů. V době, když jsme začali psát PyWPS - v roce 2006:

    * GRASS neměl žádné rozhraní pro jazyk python
    * Python 2.2 byla aktuální verze
    * Prakticky žádná podpora pro parserování XML souborů
    * Chyběly další knihovny pro práci s OGC
    * Nejúžívanější formát byl ESRI Shapfile, mluvilo se o GML, GeoTIFF

Dneska:

    * Python 3
    * GRASS má nativní vazbu do Pythonu, stejně jako další knihovny
    * Nové projekty lxml, owslib, werkzeug
    * Nové formáty - GeoJSON, TopoJSON (kde je dneska KML ...)

* Plány

Děláme na roadmap https://github.com/jachym/pywps-4/issues/milestones, která je
stále ve vývoji. Máme to rozděleno na PyWPS 4.0.0 a PyWPS 4.1.0 verze.

Do PyWPS 4.0.0 by mělo patřit:

    Co máme:
        Validators
        Server implementation based on werkzeug
        IOHandler
        File Storage

    Co bychom ještě rádi:
        ValuesReference enhancement
        WSDL/SOAP Support
        Interoperability
        PyWPS process chaining possible
        Database for basic logging
        Configuration
        Reading/Writing large XML files efficiently

Do PyWPS 4.1.0 by měly patřit nové vlastnosti:
    
    * Výstupy přes GeoServer, MapServer, QGIS Server
    * Administrativní RESTové rozhranní

* Co nás brzdí

    Nedostatek času. Momentálně nikdo nemá v popisu práce pracovat na PyWPS.
    Chybí nám sponzoři, dělníci. Něco se na obzoru vrbí, ale zatím nic
    konkrétního. Pro open source projekt jako je tento je nedostatek pracovníků
    kritický. Na aktuálním kódu pracují ve svém velice volném čase asi 3 lidi.

    Získali jsme jednoho studenta do Google Summer of Code Project - ve
    spolupráci s OSGeo.

* Sponzoři

    Intevation - Servery
    Help Service - Remote Sensing
    Deutsche Bundesstiftung Umwelt

* Závěr


