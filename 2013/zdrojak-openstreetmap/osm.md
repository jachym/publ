OpenStreetMap
=============

Motto projektu OpenStreetMap je "zmapujme svět!". Od roku 2004, kdy byl
projekt založen, udělal velký kus cesty. Co se za tu dobu stalo? Kam směřuje
projekt dnes? Jak ta data vůbec vznikají a dá se jim věřit? Jak ta data mohu
použít?

> Článek reaguje na starší text, který vyšel na [Zdrojáku v roce
> 2010](http://www.zdrojak.cz/clanky/api-k-ceskym-turistickym-mapam/). Za tu
> dobu se samozřejmě na trhu hodně změnilo, proto se nebudeme vracet k tomu,
> co bylo, ale zkusíme zmapovat co se aktuálně děje.

O OpenStreetMap
---------------
OpenStreetMap (OSM) je

> projekt zaměřený na vytváření svobodných geografických dat. U většiny
> ostatních volně dostupných map je ale užívání technicky a právně omezeno.
> Proto vznikl tento projekt, aby umožnil lidem volně nakládat s geografickými
> daty, používat je neobvyklými způsoby a v neposlední řadě, aby byla data
> dostupná v aktualizované a platné podobě bez dalších nákladů a omezení.
[OpenStreetMap](http://wiki.openstreetmap.org)

Rád říkám, že OSM má nejblíže k wikipedii - jde o kolektivní úsilí při tvorbě
sobodných dat a i v rámci OSM můžeme sledovat proces *wikizace* v tomto případě
- geodat. Analogicky s Wikipedií, tvůrci OSM (tzv. *mappeři*) tvoří buď v
oblasti která je baví, nebo kterou považují za nutnou. Vedle vysokého podílu
ruční práce existuje i neméně důležitá část automatizační-programátorská. I zde
známe války o - při pohledu z venčí - ne-zcela-podstatné věci, na štěstí je
komunita mapperů relativně kompatní a spory nebývají vyhrocené. 

Historie
--------
Projekt byl založen [Stevem Coastem](http://stevecoast.com) v roce 2004. 

TODO Obrázek

Dnes o devět let pozdějí (2013) má přes 1~000~000 přispěvatelů, 34~000~000
kilometrů silničních sítí, 78~000~000 zaznamenaných budov, globální komunitu,
firmy, které nabízejí OSM data komerčně a ekosystém projektů, které s daty z OSM
provádějí další kouzla [OSM DataReport
2013](https://www.mapbox.com/osm-data-report/).

Růst mapperů je v podstatě exponenciální, od roku 2004 stále, a stále rychleji,
stoupá, stejně jako objem dat. 

V roce 2005 proběhla první [mapping
party](http://wiki.openstreetmap.org/wiki/Map_Limehouse_Event_2005), a byl
registrovaný tisící mapper. 

V roce 2006 byla jednak vydána první stabilní verze editoru
[JOSM](http://wiki.openstreetmap.org/wiki/JOSM) (o kterém se ještě zmíníme) a
první verze [datového modelu](http://wiki.openstreetmap.org/wiki/Map_Features).
Byla publikována první verze online mapy, která je to, co většina uživatelů z
OSM vidí jako první.

První on-line editor vznikal v roce 2007 a mappeři se sešli na první konferenci
[state of the map](http://wiki.openstreetmap.org/wiki/State_Of_The_Map_2007),
data překročila 5~000~000 linií a 10~000 uživatelů. 

Daří se získávat další a další datové zdroje, nad kterými lze mapu vytvářet,
jako jsou [letecké snímky
[Yahoo!](http://wiki.openstreetmap.org/wiki/Yahoo!_aerial_imagery),
[Bing](http://wiki.openstreetmap.org/wiki/Bing) a další. 

Mezi nezásadnější zmeny patří změna licence TODO link v roce 2012, která bohužel
vedla ke ztrátě některých dat. Podařilo se je ale celkem rychle obnovit.

Organizace
----------

OpenStreetMap je podobně jako například Wikipidie formálně řízen [OpenStreetMap
Foundation](http://osmfoundation.org), která je registrována ve Spojeném
království, jako nezisková organizace. Individuálním členem se můžete stát za
15 liber, a můžete tak aktivně promluvit do dění v komunitě. Nadace má v tuto
chvíli okolo pěti set platících členů. 

V rámci nadace fungují pracovní skupiny, jako je pracovní skupina pro data,
vnitřní komunikaci, licenci, práci na softwarovém zázemí, konferenci State of
map a další.

Licence
-------

Licence OpenStreetMap má dvě části: Licence vlastních dat a licence generovaných
dlaždic - obrázků vyrenderovaných ze zdrojových dat OSM. Obrázky-dlaždice jsou
publikovány pod [Creative Commons - Uveďte autora-Zachovejte
licenci](http://creativecommons.org/licenses/by-sa/3.0/cz/). Dlaždice tedy
můžete sdílet a měnit jejich obsah, bez ohledu na to, jde-li o komerční nebo
nekomerční využití, za podmínky, že uvedete autora a odkaz na tuto licenci. V
praxi to znamená, že používáte-li dlaždice vygenerované službami OpenStreetMap,
[musíte uvézt odkaz](http://www.openstreetmap.org/copyright) s uvedením autorů
jako "© Přispěvatelé OpenStreetMap". To platí i pro například tištěné mapy, mapy
použité v médiích (např. v televizi) nebo hrách či mobilních aplikacích.

Vlastní data požívají [Open Data Commons Open Database License
(ODbl)](http://opendatacommons.org/licenses/odbl/). Data tak smíme

# kopírovat
# distribuovat
# upravovat

pokud jako zdroj uvedete OpenStreetMap a jeho přispěvatele. Pokud naše data
budete upravovat nebo je použijete ve svém díle, musíte výsledek šířit pod
stejnou licencí. 

V praxi to znamená, že za data nemusíte platit, a pokud provedete nějaké změny v
datech, můžete si je "nechat pro sebe", do té doby, než své odvozené dílo
začnete dále distribuovat. Potom musíte vaši nově odvozenou databázi nebo mapu
zpřístupnit. V ideálním případě svoje změny nahrajete zpátky do OSM databáze,
ale stačí, když je volně vystavíte. Pokud své odvozené dílo otevřeně nešíříte,
nemusíte se sdílením zdržovat.

Data jsou, jak už jsme napsali, zdarma ("free as a beer"), ale projekt lze
samozřejmě [podpořit i finančně](http://donate.openstreetmap.org/). Licence
neobsahuje žádná omezení stran komerčního nebo vědeckého využití. Komerční
využití je dokonce výslovně zmíněno v licenci a povoleno.

Data lze i prodávat. Pokud je od vás někdo koupí, může s nimi ale dále nakládat
za podmínek původní licence.

Aby to nebylo tak jednoduché, dlaždice nabízí i řada komerčních služeb a ty
samozřejmě mají svou vlastní licenci. Za všechny  bych jmenoval například
[MapBox](http://mapbox.com).

Jaká obsahuje data
------------------

OpenStreetMap se snaží o zmapování světa. Zaznamenávají se zejména objekty
lidské činnosti, jako jsou silnice, budovy, památníky a monumenty. Samozřemě se
zaznamenávají i přírodní útvary, jako jsou vodní nádrže, lesy (jejich obrysy),
geologické útvary a podobně.

[Datový model](http://wiki.openstreetmap.org/wiki/Map_Features) vychází zejména
ze situace, jaká je ve Spojeném království a ne
vždy se názvosloví a faktografie "potká" s tím, co známe u nás. Procesem
"harmonizace datových modelů" se zabývá nejeden evropský výzkumný projekt - zde
se o podobné snaží parta dobrovolníků. Ale i obráceně: některá [česká
specifika](http://wiki.openstreetmap.org/wiki/Cs:Map_Features)
nejsou v původním modelu zachycena a česká komunita tak musí trochu improvizovat
- za všechny zmiňme turistické značky Klubu českých turistů (více o nich dále).

Zachyceno může být všechno - od dálnice po pěšinu. Od sídla parlamentu po
patník. Od ocenánu po louži. Také atributy (vlastnosti) jednolitvých typů
objektů jsou velice podrobné. U silnici můžeme například nastavit její šířku,
maximální povolenou rychlost, směr - jedná-li se o jednosměrnou ulici, kvalitu
povrchu, sjízdost na kole (jakém), a podobně. U úřadu můžeme nastavit úřední
hodiny, a tak dále. 

V datovém modelu existuje dokonce možnost uložit výšku nad mořem - a to buď
pomocí bodu nebo pomocí uzavřeného polygonu. Tato data však zatím v (alespoň
české) OSM nejsou k dispozici.

Datový model
------------

Porovnání
---------
Google, seznam, here, bing

Jak začít s editací
-------------------

Jak pokračovat s editací
------------------------

Jak používat data a mapy
------------------------

Situace v České republice
-------------------------

Závěr
-----
