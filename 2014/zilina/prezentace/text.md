Jmenuji se Jáchym Čepický a původním vzděláním jsem lesník. Tématem mojí
přednášky je vše otevřené, co se nějakým způsobem týká geo věděd - GIS,
geomatika, geoinformatika, zkrátka mapy v počítači.

Jsem
bývalým členem GRASS Development teamu, původní autor programu PyWPS,
přispěvatel do několika dalších projektů, jako jsou například OpenLayers a
uživatel a propagátor otevřeného software pro geooblast.

Mezi neprogramátorské aktivity patří zejména členství v představuje
představenstvu Open Source Geospatial Foundation a jsem předseda českého
sdružení Otevřená geoinfrastruktura.

Posledních 6 let se zábavám především vývojem webových mapových aplikací pomocí
různých frameworků a o svoje zkušenosti bych se s vámi dnes rád podělil.
Více než deset let se zabývám vývojem open source software
pro geoinformatiku. Úzce s tím souvisí i to, že trochu déle se počítám mezi
uživatele operačního systému GNU/Linux. To obyčejně nepovažuji za důležité
zmiňovat, ale v kontextu této přednášky to považuji za významnou skutečnost.

Během studií jsem u svého kamaráda našel v jeho knihovničce knížku Učíme se Red Hat Linux
a při jejím čtení mi došlo, že vedle počítačů jak je znám existuje jiný
svět, který bych rád poznal. V té době pro mě počítač bylo PC s MS Windows 98,
používal jsem Excel na tvorbu protokolů a prací pro svůj obor (kterým bylo lesní
inženýrství). Nikdy jsem neměl ambici programovat, počítače jsem chápal jako
nástroje, které by mi měli v ideálním případě usnadnit práci. V knížce jsem se
seznámil se základními ideemi open source a free software a byly mi sympatické,
jakkoliv jsem nedokázal pochopit, proč by někdo sdílel svoji práci --
intelektuální vlastnictví -- s kýmkoliv jiným. Když se mi v krátké době podařilo
pořídit si svůj vlastní nový počítač, požádal jsem kamaráda o pomoc
nainstalovali jsme můj první Linux. 

Od té doby jsem se stal uživatelem open source a free software a postupem času i
jeho spolutvůrcem. Naučil jsem se, jak funguje komunita uživatelů a přispěvatelů
do open source software, pochopil jsem některé jemné rozdíly mezi svobodným
software a otevřeným software a tak dále. A dnes chápu, že open source, nebo
obecně tak zvaný crowd source -- sdílený přístup -- není žádná anomálie.

Většina z vás už určitě slyšela o tom, že hnutí free software založil Richard
Matthew Stallman v 80.~letech minulého století prací na operačním systému GNU.
Definoval tři základní svobody nebo práva, které by měl každý uživatel software
mít: právo vidět zdrojový kód, právo sdílet zdrojový kód a právo měnit zdrojový
kód a dále ho sdílet.

V systém se stal úspěšný také díky jádru operačního systému Linux. Dnes je Linux
nejpoužívanějším serverovým operačním systémem, používá se v mobilních
zařízeních, na super počítačích. Proč se tak stalo? Stalo se tak především díky
použité licenci - GNU/GPL. Díky ní se "Linux" stal otevřeným systémem
-- systém, ve kterém ostatní sdílí svůj kód -- svoje know-how -- svoje
 intelektuální vlastnictví s ostatními.

Ale koncept sdílení není přece vynalezen v 80 letech. Západní věda tak jak ji
chápeme je snad od dob antiky postavena na stejných principech: publikuji
výsledek způsobem, že je opakovatelný, očekávám, že někdo jiný mou práci
zopakuje, přezkouší její platnost, případně navrhne některé změny, a výsledek
opět publikuje. Vědecká komunita díky sdílení informací posouvá hranice našeho
poznání dále, stejně jako komunita vývojářská posouvá hranice software.

Open source software není jediný příklad pro fungující intelektuální
spoluvlastnictví. Nikdo snad nepochybuje, že wikipedia je spolehlivý informační
zdroj a přitom na její obsah nemá nikdo monopol, neexistuje globální autorita,
která by strážila věcný obsah Wikipedie. OpenStreetMap je podle mě další
úspěšný projekt. Jako geoprostoroví profesionálové můžete zpochybňovat polohovou
přesnost dat, jejich faktickou správnost nebo aktuálnost, ale nemůžete
zpochybnit, že globálně vzato je to ucelený dataset který nemá v prorietárním
světe obdoby.

Všechny tyto příklady mají díky svým licencím společné tři základní vlastnosti,
které vyzývají další a další uživatele aby se přidali: vidět obsah, sdílet obsah
a provádět změny v obsahu a sdílet tyto změny dál.

A kromě licencí, které umožňují sdílet myšlenky bezestrachu, že by se je někdo
pokoušel uzavřít ... doufám, že i vám je ze sousloví "uzavřít myšlenky" poněkud
chladno ... byl úspěch všech těchto projektů podmíněn ještě jedním důležitým
aspetktem, a to je jednoduché spojení velkého množství lidí na stejné úrovni. Je
to díky síti Internet, který je technologicky a většinou i politicky a sociálně
neutrální. Díky této síle může vznikat opravdu něco, z ničeho.

Spojte lidi, dejte jim tu správnou licenci a stane se kouzlo, přesto ... tak
jednoduché to je.

Tím se dostáváme od obecného ke konkrétnímu - k geoinformatice a k otevřeným
datům. 

Víte že většina
geodat v České republice je vytvářena a spravována českým úřadem zeměměřičským a
katastrálním. Katastrální mapa katastrálním úřadem, základní mapa zaměměřičským
úřadem, kteří do určité míry fungují na sobě nezávisle. Pokud potřebujete
například  polohopisnou mapu Základní báze geografických dat, tak si ji musíte
koupit, protože tyto data mají výjimku z výjimky autorského zákona. Autorský
zákon v České republice explicitně říká, že veškerá úřední díla jím nejsou
chráněna. Co je ale základní mapa jiného, než úřední dílo? Vzniká za státní
peníze, spravuje ji státní instituce ... proč ta data nemůžeme volně používat?
Ta data si můžete koupit. Česká republika jako celek vás vyjde na bratru 4
miliony korun, ale myslím, že byste dostali množstevní slevu 10%. Celkem: 3 726
925 Kč Ortofoto by vás vyšlo na Celkem: 2 366 501 Kč

Samozřejmě můžete používat mapy komerčních firem, ty jsou levnější (i když data
vám nikdo nenabídne, maxilně obrázky v podobě dlaždic) a dokonce můžete tato
data pomocí nástrojů pomáhat vylepšit a funguje to, sám jsem si to zkusil.
Nevím, jestli  jste to někdy udělali, ale nemáte pocit, že ten vztah je trochu
nevyvážený? Vy opravítě pokladová data a vaši práci, vaše intelektuální
vlastnictví, použije nějaká firma pro vylepšení své roční bilance?

V roce 2007 ale začal malý universitní projekt jménem OpenStreetMap, který měl
za cíl vytvořit společné intelektuální vlastnictví geodat. Tento projekt je
velice úspěšný, protože zaplnil poptávku, hlad po dobrých geodatech nebo po
geodatech, která jsou "dostatečně dobrá". Jejich licence umožňuje data sdílet,
měnit a opět sdílet. Na internetu můžete najít celou řadu konkrétních srovnání
mezi různými službami, jako je Google, Bing maps nebo Nokia mapy a
OpenStreetMap, kdy OpenStreetMap vyjde jako zdroj s nejlepším pokrytím. V České
republice někdy vychází lépe OpenStreetMap, někdy komerční mapy. Co je ale
podstatné: Existuje datový zdroj, otevřený datový zdroj, který nabízí data pro
vaše použití. Ne jen předgenerované dlaždice - obrázky, ale původní data se
vším, co se do dlaždic nevešlo. A ta data jsou pro řadu aplikací dostatečně
kvalitní. Projekt, který při pohledu z venčí dělá pár bláznů s GPSkami je
nebojím se to říci veleúspěšný a zdatně konkuruje komerčním projektům, za
kterými stojí finančí kapitál nebo státní peníze. Ten projekt vzniknul z
potřeby, z nedostatku legálních dat. Kdyby existovala dostupná otevřená geodata,
pravděpodobně by nikdy nebyl potřeba. Pokud potřebujete data přes celou
republiku, neřku-li Evropu, víte kam sáhnout.  Nastávají z mého pohledu absurdní
situace, kdy veřejné instituce, než aby řešili licence a nákup a poskytování dat
s pověřenou osobou (jako příklad můžeme vzít právě český zěměměřicský úřad),
raději použijí OpenStreetMap pro své interní potřeby. 

Jiný příklad z oboru: Firma Mapillary začala sbírat na svých serverech
fotografie pořízené mobilními telefony. Cíl má nemalý: porazit službu Google
Street View. Jenomže moc to nefunguovalo, až když před nedávnem změnili licenci
    z Creative Commons Non Commercial use na CC-Share-Alike
Přesně ... proč bych jim měl pomáhat s fotkama, když mě potom omezují v jejich
použití? Ale CC-SA, to už je jiné kafe! Lidi začali přispívat a fotek utěšeně
přibývá.

Abych tuto část nějak uzavřel: Open Source software je jenom jedna část tohoto
způsobu vytváření společné znalostní báze. Ale stejným způsobem pracuje
Wikipedia nebo OpenStreetMap a další komunity. Komunity spojené internetem
vytvářejí hodnoty, pro jejichž vytvoření byly dříve potřeba velké instituce.

Open Source software a otevřený způsob spolupráce není nějaké náboženství. Je to
prostě normální. Lidé spolu sdíleli svoje znalosti v minulosti a dělají tak i v
současnosti. Otevřenost je norma. Open Source software je všude kolem nás.
Google by nebyl čím je bez tisíců linuxových serverů, na kterých běží. Facebook
by neexistoval ze stejného důvodu. Android používá linuxové jádro. Tyto úspěšné
firmy nejen že používají Open Source (v případě Facebooku např. MySQL, PHP,
samozřejmě také Linux), ale sami jej aktivně vytváří -- Google mimo jiné
prohlížeč Chromium, javascriptovou knihovnu Closure, Facebook úspěšný
šablonovací systém React nebo nosql databázi Cassandra. Většina vašich routrů
doma používá Open Source.

Nyní tedy k více konkrétnímu. Už jsem říkal, že jsem člen představenstva Open
Source Geospatial Foundation. Co to je?

OSGeo sdružení registrované ve spojených státech s mezinárodní členskou
komunitou (v tuto chvíli je nás cca 180). OSGeo má různé aktivity, ale je
potřebné zdůraznit, že se jedná o dobrovolnickou organizaci. Kromě 9 členů
představenstva má ještě prezidenta, kterým je v současnosti Jeff McKenna.
Jednou z nejvýraznější akcí je pořádání konference Foss4G, která má i svoji
evropskou verzi, letos v německých Brémách.

OSGeo funguje také jako zastřešující organizace a certifikační autorita pro tzv.
OSGeo projekty. Evaluačními kritérii jsou velikost a aktivitu komunity, kvalitu
zdrojového kódu, rozhodovací procesy v komunitě atd atd. Je-li nějaký projekt
OSGeo-projekt, znamená to, že je stabilní a kvalitní a opravdu nezahyne příští
rok.

Pokusím se z rychlíku vám dodat přehled toho nejzajímavějšího, co open source
svět pro geoinformatiku nabízí. Seznam si nedělá cíl být kompletní, jsou to
mnou preferované a vybrané programy a více určitě naleznete na stránkách
OSGeo.org nebo na stránkách Google.com:

Je jen málo oblastí geoinformatiky, které by nebyly pokryty kvalitním open
source software -- i když připouštím, že jsou. Stále vznikají nové programy pro
další oblasti, staré ozkoušené projekty jsou ale stále zde, stabilní, s
rozšířenou vývojářskou a uživatelskou komunitou, stále dostávají nové funkce, ty
staré jsou oprašovány a udržovány.


Desktop:

QGIS je destkopová prohlížečka geodat, která se postupně mění na plnkrevný GIS,
včetně serverové části. Obsahuje mnoho  zásuvných modulů, které jeho funkce
ještě rozšiřují.

GRASS GIS je projekt vyvíjený od roku 1982 a měl jsem tu čest být členem jeho
vývojového teamu. GRASS je GIS obsahující na 500 modulů pro práci s rastrovými i
vektorovými daty. Unese analyzovat opravdu velké množství dat, lze ho spouštět
pomocí skriptů (momentálně mi na cloudové platformě Microsoft Azure běží už
druhý týden výpočet některých analýz v Praze). Čím je mezi programy pro psaní
textů LaTeX, tím je mezi GISy GRASS.

Server:
MapServer je opět velice starý projekt, který dělá to, jak se jmenuje: vydává
klientům požadovaná geodata podle požadovanvaných parametrů. MapServer obsahuje
rozhraní MapScript, takže jej lze dost modifikovat pomocí různých skriptovacích
jazyků.

GeoServer je v Javě napsaný mapový server, striktně dodržující standardy. Na
rozdíl od MapServeru disponuje webovým grafickým rozhraním. Lze jej do jisté
míry také programátorsky přizpůsobit, děje se tak ale pomocí REST API, a ne na
úrovni programátorských knihoven.

Web:
OpenLayers je javascriptová knihovna pro tvorbu mapových aplikací. Je to opravdu
švýcarský nůž, který obsahuje podporu pro všechny myslitelné datové formáty. V
tuto chvíli probíhá přepisování této knihovny na novou verzi pomocí nových
technologií, jako je Google Closure.

Knihovny:
GDAL/OGR je knihovna schopná převézt nepřeberné množství rastrových na
vektorových formátů mezi sebou. Je používána i v proprietárním software ArcGIS.

Knihovna PROJ.4 zase umí pracovat s různými mapovými projekcemi a souř. systémy.

GeoTools dělá to samé pro programovací jazyk Java.

Existuje i řada projektů mimo OSGeo. Mají svou vývojářkou a uživatelskou
komunitu. Asi jste slyšeli o projektu Leaflet, gvSig (ten je v OSGeo
inkubárotru), knihovně D3js pro vykreslování dat na webu.

Řekněte, jaká problematika vás zajímá a já vám řeknu, co bych na to použil. A
nebo ne.

Může se stát, že na váš úkol neexistuje Open Source odpověď. V tom případě máte
dvě možnosti: zvažte, jestli je ve vašich silách jakkoliv přispět do
existujícího projektu nebo vytvořit nový - je to tak snadné. Nebo jděte do
proprietárního software. Buďte si ale vždy vědomi, proč to děláte a co tím
ztrácíte.

Z toho všeho co říkám si možná říkáte: proč to tedy nikdo nepoužívá, když je to
tak skvělý produkt? Proč není open source software dávno rozšířenější, než jak
to vypadá?

Důvody pro tento stav -- a je jedno jestli je to objektivní fakt nebo subjektivní
pocit -- jsou samozřejmě mnohé a jak už to bývá, mají povahu vnitřní i vnější.

Jako jeden z prvních důvodů (bez nároku na prvenství z hlediska významnosti)
uvedu to, že člověk používá to, co zná. Věřím, že obsahem výuky na
školách ve všech oborech a stupních by měly být především obecně platné
principy, až od nich odvozené konkrétní situace. Učíme obecně Archimedův zákon,
a teprve následně několik jeho praktických aplikací, jako že ve vodě je slon
lehčí nebo spolu s inženýry španělského námořnictva, že ponorka, má-li se vynořit,
musí mít především v součtu menší objemovou hustotu, než voda. Proč se ale tento
princip uplatňuje při výuce software jen velice zřídka? Proč výuka počítačí
obecně a GIS konkrétně se téměř bez výjimky provádí na konkrétním jednom
software?

Dalším důvodem je neexistence jednotného telefonního čísla -- chybí marketingové
oddělení open source GIS, není tu někdo, kdo by zákazníkům vysvětlil proč je
konkrétní produkt ten nejlepší (v absolutním i relativním významu). U open source
software se předpokládá, že jste dospělí, že jste nebo se chcete stát experty a
proto na to, co je pro váš případ to nejlepší si přijdete sami. Open source je
náročný na lidské zdroje, pokud nemáte u sebe někoho dalšího, jste v tom tak
trochu sami, ,,jenom`` s podporou komunity. To může hodně lidí odradit, ale
bylo mnohokrát  ilustrováno, že podpora komunity funguje, první odpověď v mailing
listech bývá u větších projektů v řádu minut.

Dalším důvodem bude roztříštěná nabídka open source software. Jak jsem řekl
dříve, nemáte se moc koho zeptat a ještě ke všemu si musíte vybírat z množství
variant -- sám s tím mám často problém. Provozní výzkum, porovnávání různých
programů a sledování nových je denní chléb. Mám vzít TileCache, MapStach,
GeoServer cache, MapCache? A co je to ten Mapnik? A jaký je rozdíl mezi Leaflet
a OpenLayers? Na tyto otázky získáte nejlépe odpověď tak, že budete číst nebo se
zeptáte někoho, kdo to ví, ale jak jsem již řekl -- ve vašem okolí je většinou
problém najít někoho kdo by to věděl. Nebo snad ne?

Dalším důvodem je nejednotný systém návazného vzdělávání. Existují spíše
jednotlivci, nabízející školení. Školení jsou ale nejednotná, různá obsahem i
kvalitou.

Otevřený svět Geo* má kromě dvou již zmíněných částí -- totiž Open Data a Open
Source Software ještě jednu důležitou část, a tou je Open Standards. Tu pro nás
zajištuje organizace Open Geospatial Consorcium.

OGC je mezinárodní standardizační organizace pro Geo* doménu. Standardizuje
formáty a služby. Její standardy jsou vždy a zásadně otevřené a hlavně, široce
akceptované vývojářskou a uživatelksou komunitou. Možná jste slyšeli o službách
OGC WMS, WFS, WCS nebo WPS a CSW. Tyto služby vám umožňují stahovat mapy,
vektorová a rastrová data, spouštět výpočty  na serverech (nebo jak se dnes
říká, v cloudu) nebo vyhledávat data služby po celém světě. Zdá se vám to příliš
abstraktní?

V roce 2007 byla evropskou komisí schválena směrnice INSPIRE, která (velice
zjednodušeně řečeno) popisuje způsob, jakým má veřejná správa umožnit přístup k
datům (nejen, ale zejména) o životním prostředí. Směrnice neříká nic o tom za
jakých právních a finančních podmínek mají být data zveřejněna - nejedná se o
Open Data. Řeší ale technickou a obsahovou stránku věci a ve svých pravidelch
pro implementaci se důrazně opírá právě o standardy OGC.

Takže: ve své přednášce jsem mluvil o Open Source, Open Data, Open Standards pro
doménu Geo. Proč jsou skvělé a snad i proč nefungují. Už i u nás a u vás na
Slovensku existují firmy, které nabízejí profesionální služby v této doméně.
Také díky velké finančních krizi posledních let se daří stále častěji firmám z
open soure světa prorážet na komerčním poli.

Myslím, že i vzhledem k tomu kolik Slovenských vývojářů se pohybuje na open
source GIS scéně, má Slovensko a snad i Česko světlou geo-budoucnost.
