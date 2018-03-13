

```python
# Unit 6 | Assignment - What's the Weather Like?

# Dependencies
import csv
import json
from citipy import citipy
import numpy as np
import matplotlib.pyplot as plt
import requests as req
import pandas as pd
from config import api_key
import random
%matplotlib inline
```


```python
# Save config information.
url = "http://api.openweathermap.org/data/2.5/weather?"
units = "metric"

# Build partial query URL
#query_url = "{url}appid={api_key}&units={units}&q="
query_url = "%sappid=%s&units=%s&q="%(url, api_key, units)
#query_url
```


```python
# Perform a weather check on each of the cities using a series of successive API calls.
# Include a print log of each city as it's being processed with the city number, city name, and requested URL.
# Save both a CSV of all data retrieved and png images for each scatter plot.

# play with citipy!
# city = citipy.nearest_city(40.6936, -89.5890)
# print(city.city_name)
# print(city.country_code)
```


```python
# Randomly select at least 500 unique (non-repeat) cities based on latitude and longitude.
# Generate a list of at least 500 random, unique cities

# since citipy won't grab 500 cities at a time, i will loop thru 15 times
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
CandidateCityList = []

for number in numbers:
    # Generate random lattitudes from -90 to 90
    # create a list of random lattitudes
    ListLength = 100
    LatList = random.sample(list(range(-90,90)),ListLength)
    LonList = random.sample(list(range(-180,180)),ListLength)
    #print(LatList)
    #print(LonList)

    # Loop & append
    # Loop through the list of cities and perform a request for data on each
    i = 0
    for i in range(0, len(LatList)):
        TestCity = citipy.nearest_city(LatList[i], LonList[i])
        CandidateCityList.append(TestCity.city_name) 

#print(CandidateCityList)
print(len(CandidateCityList))
# clean up dups
FinalCityList = list(set(CandidateCityList))
print(FinalCityList)
print(len(FinalCityList))

```

    1500
    ['santa rosa', 'upernavik', 'swellendam', 'kasangulu', 'purwodadi', 'taltal', 'mys shmidta', 'bluff', 'petropavlovsk-kamchatskiy', 'rongcheng', 'sakakah', 'sorsk', 'caravelas', 'kulhudhuffushi', 'marzuq', 'colac', 'otautau', 'agirish', 'te anau', 'mangrol', 'hami', 'inuvik', 'ushuaia', 'genhe', 'nizhneyansk', 'malwan', 'altay', 'manosque', 'stokmarknes', 'athabasca', 'barahan', 'bull savanna', 'butaritari', 'stantsiya gorchakovo', 'tungor', 'lebu', 'namibe', 'barcelona', 'ouegoa', 'haines junction', 'rawson', 'tukrah', 'jinchang', 'nguiu', 'kieta', 'longlac', 'merauke', 'ust-maya', 'bathurst', 'luderitz', 'rostovka', 'katherine', 'peresichna', 'saleaula', 'cascais', 'chicontepec', 'biak', 'yertsevo', 'karkaralinsk', 'aklavik', 'zyryanka', 'balikpapan', 'sitka', 'vila franca do campo', 'geresk', 'konstancin-jeziorna', 'osorheiu', 'ayagoz', 'de-kastri', 'okhotsk', 'yellowknife', 'phan thiet', 'kamenka', 'sentyabrskiy', 'voyvozh', 'zima', 'luganville', 'grajau', 'palmer', 'richards bay', 'tabiauea', 'chauk', 'atar', 'junin', 'lavrentiya', 'mangai', 'iquitos', 'banjar', 'gualaco', 'new norfolk', 'preobrazheniye', 'codrington', 'fuxin', 'port hedland', 'samusu', 'saryshagan', 'pevek', 'krutinka', 'kutum', 'jimma', 'kroya', 'tsihombe', 'rastolita', 'gerash', 'pisco', 'srivardhan', 'mahebourg', 'gondanglegi', 'kuching', 'tilichiki', 'bosaso', 'dabola', 'alice springs', 'portpatrick', 'dikson', 'umzimvubu', 'kuusamo', 'goderich', 'hilo', 'victoria', 'bochil', 'meulaboh', 'whitehorse', 'san rafael', 'borodino', 'deputatskiy', 'benidorm', 'athens', 'khasan', 'igarka', 'kez', 'klaksvik', 'koungou', 'winnemucca', 'lahaina', 'yelandur', 'canala', 'linhares', 'hualmay', 'luau', 'meylan', 'avarua', 'batesville', 'arlit', 'cherskiy', 'sao filipe', 'kaitangata', 'praia da vitoria', 'khani', 'batken', 'hamilton', 'nicolas bravo', 'la ronge', 'tarakan', 'annau', 'baruun-urt', 'zeya', 'tunceli', 'sarangani', 'dolbeau', 'bumba', 'santa cruz', 'padang', 'shiyan', 'mount isa', 'wajima', 'poso', 'west wendover', 'palazzolo acreide', 'virden', 'batemans bay', 'kindu', 'mar del plata', 'namatanai', 'punta arenas', 'saint-francois', 'ganzhou', 'chokurdakh', 'misratah', 'goryachegorsk', 'pacific grove', 'saint anthony', 'warwick', 'am timan', 'albacete', 'mount gambier', 'broken hill', 'mitzic', 'hithadhoo', 'neftcala', 'turayf', 'uvalde', 'halvad', 'severo-kurilsk', 'east london', 'aztec', 'keuruu', 'poum', 'sistranda', 'medea', 'port keats', 'olafsvik', 'san juan de colon', 'hargeysa', 'alyangula', 'port blair', 'ballina', 'hangu', 'san quintin', 'avera', 'almaznyy', 'iqaluit', 'walvis bay', 'kuala selangor', 'viedma', 'bethel', 'calama', 'kirovsk', 'chabahar', 'baiyin', 'cap-aux-meules', 'hofn', 'busselton', 'faya', 'borogontsy', 'kamaishi', 'muros', 'carnarvon', 'tambovka', 'castro', 'lyaskelya', 'ayna', 'kingsport', 'tuktoyaktuk', 'payo', 'kahului', 'sorland', 'fort abbas', 'sol-iletsk', 'valkeakoski', 'den chai', 'bloemfontein', 'rikitea', 'adrar', 'saint george', 'nha trang', 'geraldton', 'londoko', 'itarema', 'thinadhoo', 'kamina', 'barrow', 'nome', 'cacu', 'muleba', 'korhogo', 'namanyere', 'guderup', 'warqla', 'blagoveshchensk', 'christchurch', 'wulanhaote', 'norman wells', 'belyy yar', 'airai', 'saint-malo', 'aksarka', 'nara', 'zalantun', 'barbar', 'tura', 'plettenberg bay', 'cayenne', 'temaraia', 'olbia', 'dingle', 'kibuye', 'srandakan', 'ribeira grande', 'mahina', 'dossor', 'torbay', 'kaoma', 'lang suan', 'maragogi', 'caraquet', 'juba', 'ozgon', 'baixa grande', 'carauari', 'msanga', 'bandarbeyla', 'lorengau', 'lumajang', 'tagusao', 'khormuj', 'gamba', 'leh', 'barcelos', 'sur', 'aguada de pasajeros', 'trelew', 'tubmanburg', 'finschhafen', 'litovko', 'koslan', 'tateyama', 'baker city', 'qaanaaq', 'gornja koprivna', 'luanda', 'yarmouth', 'basoko', 'bafq', 'byron bay', 'bemidji', 'kanker', 'male', 'port elizabeth', 'praxedis guerrero', 'zhigansk', 'fujin', 'coihaique', 'zhanaozen', 'rio cuarto', 'barra do garcas', 'grindavik', 'phangnga', 'venado tuerto', 'qeshm', 'vaitupu', 'bilibino', 'luena', 'saquena', 'shenjiamen', 'lipin bor', 'payson', 'alofi', 'alihe', 'xiaolingwei', 'winchester', 'puerto madryn', 'madison', 'guerrero negro', 'grand gaube', 'russkaya polyana', 'vardo', 'port perry', 'tidore', 'noyabrsk', 'clyde river', 'hasaki', 'arraial do cabo', 'lauria', 'torzhok', 'anadyr', 'bogovina', 'krutikha', 'grootfontein', 'auki', 'baghdad', 'ruatoria', 'gillette', 'porto novo', 'oussouye', 'saldanha', 'faanui', 'sisimiut', 'maningrida', 'eenhana', 'narsaq', 'broome', 'newport', 'yomitan', 'inhambane', 'noshiro', 'santa maria', 'wanaka', 'atuona', 'lompoc', 'puerto ayora', 'waling', 'mackenzie', 'constitucion', 'wenchi', 'barentsburg', 'awallan', 'port-gentil', 'maracacume', 'perene', 'micheweni', 'methoni', 'nikolskoye', 'waipawa', 'mayor pablo lagerenza', 'skibotn', 'souillac', 'leningradskiy', 'dunedin', 'nantucket', 'chitipa', 'mao', 'korla', 'point fortin', 'tiksi', 'kodiak', 'mehamn', 'jamestown', 'sterling', 'pangnirtung', 'vestmannaeyjar', 'nyurba', 'poykovskiy', 'puri', 'cabedelo', 'yilan', 'cefalu', 'aykhal', 'rocha', 'concepcion', 'georgetown', 'ciras', 'paros', 'vaini', 'prabumulih', 'bowen', 'hervey bay', 'northam', 'sola', 'krasnovishersk', 'puerto escondido', 'tumannyy', 'kavaratti', 'saleilua', 'kruisfontein', 'kavieng', 'thompson', 'half moon bay', 'gorno-altaysk', 'sibolga', 'maniitsoq', 'coquimbo', 'seoul', 'debre tabor', 'rocky mountain house', 'naze', 'mangit', 'ust-omchug', 'sabang', 'carthage', 'quatre cocos', 'lixourion', 'kegayli', 'saint-jean-port-joli', 'ilulissat', 'usinsk', 'raudeberg', 'khatanga', 'ambon', 'safonovo', 'padre bernardo', 'balila', 'lucapa', 'varhaug', 'taolanaro', 'nurota', 'longyearbyen', 'astipalaia', 'innisfail', 'provideniya', 'talaya', 'mataura', 'beidao', 'dapaong', 'ust-tsilma', 'calabozo', 'sioux lookout', 'bredasdorp', 'road town', 'mayo', 'novomykolayivka', 'tashtyp', 'buala', 'kupang', 'masallatah', 'esil', 'takaka', 'tomatlan', 'mackay', 'hebi', 'sawakin', 'bathsheba', 'clarence town', 'andra', 'angouleme', 'lolua', 'kailua', 'bengkulu', 'salina cruz', 'belushya guba', 'nova olimpia', 'hobart', 'korablino', 'carbonear', 'de aar', 'comodoro rivadavia', 'acajutla', 'cabo san lucas', 'uruacu', 'vao', 'champasak', 'gat', 'malacacheta', 'manta', 'kapaa', 'denpasar', 'tasiilaq', 'amderma', 'severo-yeniseyskiy', 'puerto del rosario', 'katsuura', 'dafeng', 'trincomalee', 'ponta do sol', 'cidreira', 'longkou', 'huarmey', 'kapoeta', 'kungurtug', 'fort nelson', 'tarauaca', 'sherpur', 'manado', 'mahaicony', 'presidencia roque saenz pena', 'kilosa', 'tabou', 'jiuquan', 'sumbe', 'safaga', 'klaebu', 'fairbanks', 'khagrachari', 'gorontalo', 'eureka', 'dubbo', 'davila', 'beringovskiy', 'otaru', 'shimoda', 'chimore', 'challans', 'hermanus', 'saint-philippe', 'abidjan', 'chuy', 'albany', 'leshan', 'lukhovitsy', 'grand river south east', 'acari', 'aswan', 'isagarh', 'bambous virieux', 'hovd', 'cururupu', 'gairo', 'marcona', 'lac du bonnet', 'okha', 'ladwa', 'xudat', 'sidi ali', 'illoqqortoormiut', 'yulara', 'tuatapere', 'bur gabo', 'isiro', 'port augusta', 'cape town', 'badarganj', 'ostersund', 'uyuni', 'sotnikovskoye', 'saint-augustin', 'jacmel', 'borovoy', 'imeni poliny osipenko', 'colombo', 'malartic', 'khash', 'tartus', 'bud', 'nizhnyaya salda', 'morros', 'lagoa', 'los llanos de aridane', 'wewak', 'roswell', 'talnakh', 'ahipara', 'axim', 'vestmanna', 'moussoro', 'san patricio', 'attawapiskat', 'viseu', 'saskylakh', 'port lincoln', 'olovyannaya', 'hambantota', 'port alfred', 'esperance', 'bonavista', 'bolobo']
    615
    


```python
# play with the weather API
# Save config information
current_city = "Peoria"
#current_city = "belushya guba"
# Build query URL
current_url = query_url + current_city
#current_url
response = req.get(current_url).json() # returns a dictionary?
response.keys()                # keys from the dictionary 
#print(json.dumps(response, indent = 4, sort_keys = True))

```




    dict_keys(['coord', 'weather', 'base', 'main', 'visibility', 'wind', 'clouds', 'dt', 'sys', 'id', 'name', 'cod'])




```python
# Perform API calls
#TestCityList = ['peoria', 'paris', 'moscow', 'cape town', 'mumbai', 'london', 'seattle']
TestCityList = FinalCityList

# set up lists to hold reponse info
cityname = []
cloudiness = []
country = []
lat = []
lng = []
date = []
humidity = []
lat = []
lng = []
maxtemp = []
windspeed = []

# Loop & append
CityNbr = 0
# Loop through the list of cities and perform a request for data on each
for city in TestCityList:
    response = req.get(query_url + city).json()
    try:
        print('Looking for:  '+ str(CityNbr) + ' ' + city)
        print(query_url + city)
        cityname.append(response['name'])
        cloudiness.append(response['clouds']['all'])
        country.append(response['sys']['country'])
        date.append(response['dt'])
        humidity.append(response['main']['humidity'])
        lat.append(response['coord']['lat'])
        lng.append(response['coord']['lon'])
        maxtemp.append(response['main']['temp_max'])
        windspeed.append(response['wind']['speed'])
        CityNbr = CityNbr + 1
    except:
        print('Looking for:  '+ city + ' not found')
# print("City Names: %s"%(cityname))
# print("The latitude information received is: %s"%(lat))
# print("The temperature information received is: %s"%(maxtemp))

```

    Looking for:  0 santa rosa
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=santa rosa
    Looking for:  1 upernavik
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=upernavik
    Looking for:  2 swellendam
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=swellendam
    Looking for:  3 kasangulu
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kasangulu
    Looking for:  4 purwodadi
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=purwodadi
    Looking for:  5 taltal
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=taltal
    Looking for:  6 mys shmidta
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=mys shmidta
    Looking for:  mys shmidta not found
    Looking for:  6 bluff
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=bluff
    Looking for:  7 petropavlovsk-kamchatskiy
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=petropavlovsk-kamchatskiy
    Looking for:  8 rongcheng
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=rongcheng
    Looking for:  9 sakakah
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=sakakah
    Looking for:  sakakah not found
    Looking for:  9 sorsk
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=sorsk
    Looking for:  10 caravelas
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=caravelas
    Looking for:  11 kulhudhuffushi
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kulhudhuffushi
    Looking for:  12 marzuq
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=marzuq
    Looking for:  13 colac
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=colac
    Looking for:  14 otautau
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=otautau
    Looking for:  15 agirish
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=agirish
    Looking for:  16 te anau
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=te anau
    Looking for:  17 mangrol
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=mangrol
    Looking for:  18 hami
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=hami
    Looking for:  19 inuvik
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=inuvik
    Looking for:  20 ushuaia
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=ushuaia
    Looking for:  21 genhe
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=genhe
    Looking for:  22 nizhneyansk
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=nizhneyansk
    Looking for:  nizhneyansk not found
    Looking for:  22 malwan
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=malwan
    Looking for:  malwan not found
    Looking for:  22 altay
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=altay
    Looking for:  23 manosque
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=manosque
    Looking for:  24 stokmarknes
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=stokmarknes
    Looking for:  25 athabasca
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=athabasca
    Looking for:  26 barahan
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=barahan
    Looking for:  27 bull savanna
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=bull savanna
    Looking for:  28 butaritari
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=butaritari
    Looking for:  29 stantsiya gorchakovo
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=stantsiya gorchakovo
    Looking for:  stantsiya gorchakovo not found
    Looking for:  29 tungor
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=tungor
    Looking for:  30 lebu
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=lebu
    Looking for:  31 namibe
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=namibe
    Looking for:  32 barcelona
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=barcelona
    Looking for:  33 ouegoa
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=ouegoa
    Looking for:  34 haines junction
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=haines junction
    Looking for:  35 rawson
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=rawson
    Looking for:  36 tukrah
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=tukrah
    Looking for:  tukrah not found
    Looking for:  36 jinchang
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=jinchang
    Looking for:  37 nguiu
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=nguiu
    Looking for:  nguiu not found
    Looking for:  37 kieta
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kieta
    Looking for:  38 longlac
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=longlac
    Looking for:  longlac not found
    Looking for:  38 merauke
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=merauke
    Looking for:  39 ust-maya
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=ust-maya
    Looking for:  40 bathurst
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=bathurst
    Looking for:  41 luderitz
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=luderitz
    Looking for:  42 rostovka
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=rostovka
    Looking for:  43 katherine
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=katherine
    Looking for:  44 peresichna
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=peresichna
    Looking for:  45 saleaula
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=saleaula
    Looking for:  saleaula not found
    Looking for:  45 cascais
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=cascais
    Looking for:  46 chicontepec
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=chicontepec
    Looking for:  47 biak
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=biak
    Looking for:  48 yertsevo
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=yertsevo
    Looking for:  49 karkaralinsk
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=karkaralinsk
    Looking for:  karkaralinsk not found
    Looking for:  49 aklavik
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=aklavik
    Looking for:  50 zyryanka
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=zyryanka
    Looking for:  51 balikpapan
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=balikpapan
    Looking for:  52 sitka
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=sitka
    Looking for:  53 vila franca do campo
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=vila franca do campo
    Looking for:  54 geresk
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=geresk
    Looking for:  geresk not found
    Looking for:  54 konstancin-jeziorna
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=konstancin-jeziorna
    Looking for:  55 osorheiu
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=osorheiu
    Looking for:  56 ayagoz
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=ayagoz
    Looking for:  57 de-kastri
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=de-kastri
    Looking for:  58 okhotsk
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=okhotsk
    Looking for:  59 yellowknife
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=yellowknife
    Looking for:  60 phan thiet
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=phan thiet
    Looking for:  61 kamenka
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kamenka
    Looking for:  62 sentyabrskiy
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=sentyabrskiy
    Looking for:  sentyabrskiy not found
    Looking for:  62 voyvozh
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=voyvozh
    Looking for:  63 zima
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=zima
    Looking for:  64 luganville
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=luganville
    Looking for:  65 grajau
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=grajau
    Looking for:  grajau not found
    Looking for:  65 palmer
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=palmer
    Looking for:  66 richards bay
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=richards bay
    Looking for:  67 tabiauea
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=tabiauea
    Looking for:  tabiauea not found
    Looking for:  67 chauk
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=chauk
    Looking for:  68 atar
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=atar
    Looking for:  69 junin
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=junin
    Looking for:  70 lavrentiya
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=lavrentiya
    Looking for:  71 mangai
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=mangai
    Looking for:  72 iquitos
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=iquitos
    Looking for:  73 banjar
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=banjar
    Looking for:  74 gualaco
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=gualaco
    Looking for:  75 new norfolk
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=new norfolk
    Looking for:  76 preobrazheniye
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=preobrazheniye
    Looking for:  77 codrington
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=codrington
    Looking for:  78 fuxin
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=fuxin
    Looking for:  79 port hedland
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=port hedland
    Looking for:  80 samusu
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=samusu
    Looking for:  samusu not found
    Looking for:  80 saryshagan
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=saryshagan
    Looking for:  saryshagan not found
    Looking for:  80 pevek
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=pevek
    Looking for:  81 krutinka
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=krutinka
    Looking for:  82 kutum
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kutum
    Looking for:  83 jimma
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=jimma
    Looking for:  84 kroya
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kroya
    Looking for:  85 tsihombe
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=tsihombe
    Looking for:  tsihombe not found
    Looking for:  85 rastolita
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=rastolita
    Looking for:  86 gerash
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=gerash
    Looking for:  87 pisco
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=pisco
    Looking for:  88 srivardhan
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=srivardhan
    Looking for:  89 mahebourg
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=mahebourg
    Looking for:  90 gondanglegi
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=gondanglegi
    Looking for:  91 kuching
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kuching
    Looking for:  92 tilichiki
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=tilichiki
    Looking for:  93 bosaso
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=bosaso
    Looking for:  94 dabola
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=dabola
    Looking for:  95 alice springs
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=alice springs
    Looking for:  96 portpatrick
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=portpatrick
    Looking for:  portpatrick not found
    Looking for:  96 dikson
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=dikson
    Looking for:  97 umzimvubu
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=umzimvubu
    Looking for:  umzimvubu not found
    Looking for:  97 kuusamo
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kuusamo
    Looking for:  98 goderich
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=goderich
    Looking for:  99 hilo
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=hilo
    Looking for:  100 victoria
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=victoria
    Looking for:  101 bochil
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=bochil
    Looking for:  102 meulaboh
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=meulaboh
    Looking for:  103 whitehorse
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=whitehorse
    Looking for:  104 san rafael
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=san rafael
    Looking for:  105 borodino
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=borodino
    Looking for:  106 deputatskiy
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=deputatskiy
    Looking for:  107 benidorm
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=benidorm
    Looking for:  108 athens
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=athens
    Looking for:  109 khasan
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=khasan
    Looking for:  110 igarka
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=igarka
    Looking for:  111 kez
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kez
    Looking for:  112 klaksvik
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=klaksvik
    Looking for:  113 koungou
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=koungou
    Looking for:  koungou not found
    Looking for:  113 winnemucca
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=winnemucca
    Looking for:  114 lahaina
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=lahaina
    Looking for:  115 yelandur
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=yelandur
    Looking for:  116 canala
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=canala
    Looking for:  117 linhares
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=linhares
    Looking for:  118 hualmay
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=hualmay
    Looking for:  119 luau
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=luau
    Looking for:  120 meylan
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=meylan
    Looking for:  121 avarua
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=avarua
    Looking for:  122 batesville
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=batesville
    Looking for:  123 arlit
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=arlit
    Looking for:  124 cherskiy
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=cherskiy
    Looking for:  125 sao filipe
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=sao filipe
    Looking for:  126 kaitangata
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kaitangata
    Looking for:  127 praia da vitoria
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=praia da vitoria
    Looking for:  128 khani
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=khani
    Looking for:  129 batken
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=batken
    Looking for:  130 hamilton
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=hamilton
    Looking for:  131 nicolas bravo
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=nicolas bravo
    Looking for:  132 la ronge
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=la ronge
    Looking for:  133 tarakan
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=tarakan
    Looking for:  134 annau
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=annau
    Looking for:  135 baruun-urt
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=baruun-urt
    Looking for:  136 zeya
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=zeya
    Looking for:  137 tunceli
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=tunceli
    Looking for:  138 sarangani
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=sarangani
    Looking for:  139 dolbeau
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=dolbeau
    Looking for:  dolbeau not found
    Looking for:  139 bumba
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=bumba
    Looking for:  140 santa cruz
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=santa cruz
    Looking for:  141 padang
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=padang
    Looking for:  142 shiyan
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=shiyan
    Looking for:  143 mount isa
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=mount isa
    Looking for:  144 wajima
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=wajima
    Looking for:  145 poso
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=poso
    Looking for:  146 west wendover
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=west wendover
    Looking for:  147 palazzolo acreide
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=palazzolo acreide
    Looking for:  148 virden
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=virden
    Looking for:  149 batemans bay
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=batemans bay
    Looking for:  150 kindu
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kindu
    Looking for:  151 mar del plata
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=mar del plata
    Looking for:  152 namatanai
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=namatanai
    Looking for:  153 punta arenas
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=punta arenas
    Looking for:  154 saint-francois
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=saint-francois
    Looking for:  155 ganzhou
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=ganzhou
    Looking for:  156 chokurdakh
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=chokurdakh
    Looking for:  157 misratah
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=misratah
    Looking for:  158 goryachegorsk
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=goryachegorsk
    Looking for:  159 pacific grove
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=pacific grove
    Looking for:  160 saint anthony
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=saint anthony
    Looking for:  161 warwick
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=warwick
    Looking for:  162 am timan
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=am timan
    Looking for:  163 albacete
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=albacete
    Looking for:  164 mount gambier
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=mount gambier
    Looking for:  165 broken hill
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=broken hill
    Looking for:  166 mitzic
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=mitzic
    Looking for:  167 hithadhoo
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=hithadhoo
    Looking for:  168 neftcala
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=neftcala
    Looking for:  169 turayf
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=turayf
    Looking for:  170 uvalde
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=uvalde
    Looking for:  171 halvad
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=halvad
    Looking for:  172 severo-kurilsk
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=severo-kurilsk
    Looking for:  173 east london
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=east london
    Looking for:  174 aztec
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=aztec
    Looking for:  175 keuruu
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=keuruu
    Looking for:  176 poum
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=poum
    Looking for:  177 sistranda
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=sistranda
    Looking for:  178 medea
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=medea
    Looking for:  179 port keats
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=port keats
    Looking for:  180 olafsvik
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=olafsvik
    Looking for:  olafsvik not found
    Looking for:  180 san juan de colon
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=san juan de colon
    Looking for:  181 hargeysa
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=hargeysa
    Looking for:  182 alyangula
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=alyangula
    Looking for:  183 port blair
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=port blair
    Looking for:  184 ballina
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=ballina
    Looking for:  185 hangu
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=hangu
    Looking for:  186 san quintin
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=san quintin
    Looking for:  187 avera
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=avera
    Looking for:  188 almaznyy
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=almaznyy
    Looking for:  189 iqaluit
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=iqaluit
    Looking for:  190 walvis bay
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=walvis bay
    Looking for:  191 kuala selangor
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kuala selangor
    Looking for:  192 viedma
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=viedma
    Looking for:  193 bethel
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=bethel
    Looking for:  194 calama
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=calama
    Looking for:  195 kirovsk
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kirovsk
    Looking for:  196 chabahar
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=chabahar
    Looking for:  197 baiyin
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=baiyin
    Looking for:  198 cap-aux-meules
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=cap-aux-meules
    Looking for:  199 hofn
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=hofn
    Looking for:  200 busselton
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=busselton
    Looking for:  201 faya
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=faya
    Looking for:  202 borogontsy
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=borogontsy
    Looking for:  203 kamaishi
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kamaishi
    Looking for:  204 muros
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=muros
    Looking for:  205 carnarvon
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=carnarvon
    Looking for:  206 tambovka
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=tambovka
    Looking for:  207 castro
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=castro
    Looking for:  208 lyaskelya
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=lyaskelya
    Looking for:  209 ayna
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=ayna
    Looking for:  210 kingsport
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kingsport
    Looking for:  211 tuktoyaktuk
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=tuktoyaktuk
    Looking for:  212 payo
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=payo
    Looking for:  213 kahului
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kahului
    Looking for:  214 sorland
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=sorland
    Looking for:  215 fort abbas
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=fort abbas
    Looking for:  216 sol-iletsk
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=sol-iletsk
    Looking for:  217 valkeakoski
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=valkeakoski
    Looking for:  218 den chai
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=den chai
    Looking for:  219 bloemfontein
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=bloemfontein
    Looking for:  220 rikitea
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=rikitea
    Looking for:  221 adrar
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=adrar
    Looking for:  222 saint george
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=saint george
    Looking for:  223 nha trang
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=nha trang
    Looking for:  224 geraldton
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=geraldton
    Looking for:  225 londoko
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=londoko
    Looking for:  londoko not found
    Looking for:  225 itarema
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=itarema
    Looking for:  226 thinadhoo
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=thinadhoo
    Looking for:  227 kamina
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kamina
    Looking for:  228 barrow
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=barrow
    Looking for:  229 nome
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=nome
    Looking for:  230 cacu
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=cacu
    Looking for:  231 muleba
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=muleba
    Looking for:  232 korhogo
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=korhogo
    Looking for:  233 namanyere
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=namanyere
    Looking for:  234 guderup
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=guderup
    Looking for:  235 warqla
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=warqla
    Looking for:  warqla not found
    Looking for:  235 blagoveshchensk
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=blagoveshchensk
    Looking for:  236 christchurch
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=christchurch
    Looking for:  237 wulanhaote
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=wulanhaote
    Looking for:  wulanhaote not found
    Looking for:  237 norman wells
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=norman wells
    Looking for:  238 belyy yar
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=belyy yar
    Looking for:  239 airai
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=airai
    Looking for:  240 saint-malo
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=saint-malo
    Looking for:  241 aksarka
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=aksarka
    Looking for:  242 nara
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=nara
    Looking for:  243 zalantun
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=zalantun
    Looking for:  244 barbar
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=barbar
    Looking for:  barbar not found
    Looking for:  244 tura
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=tura
    Looking for:  245 plettenberg bay
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=plettenberg bay
    Looking for:  246 cayenne
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=cayenne
    Looking for:  247 temaraia
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=temaraia
    Looking for:  temaraia not found
    Looking for:  247 olbia
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=olbia
    Looking for:  248 dingle
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=dingle
    Looking for:  249 kibuye
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kibuye
    Looking for:  250 srandakan
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=srandakan
    Looking for:  251 ribeira grande
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=ribeira grande
    Looking for:  252 mahina
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=mahina
    Looking for:  253 dossor
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=dossor
    Looking for:  254 torbay
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=torbay
    Looking for:  255 kaoma
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kaoma
    Looking for:  256 lang suan
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=lang suan
    Looking for:  257 maragogi
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=maragogi
    Looking for:  258 caraquet
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=caraquet
    Looking for:  259 juba
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=juba
    Looking for:  260 ozgon
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=ozgon
    Looking for:  ozgon not found
    Looking for:  260 baixa grande
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=baixa grande
    Looking for:  261 carauari
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=carauari
    Looking for:  262 msanga
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=msanga
    Looking for:  263 bandarbeyla
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=bandarbeyla
    Looking for:  264 lorengau
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=lorengau
    Looking for:  265 lumajang
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=lumajang
    Looking for:  266 tagusao
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=tagusao
    Looking for:  267 khormuj
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=khormuj
    Looking for:  khormuj not found
    Looking for:  267 gamba
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=gamba
    Looking for:  268 leh
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=leh
    Looking for:  269 barcelos
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=barcelos
    Looking for:  270 sur
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=sur
    Looking for:  271 aguada de pasajeros
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=aguada de pasajeros
    Looking for:  272 trelew
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=trelew
    Looking for:  273 tubmanburg
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=tubmanburg
    Looking for:  274 finschhafen
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=finschhafen
    Looking for:  275 litovko
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=litovko
    Looking for:  276 koslan
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=koslan
    Looking for:  277 tateyama
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=tateyama
    Looking for:  278 baker city
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=baker city
    Looking for:  279 qaanaaq
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=qaanaaq
    Looking for:  280 gornja koprivna
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=gornja koprivna
    Looking for:  281 luanda
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=luanda
    Looking for:  282 yarmouth
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=yarmouth
    Looking for:  283 basoko
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=basoko
    Looking for:  284 bafq
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=bafq
    Looking for:  285 byron bay
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=byron bay
    Looking for:  286 bemidji
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=bemidji
    Looking for:  287 kanker
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kanker
    Looking for:  288 male
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=male
    Looking for:  289 port elizabeth
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=port elizabeth
    Looking for:  290 praxedis guerrero
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=praxedis guerrero
    Looking for:  291 zhigansk
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=zhigansk
    Looking for:  292 fujin
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=fujin
    Looking for:  293 coihaique
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=coihaique
    Looking for:  294 zhanaozen
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=zhanaozen
    Looking for:  295 rio cuarto
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=rio cuarto
    Looking for:  296 barra do garcas
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=barra do garcas
    Looking for:  297 grindavik
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=grindavik
    Looking for:  298 phangnga
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=phangnga
    Looking for:  299 venado tuerto
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=venado tuerto
    Looking for:  300 qeshm
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=qeshm
    Looking for:  301 vaitupu
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=vaitupu
    Looking for:  vaitupu not found
    Looking for:  301 bilibino
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=bilibino
    Looking for:  302 luena
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=luena
    Looking for:  303 saquena
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=saquena
    Looking for:  304 shenjiamen
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=shenjiamen
    Looking for:  305 lipin bor
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=lipin bor
    Looking for:  306 payson
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=payson
    Looking for:  307 alofi
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=alofi
    Looking for:  308 alihe
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=alihe
    Looking for:  309 xiaolingwei
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=xiaolingwei
    Looking for:  310 winchester
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=winchester
    Looking for:  311 puerto madryn
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=puerto madryn
    Looking for:  312 madison
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=madison
    Looking for:  313 guerrero negro
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=guerrero negro
    Looking for:  314 grand gaube
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=grand gaube
    Looking for:  315 russkaya polyana
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=russkaya polyana
    Looking for:  316 vardo
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=vardo
    Looking for:  317 port perry
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=port perry
    Looking for:  318 tidore
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=tidore
    Looking for:  tidore not found
    Looking for:  318 noyabrsk
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=noyabrsk
    Looking for:  319 clyde river
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=clyde river
    Looking for:  320 hasaki
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=hasaki
    Looking for:  321 arraial do cabo
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=arraial do cabo
    Looking for:  322 lauria
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=lauria
    Looking for:  323 torzhok
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=torzhok
    Looking for:  324 anadyr
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=anadyr
    Looking for:  325 bogovina
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=bogovina
    Looking for:  326 krutikha
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=krutikha
    Looking for:  327 grootfontein
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=grootfontein
    Looking for:  328 auki
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=auki
    Looking for:  329 baghdad
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=baghdad
    Looking for:  330 ruatoria
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=ruatoria
    Looking for:  ruatoria not found
    Looking for:  330 gillette
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=gillette
    Looking for:  331 porto novo
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=porto novo
    Looking for:  332 oussouye
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=oussouye
    Looking for:  333 saldanha
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=saldanha
    Looking for:  334 faanui
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=faanui
    Looking for:  335 sisimiut
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=sisimiut
    Looking for:  336 maningrida
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=maningrida
    Looking for:  337 eenhana
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=eenhana
    Looking for:  338 narsaq
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=narsaq
    Looking for:  339 broome
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=broome
    Looking for:  340 newport
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=newport
    Looking for:  341 yomitan
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=yomitan
    Looking for:  yomitan not found
    Looking for:  341 inhambane
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=inhambane
    Looking for:  342 noshiro
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=noshiro
    Looking for:  343 santa maria
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=santa maria
    Looking for:  344 wanaka
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=wanaka
    Looking for:  345 atuona
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=atuona
    Looking for:  346 lompoc
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=lompoc
    Looking for:  347 puerto ayora
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=puerto ayora
    Looking for:  348 waling
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=waling
    Looking for:  waling not found
    Looking for:  348 mackenzie
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=mackenzie
    Looking for:  349 constitucion
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=constitucion
    Looking for:  350 wenchi
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=wenchi
    Looking for:  351 barentsburg
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=barentsburg
    Looking for:  barentsburg not found
    Looking for:  351 awallan
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=awallan
    Looking for:  352 port-gentil
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=port-gentil
    Looking for:  353 maracacume
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=maracacume
    Looking for:  354 perene
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=perene
    Looking for:  355 micheweni
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=micheweni
    Looking for:  356 methoni
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=methoni
    Looking for:  357 nikolskoye
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=nikolskoye
    Looking for:  358 waipawa
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=waipawa
    Looking for:  359 mayor pablo lagerenza
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=mayor pablo lagerenza
    Looking for:  360 skibotn
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=skibotn
    Looking for:  361 souillac
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=souillac
    Looking for:  362 leningradskiy
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=leningradskiy
    Looking for:  363 dunedin
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=dunedin
    Looking for:  364 nantucket
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=nantucket
    Looking for:  365 chitipa
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=chitipa
    Looking for:  366 mao
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=mao
    Looking for:  367 korla
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=korla
    Looking for:  korla not found
    Looking for:  367 point fortin
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=point fortin
    Looking for:  368 tiksi
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=tiksi
    Looking for:  369 kodiak
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kodiak
    Looking for:  370 mehamn
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=mehamn
    Looking for:  371 jamestown
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=jamestown
    Looking for:  372 sterling
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=sterling
    Looking for:  373 pangnirtung
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=pangnirtung
    Looking for:  374 vestmannaeyjar
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=vestmannaeyjar
    Looking for:  375 nyurba
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=nyurba
    Looking for:  376 poykovskiy
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=poykovskiy
    Looking for:  377 puri
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=puri
    Looking for:  378 cabedelo
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=cabedelo
    Looking for:  379 yilan
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=yilan
    Looking for:  380 cefalu
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=cefalu
    Looking for:  381 aykhal
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=aykhal
    Looking for:  382 rocha
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=rocha
    Looking for:  383 concepcion
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=concepcion
    Looking for:  384 georgetown
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=georgetown
    Looking for:  385 ciras
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=ciras
    Looking for:  ciras not found
    Looking for:  385 paros
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=paros
    Looking for:  386 vaini
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=vaini
    Looking for:  387 prabumulih
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=prabumulih
    Looking for:  388 bowen
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=bowen
    Looking for:  389 hervey bay
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=hervey bay
    Looking for:  390 northam
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=northam
    Looking for:  391 sola
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=sola
    Looking for:  392 krasnovishersk
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=krasnovishersk
    Looking for:  393 puerto escondido
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=puerto escondido
    Looking for:  394 tumannyy
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=tumannyy
    Looking for:  tumannyy not found
    Looking for:  394 kavaratti
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kavaratti
    Looking for:  395 saleilua
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=saleilua
    Looking for:  saleilua not found
    Looking for:  395 kruisfontein
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kruisfontein
    Looking for:  396 kavieng
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kavieng
    Looking for:  397 thompson
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=thompson
    Looking for:  398 half moon bay
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=half moon bay
    Looking for:  399 gorno-altaysk
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=gorno-altaysk
    Looking for:  400 sibolga
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=sibolga
    Looking for:  401 maniitsoq
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=maniitsoq
    Looking for:  402 coquimbo
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=coquimbo
    Looking for:  403 seoul
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=seoul
    Looking for:  404 debre tabor
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=debre tabor
    Looking for:  405 rocky mountain house
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=rocky mountain house
    Looking for:  406 naze
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=naze
    Looking for:  407 mangit
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=mangit
    Looking for:  408 ust-omchug
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=ust-omchug
    Looking for:  409 sabang
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=sabang
    Looking for:  410 carthage
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=carthage
    Looking for:  411 quatre cocos
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=quatre cocos
    Looking for:  412 lixourion
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=lixourion
    Looking for:  413 kegayli
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kegayli
    Looking for:  kegayli not found
    Looking for:  413 saint-jean-port-joli
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=saint-jean-port-joli
    Looking for:  saint-jean-port-joli not found
    Looking for:  413 ilulissat
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=ilulissat
    Looking for:  414 usinsk
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=usinsk
    Looking for:  415 raudeberg
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=raudeberg
    Looking for:  416 khatanga
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=khatanga
    Looking for:  417 ambon
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=ambon
    Looking for:  418 safonovo
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=safonovo
    Looking for:  419 padre bernardo
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=padre bernardo
    Looking for:  padre bernardo not found
    Looking for:  419 balila
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=balila
    Looking for:  420 lucapa
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=lucapa
    Looking for:  421 varhaug
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=varhaug
    Looking for:  422 taolanaro
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=taolanaro
    Looking for:  taolanaro not found
    Looking for:  422 nurota
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=nurota
    Looking for:  423 longyearbyen
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=longyearbyen
    Looking for:  424 astipalaia
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=astipalaia
    Looking for:  astipalaia not found
    Looking for:  424 innisfail
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=innisfail
    Looking for:  425 provideniya
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=provideniya
    Looking for:  426 talaya
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=talaya
    Looking for:  427 mataura
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=mataura
    Looking for:  428 beidao
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=beidao
    Looking for:  429 dapaong
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=dapaong
    Looking for:  430 ust-tsilma
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=ust-tsilma
    Looking for:  431 calabozo
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=calabozo
    Looking for:  432 sioux lookout
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=sioux lookout
    Looking for:  433 bredasdorp
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=bredasdorp
    Looking for:  434 road town
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=road town
    Looking for:  435 mayo
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=mayo
    Looking for:  436 novomykolayivka
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=novomykolayivka
    Looking for:  437 tashtyp
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=tashtyp
    Looking for:  438 buala
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=buala
    Looking for:  439 kupang
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kupang
    Looking for:  440 masallatah
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=masallatah
    Looking for:  441 esil
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=esil
    Looking for:  442 takaka
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=takaka
    Looking for:  443 tomatlan
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=tomatlan
    Looking for:  444 mackay
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=mackay
    Looking for:  445 hebi
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=hebi
    Looking for:  446 sawakin
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=sawakin
    Looking for:  447 bathsheba
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=bathsheba
    Looking for:  448 clarence town
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=clarence town
    Looking for:  449 andra
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=andra
    Looking for:  450 angouleme
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=angouleme
    Looking for:  451 lolua
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=lolua
    Looking for:  lolua not found
    Looking for:  451 kailua
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kailua
    Looking for:  452 bengkulu
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=bengkulu
    Looking for:  bengkulu not found
    Looking for:  452 salina cruz
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=salina cruz
    Looking for:  453 belushya guba
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=belushya guba
    Looking for:  belushya guba not found
    Looking for:  453 nova olimpia
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=nova olimpia
    Looking for:  454 hobart
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=hobart
    Looking for:  455 korablino
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=korablino
    Looking for:  456 carbonear
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=carbonear
    Looking for:  457 de aar
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=de aar
    Looking for:  458 comodoro rivadavia
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=comodoro rivadavia
    Looking for:  459 acajutla
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=acajutla
    Looking for:  460 cabo san lucas
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=cabo san lucas
    Looking for:  461 uruacu
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=uruacu
    Looking for:  462 vao
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=vao
    Looking for:  463 champasak
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=champasak
    Looking for:  464 gat
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=gat
    Looking for:  465 malacacheta
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=malacacheta
    Looking for:  466 manta
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=manta
    Looking for:  467 kapaa
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kapaa
    Looking for:  468 denpasar
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=denpasar
    Looking for:  469 tasiilaq
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=tasiilaq
    Looking for:  470 amderma
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=amderma
    Looking for:  amderma not found
    Looking for:  470 severo-yeniseyskiy
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=severo-yeniseyskiy
    Looking for:  471 puerto del rosario
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=puerto del rosario
    Looking for:  472 katsuura
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=katsuura
    Looking for:  473 dafeng
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=dafeng
    Looking for:  474 trincomalee
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=trincomalee
    Looking for:  475 ponta do sol
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=ponta do sol
    Looking for:  476 cidreira
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=cidreira
    Looking for:  477 longkou
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=longkou
    Looking for:  478 huarmey
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=huarmey
    Looking for:  479 kapoeta
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kapoeta
    Looking for:  kapoeta not found
    Looking for:  479 kungurtug
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kungurtug
    Looking for:  480 fort nelson
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=fort nelson
    Looking for:  481 tarauaca
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=tarauaca
    Looking for:  482 sherpur
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=sherpur
    Looking for:  483 manado
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=manado
    Looking for:  484 mahaicony
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=mahaicony
    Looking for:  mahaicony not found
    Looking for:  484 presidencia roque saenz pena
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=presidencia roque saenz pena
    Looking for:  485 kilosa
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=kilosa
    Looking for:  486 tabou
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=tabou
    Looking for:  487 jiuquan
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=jiuquan
    Looking for:  488 sumbe
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=sumbe
    Looking for:  489 safaga
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=safaga
    Looking for:  safaga not found
    Looking for:  489 klaebu
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=klaebu
    Looking for:  490 fairbanks
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=fairbanks
    Looking for:  491 khagrachari
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=khagrachari
    Looking for:  khagrachari not found
    Looking for:  491 gorontalo
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=gorontalo
    Looking for:  492 eureka
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=eureka
    Looking for:  493 dubbo
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=dubbo
    Looking for:  494 davila
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=davila
    Looking for:  495 beringovskiy
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=beringovskiy
    Looking for:  496 otaru
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=otaru
    Looking for:  497 shimoda
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=shimoda
    Looking for:  498 chimore
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=chimore
    Looking for:  499 challans
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=challans
    Looking for:  500 hermanus
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=hermanus
    Looking for:  501 saint-philippe
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=saint-philippe
    Looking for:  502 abidjan
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=abidjan
    Looking for:  503 chuy
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=chuy
    Looking for:  504 albany
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=albany
    Looking for:  505 leshan
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=leshan
    Looking for:  leshan not found
    Looking for:  505 lukhovitsy
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=lukhovitsy
    Looking for:  506 grand river south east
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=grand river south east
    Looking for:  grand river south east not found
    Looking for:  506 acari
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=acari
    Looking for:  507 aswan
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=aswan
    Looking for:  508 isagarh
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=isagarh
    Looking for:  509 bambous virieux
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=bambous virieux
    Looking for:  510 hovd
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=hovd
    Looking for:  511 cururupu
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=cururupu
    Looking for:  512 gairo
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=gairo
    Looking for:  513 marcona
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=marcona
    Looking for:  marcona not found
    Looking for:  513 lac du bonnet
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=lac du bonnet
    Looking for:  514 okha
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=okha
    Looking for:  515 ladwa
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=ladwa
    Looking for:  516 xudat
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=xudat
    Looking for:  517 sidi ali
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=sidi ali
    Looking for:  518 illoqqortoormiut
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=illoqqortoormiut
    Looking for:  illoqqortoormiut not found
    Looking for:  518 yulara
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=yulara
    Looking for:  519 tuatapere
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=tuatapere
    Looking for:  520 bur gabo
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=bur gabo
    Looking for:  bur gabo not found
    Looking for:  520 isiro
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=isiro
    Looking for:  521 port augusta
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=port augusta
    Looking for:  522 cape town
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=cape town
    Looking for:  523 badarganj
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=badarganj
    Looking for:  524 ostersund
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=ostersund
    Looking for:  525 uyuni
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=uyuni
    Looking for:  526 sotnikovskoye
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=sotnikovskoye
    Looking for:  527 saint-augustin
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=saint-augustin
    Looking for:  528 jacmel
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=jacmel
    Looking for:  529 borovoy
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=borovoy
    Looking for:  530 imeni poliny osipenko
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=imeni poliny osipenko
    Looking for:  531 colombo
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=colombo
    Looking for:  532 malartic
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=malartic
    Looking for:  533 khash
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=khash
    Looking for:  534 tartus
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=tartus
    Looking for:  tartus not found
    Looking for:  534 bud
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=bud
    Looking for:  535 nizhnyaya salda
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=nizhnyaya salda
    Looking for:  536 morros
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=morros
    Looking for:  537 lagoa
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=lagoa
    Looking for:  538 los llanos de aridane
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=los llanos de aridane
    Looking for:  539 wewak
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=wewak
    Looking for:  540 roswell
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=roswell
    Looking for:  541 talnakh
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=talnakh
    Looking for:  542 ahipara
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=ahipara
    Looking for:  543 axim
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=axim
    Looking for:  544 vestmanna
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=vestmanna
    Looking for:  545 moussoro
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=moussoro
    Looking for:  546 san patricio
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=san patricio
    Looking for:  547 attawapiskat
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=attawapiskat
    Looking for:  attawapiskat not found
    Looking for:  547 viseu
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=viseu
    Looking for:  548 saskylakh
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=saskylakh
    Looking for:  549 port lincoln
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=port lincoln
    Looking for:  550 olovyannaya
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=olovyannaya
    Looking for:  551 hambantota
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=hambantota
    Looking for:  552 port alfred
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=port alfred
    Looking for:  553 esperance
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=esperance
    Looking for:  554 bonavista
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=bonavista
    Looking for:  555 bolobo
    http://api.openweathermap.org/data/2.5/weather?appid=072d7a0514e41ad73f86777cb59af9d0&units=metric&q=bolobo
    


```python
# create the dataframe to hold the results 

# create a data frame from cities, lat, and temp
weather_dict = {'City': cityname,
                'Cloudiness': cloudiness,
                'Country': country,
                'Date': date,
                'Humidity': humidity,
                'Lat': lat,
                'Lng': lng,
                'Max Temp': maxtemp,
                'Wind Speed' : windspeed
                }

CityResults_df = pd.DataFrame(weather_dict)
CityResults_df.head(600)

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>Cloudiness</th>
      <th>Country</th>
      <th>Date</th>
      <th>Humidity</th>
      <th>Lat</th>
      <th>Lng</th>
      <th>Max Temp</th>
      <th>Wind Speed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Santa Rosa</td>
      <td>20</td>
      <td>AR</td>
      <td>1520901300</td>
      <td>46</td>
      <td>-36.62</td>
      <td>-64.29</td>
      <td>23.00</td>
      <td>6.70</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Upernavik</td>
      <td>36</td>
      <td>GL</td>
      <td>1520906999</td>
      <td>96</td>
      <td>72.79</td>
      <td>-56.15</td>
      <td>-18.98</td>
      <td>0.51</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Swellendam</td>
      <td>0</td>
      <td>ZA</td>
      <td>1520902800</td>
      <td>88</td>
      <td>-34.02</td>
      <td>20.44</td>
      <td>17.00</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Kasangulu</td>
      <td>12</td>
      <td>CD</td>
      <td>1520902800</td>
      <td>74</td>
      <td>-4.59</td>
      <td>15.17</td>
      <td>26.00</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Purwodadi</td>
      <td>76</td>
      <td>ID</td>
      <td>1520907001</td>
      <td>89</td>
      <td>-7.08</td>
      <td>110.92</td>
      <td>26.22</td>
      <td>1.26</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Taltal</td>
      <td>0</td>
      <td>CL</td>
      <td>1520907001</td>
      <td>97</td>
      <td>-25.41</td>
      <td>-70.49</td>
      <td>11.57</td>
      <td>0.66</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Bluff</td>
      <td>36</td>
      <td>AU</td>
      <td>1520906921</td>
      <td>37</td>
      <td>-23.58</td>
      <td>149.07</td>
      <td>31.12</td>
      <td>6.31</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Petropavlovsk-Kamchatskiy</td>
      <td>48</td>
      <td>RU</td>
      <td>1520904600</td>
      <td>48</td>
      <td>53.05</td>
      <td>158.65</td>
      <td>-6.00</td>
      <td>1.00</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Rongcheng</td>
      <td>0</td>
      <td>CN</td>
      <td>1520907003</td>
      <td>58</td>
      <td>37.16</td>
      <td>122.42</td>
      <td>16.12</td>
      <td>7.16</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Sorsk</td>
      <td>0</td>
      <td>RU</td>
      <td>1520907003</td>
      <td>71</td>
      <td>54.00</td>
      <td>90.25</td>
      <td>-19.93</td>
      <td>0.56</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Caravelas</td>
      <td>64</td>
      <td>BR</td>
      <td>1520907004</td>
      <td>100</td>
      <td>-17.73</td>
      <td>-39.27</td>
      <td>26.97</td>
      <td>7.01</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Kulhudhuffushi</td>
      <td>68</td>
      <td>MV</td>
      <td>1520907004</td>
      <td>100</td>
      <td>6.62</td>
      <td>73.07</td>
      <td>26.57</td>
      <td>4.16</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Marzuq</td>
      <td>0</td>
      <td>YE</td>
      <td>1520907004</td>
      <td>82</td>
      <td>14.40</td>
      <td>46.47</td>
      <td>7.02</td>
      <td>0.96</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Colac</td>
      <td>0</td>
      <td>AU</td>
      <td>1520907005</td>
      <td>58</td>
      <td>-38.34</td>
      <td>143.59</td>
      <td>20.52</td>
      <td>2.31</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Otautau</td>
      <td>92</td>
      <td>NZ</td>
      <td>1520907005</td>
      <td>87</td>
      <td>-46.14</td>
      <td>168.00</td>
      <td>10.87</td>
      <td>9.01</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Agirish</td>
      <td>36</td>
      <td>RU</td>
      <td>1520907005</td>
      <td>77</td>
      <td>61.92</td>
      <td>63.02</td>
      <td>-12.58</td>
      <td>2.81</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Te Anau</td>
      <td>92</td>
      <td>NZ</td>
      <td>1520907006</td>
      <td>78</td>
      <td>-45.41</td>
      <td>167.72</td>
      <td>8.22</td>
      <td>4.46</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Mangrol</td>
      <td>0</td>
      <td>IN</td>
      <td>1520907006</td>
      <td>37</td>
      <td>25.33</td>
      <td>76.51</td>
      <td>23.17</td>
      <td>2.41</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Hami</td>
      <td>0</td>
      <td>CN</td>
      <td>1520907007</td>
      <td>58</td>
      <td>42.84</td>
      <td>93.51</td>
      <td>12.27</td>
      <td>3.41</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Inuvik</td>
      <td>40</td>
      <td>CA</td>
      <td>1520902800</td>
      <td>66</td>
      <td>68.36</td>
      <td>-133.71</td>
      <td>-11.00</td>
      <td>1.46</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Ushuaia</td>
      <td>75</td>
      <td>AR</td>
      <td>1520906400</td>
      <td>70</td>
      <td>-54.81</td>
      <td>-68.31</td>
      <td>7.00</td>
      <td>4.60</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Genhe</td>
      <td>12</td>
      <td>CN</td>
      <td>1520907007</td>
      <td>70</td>
      <td>50.78</td>
      <td>121.52</td>
      <td>-2.78</td>
      <td>2.46</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Altay</td>
      <td>56</td>
      <td>CN</td>
      <td>1520907008</td>
      <td>74</td>
      <td>47.83</td>
      <td>88.13</td>
      <td>-3.38</td>
      <td>1.16</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Manosque</td>
      <td>0</td>
      <td>FR</td>
      <td>1520904600</td>
      <td>70</td>
      <td>43.83</td>
      <td>5.78</td>
      <td>10.00</td>
      <td>2.10</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Stokmarknes</td>
      <td>0</td>
      <td>NO</td>
      <td>1520907009</td>
      <td>100</td>
      <td>68.56</td>
      <td>14.91</td>
      <td>-3.88</td>
      <td>1.36</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Athabasca</td>
      <td>0</td>
      <td>CA</td>
      <td>1520906768</td>
      <td>77</td>
      <td>54.72</td>
      <td>-113.29</td>
      <td>-7.13</td>
      <td>3.41</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Barahan</td>
      <td>0</td>
      <td>PH</td>
      <td>1520907009</td>
      <td>87</td>
      <td>13.01</td>
      <td>120.76</td>
      <td>28.72</td>
      <td>0.31</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Bull Savanna</td>
      <td>24</td>
      <td>JM</td>
      <td>1520906914</td>
      <td>87</td>
      <td>17.89</td>
      <td>-77.59</td>
      <td>21.37</td>
      <td>1.56</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Butaritari</td>
      <td>80</td>
      <td>KI</td>
      <td>1520906916</td>
      <td>100</td>
      <td>3.07</td>
      <td>172.79</td>
      <td>28.27</td>
      <td>5.51</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Tungor</td>
      <td>76</td>
      <td>RU</td>
      <td>1520907010</td>
      <td>97</td>
      <td>53.39</td>
      <td>142.95</td>
      <td>-8.03</td>
      <td>2.26</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>526</th>
      <td>Sotnikovskoye</td>
      <td>20</td>
      <td>RU</td>
      <td>1520907186</td>
      <td>86</td>
      <td>45.00</td>
      <td>43.79</td>
      <td>-6.43</td>
      <td>4.56</td>
    </tr>
    <tr>
      <th>527</th>
      <td>Saint-Augustin</td>
      <td>0</td>
      <td>FR</td>
      <td>1520906400</td>
      <td>87</td>
      <td>44.83</td>
      <td>-0.61</td>
      <td>9.00</td>
      <td>3.60</td>
    </tr>
    <tr>
      <th>528</th>
      <td>Jacmel</td>
      <td>0</td>
      <td>HT</td>
      <td>1520907187</td>
      <td>97</td>
      <td>18.24</td>
      <td>-72.54</td>
      <td>25.92</td>
      <td>7.96</td>
    </tr>
    <tr>
      <th>529</th>
      <td>Borovoy</td>
      <td>80</td>
      <td>RU</td>
      <td>1520907187</td>
      <td>81</td>
      <td>63.23</td>
      <td>52.89</td>
      <td>-8.63</td>
      <td>4.46</td>
    </tr>
    <tr>
      <th>530</th>
      <td>Imeni Poliny Osipenko</td>
      <td>68</td>
      <td>RU</td>
      <td>1520907188</td>
      <td>80</td>
      <td>52.42</td>
      <td>136.49</td>
      <td>-5.03</td>
      <td>2.21</td>
    </tr>
    <tr>
      <th>531</th>
      <td>Colombo</td>
      <td>40</td>
      <td>LK</td>
      <td>1520903400</td>
      <td>88</td>
      <td>6.93</td>
      <td>79.85</td>
      <td>24.00</td>
      <td>1.50</td>
    </tr>
    <tr>
      <th>532</th>
      <td>Malartic</td>
      <td>90</td>
      <td>CA</td>
      <td>1520905380</td>
      <td>92</td>
      <td>48.14</td>
      <td>-78.13</td>
      <td>-4.00</td>
      <td>1.50</td>
    </tr>
    <tr>
      <th>533</th>
      <td>Khash</td>
      <td>0</td>
      <td>IR</td>
      <td>1520907189</td>
      <td>64</td>
      <td>28.22</td>
      <td>61.21</td>
      <td>8.67</td>
      <td>2.06</td>
    </tr>
    <tr>
      <th>534</th>
      <td>Bud</td>
      <td>0</td>
      <td>NO</td>
      <td>1520905800</td>
      <td>68</td>
      <td>62.91</td>
      <td>6.91</td>
      <td>1.00</td>
      <td>3.10</td>
    </tr>
    <tr>
      <th>535</th>
      <td>Nizhnyaya Salda</td>
      <td>0</td>
      <td>RU</td>
      <td>1520907189</td>
      <td>64</td>
      <td>58.07</td>
      <td>60.71</td>
      <td>-17.63</td>
      <td>2.36</td>
    </tr>
    <tr>
      <th>536</th>
      <td>Morros</td>
      <td>20</td>
      <td>BR</td>
      <td>1520906400</td>
      <td>83</td>
      <td>-2.87</td>
      <td>-44.04</td>
      <td>27.00</td>
      <td>3.60</td>
    </tr>
    <tr>
      <th>537</th>
      <td>Lagoa</td>
      <td>75</td>
      <td>PT</td>
      <td>1520904600</td>
      <td>100</td>
      <td>37.14</td>
      <td>-8.45</td>
      <td>15.00</td>
      <td>3.10</td>
    </tr>
    <tr>
      <th>538</th>
      <td>Los Llanos de Aridane</td>
      <td>8</td>
      <td>ES</td>
      <td>1520906400</td>
      <td>82</td>
      <td>28.66</td>
      <td>-17.92</td>
      <td>16.00</td>
      <td>3.10</td>
    </tr>
    <tr>
      <th>539</th>
      <td>Wewak</td>
      <td>56</td>
      <td>PG</td>
      <td>1520907191</td>
      <td>68</td>
      <td>-3.55</td>
      <td>143.63</td>
      <td>30.47</td>
      <td>2.26</td>
    </tr>
    <tr>
      <th>540</th>
      <td>Roswell</td>
      <td>1</td>
      <td>US</td>
      <td>1520904900</td>
      <td>27</td>
      <td>33.39</td>
      <td>-104.52</td>
      <td>14.00</td>
      <td>5.70</td>
    </tr>
    <tr>
      <th>541</th>
      <td>Talnakh</td>
      <td>64</td>
      <td>RU</td>
      <td>1520906963</td>
      <td>84</td>
      <td>69.49</td>
      <td>88.39</td>
      <td>-25.48</td>
      <td>8.21</td>
    </tr>
    <tr>
      <th>542</th>
      <td>Ahipara</td>
      <td>80</td>
      <td>NZ</td>
      <td>1520907191</td>
      <td>81</td>
      <td>-35.17</td>
      <td>173.16</td>
      <td>20.92</td>
      <td>7.11</td>
    </tr>
    <tr>
      <th>543</th>
      <td>Axim</td>
      <td>56</td>
      <td>GH</td>
      <td>1520907192</td>
      <td>100</td>
      <td>4.87</td>
      <td>-2.24</td>
      <td>27.37</td>
      <td>4.11</td>
    </tr>
    <tr>
      <th>544</th>
      <td>Vestmanna</td>
      <td>88</td>
      <td>FO</td>
      <td>1520905800</td>
      <td>55</td>
      <td>62.16</td>
      <td>-7.17</td>
      <td>4.00</td>
      <td>8.70</td>
    </tr>
    <tr>
      <th>545</th>
      <td>Moussoro</td>
      <td>0</td>
      <td>TD</td>
      <td>1520907192</td>
      <td>14</td>
      <td>13.64</td>
      <td>16.49</td>
      <td>22.87</td>
      <td>5.91</td>
    </tr>
    <tr>
      <th>546</th>
      <td>San Patricio</td>
      <td>0</td>
      <td>PY</td>
      <td>1520906927</td>
      <td>65</td>
      <td>-26.98</td>
      <td>-56.83</td>
      <td>24.67</td>
      <td>2.06</td>
    </tr>
    <tr>
      <th>547</th>
      <td>Viseu</td>
      <td>40</td>
      <td>PT</td>
      <td>1520902800</td>
      <td>93</td>
      <td>40.66</td>
      <td>-7.91</td>
      <td>10.00</td>
      <td>4.60</td>
    </tr>
    <tr>
      <th>548</th>
      <td>Saskylakh</td>
      <td>64</td>
      <td>RU</td>
      <td>1520907193</td>
      <td>82</td>
      <td>71.97</td>
      <td>114.09</td>
      <td>-32.53</td>
      <td>2.96</td>
    </tr>
    <tr>
      <th>549</th>
      <td>Port Lincoln</td>
      <td>0</td>
      <td>AU</td>
      <td>1520907193</td>
      <td>85</td>
      <td>-34.72</td>
      <td>135.86</td>
      <td>19.72</td>
      <td>5.16</td>
    </tr>
    <tr>
      <th>550</th>
      <td>Olovyannaya</td>
      <td>80</td>
      <td>RU</td>
      <td>1520907194</td>
      <td>63</td>
      <td>50.94</td>
      <td>115.59</td>
      <td>-3.93</td>
      <td>2.86</td>
    </tr>
    <tr>
      <th>551</th>
      <td>Hambantota</td>
      <td>80</td>
      <td>LK</td>
      <td>1520907194</td>
      <td>100</td>
      <td>6.12</td>
      <td>81.12</td>
      <td>25.72</td>
      <td>6.46</td>
    </tr>
    <tr>
      <th>552</th>
      <td>Port Alfred</td>
      <td>0</td>
      <td>ZA</td>
      <td>1520906936</td>
      <td>84</td>
      <td>-33.59</td>
      <td>26.89</td>
      <td>21.92</td>
      <td>9.36</td>
    </tr>
    <tr>
      <th>553</th>
      <td>Esperance</td>
      <td>20</td>
      <td>TT</td>
      <td>1520902800</td>
      <td>78</td>
      <td>10.24</td>
      <td>-61.45</td>
      <td>25.00</td>
      <td>2.10</td>
    </tr>
    <tr>
      <th>554</th>
      <td>Bonavista</td>
      <td>0</td>
      <td>CA</td>
      <td>1520907195</td>
      <td>85</td>
      <td>48.65</td>
      <td>-53.11</td>
      <td>-0.33</td>
      <td>8.06</td>
    </tr>
    <tr>
      <th>555</th>
      <td>Bolobo</td>
      <td>36</td>
      <td>CD</td>
      <td>1520907195</td>
      <td>97</td>
      <td>-2.17</td>
      <td>16.23</td>
      <td>22.97</td>
      <td>1.21</td>
    </tr>
  </tbody>
</table>
<p>556 rows × 9 columns</p>
</div>




```python
# Write the dataframe to a .csv
file_name = 'City_results.csv'
CityResults_df.to_csv(file_name, encoding='utf-8', index=False)



```


```python
# set the date
currentdate = '03/13/2018'

# Scatter Plots - Temperature (F) vs. Latitude
x_axis = CityResults_df['Lat']
y_axis = CityResults_df['Max Temp']
TempVsLat = plt.scatter(x_axis, y_axis, marker="o", facecolors= 'blue', edgecolors='black',
            s=50, alpha=0.40)

plt.xlim(-90, 90)
plt.ylim(-100, 150)

plt.title('City Latitude vs. Max Temperature (' + currentdate + ')')
plt.xlabel('Latitude')
plt.ylabel('Max Temperature (F)')

plt.savefig('TempVsLat.png')
```


![png](output_8_0.png)



```python
# Scatter Plots - Humidity (%) vs. Latitude
x_axis = CityResults_df['Lat']
y_axis = CityResults_df['Humidity']
HumidityVsLat = plt.scatter(x_axis, y_axis, marker="o", facecolors= 'blue', edgecolors='black',
            s=50, alpha=0.40)

plt.xlim(-90, 90)
plt.ylim(-5, 105)

plt.title('City Latitude vs. Humidity (' + currentdate + ')')
plt.xlabel('Latitude')
plt.ylabel('Humidity (%)')

plt.savefig('HumidityVsLat.png')
```


![png](output_9_0.png)



```python
# Scatter Plots - Cloudiness (%) vs. Latitude
x_axis = CityResults_df['Lat']
y_axis = CityResults_df['Cloudiness']
CloudVsLat = plt.scatter(x_axis, y_axis, marker="o", facecolors= 'blue', edgecolors='black',
            s=50, alpha=0.40)

plt.xlim(-90, 90)
plt.ylim(-5, 105)

plt.title('City Latitude vs. Cloudiness (' + currentdate + ')')
plt.xlabel('Latitude')
plt.ylabel('Cloudiness (%)')

plt.savefig('CloudVsLat.png')
```


![png](output_10_0.png)



```python
# Scatter Plots - Wind Speed (mph) vs. Latitude
x_axis = CityResults_df['Lat']
y_axis = CityResults_df['Wind Speed']
WindVsLat = plt.scatter(x_axis, y_axis, marker="o", facecolors= 'blue', edgecolors='black',
            s=50, alpha=0.40)

plt.xlim(-90, 90)
plt.ylim(-5, 40)

plt.title('City Latitude vs. Wind Speed (' + currentdate + ')')
plt.xlabel('Latitude')
plt.ylabel('Wind Speed (mph)')

plt.savefig('WindVsLat.png')
```


![png](output_11_0.png)



```python
#  Your final notebook must:
#  • Randomly select at least 500 unique (non-repeat) cities based on latitude and longitude.
#  • Perform a weather check on each of the cities using a series of successive API calls.
#  • Include a print log of each city as it's being processed with the city number, city name, 
#    and requested URL.
#  • Save both a CSV of all data retrieved and png images for each scatter plot.

#  As final considerations:
#  • You must use the Matplotlib and Seaborn libraries.
#  • You must include a written description of three observable trends based on the data.
#  • You must use proper labeling of your plots, including aspects like: Plot Titles (with date 
#    of analysis) and Axes Labels.
#  • You must include an exported markdown version of your Notebook called README.md in your 
#    GitHub repository.
#  • See Example Solution for a reference on expected format.

#  Hints and Considerations
#  • You may want to start this assignment by refreshing yourself on 4th grade geography, in 
#    particular, the geographic coordinate system.
#  • Next, spend the requisite time necessary to study the OpenWeatherMap API. Based on your
#    initial study, you should be able to answer basic questions about the API: Where do you
#    request the API key? Which Weather API in particular will you need? What URL endpoints
#    does it expect? What JSON structure does it respond with? Before you write a line of code,
#    you should be aiming to have a crystal clear understanding of your intended outcome.
#  • Though we've never worked with the citipy Python library, push yourself to decipher how 
#    it works, and why it might be relevant. Before you try to incorporate the library into your
#    analysis, start by creating simple test cases outside your main script to confirm that you 
#    are using it correctly. Too often, when introduced to a new library, students get bogged 
#    down by the most minor of errors -- spending hours investigating their entire code -- when,
#    in fact, a simple and focused test would have shown their basic utilization of the library 
#    was wrong from the start. Don't let this be you!
#  • Part of our expectation in this challenge is that you will use critical thinking skills to 
#    understand how and why we're recommending the tools we are. What is Citipy for? Why would 
#    you use it in conjunction with the OpenWeatherMap API? How would you do so?
#  • In building your script, pay attention to the cities you are using in your query pool. Are 
#    you getting coverage of the full gamut of latitudes and longitudes? Or are you simply choosing
#    500 cities concentrated in one region of the world? Even if you were a geographic genius, 
#    simply rattling 500 cities based on your human selection would create a biased dataset. Be 
#    thinking of how you should counter this. (Hint: Consider the full range of latitudes).
#  • Lastly, remember -- this is a challenging activity. Push yourself! If you complete this task, 
#    then you can safely say that you've gained a strong mastery of the core foundations of data 
#    analytics and it will only go better from here. Good luck!
```


```python
# Generate a Sample Cities List
#create a sample file for creating the plots
#ResultsColumnNames = ['City', 'Cloudiness', 'Country', 'Date', 'Humidity', 'Lat', 'Lng', 'Max Temp', 'Wind Speed']
# Populate the sample columns
#CityList = ['longyearbyen', 'Asau', 'hartselle', 'komsomolskiy', 'kapaa']
#CloudinessList = [75, 0, 1, 40, 90]
#CountryList = ['SJ','RO', 'US','UZ', 'US']
#DateList = [1483588200, 1483592400, 1483592280, 1483592400, 1483592160]
#HumidityList = [73, 59, 86, 80, 88]
#LatList = [78.22, 46.43, 34.44, 40.43, 22.08]
#LngList = [15.64, 26.40, -86.94, 71.72, -159.32]
#MaxTempList = [26.6, 37.4, 32.0, 37.4, 71.6]
#WindSpeedList = [19.46, 14.99, 3.36, 3.36, 17.22]

# create a dataframe and insert the data
#CityResults_df = pd.DataFrame(columns=ResultsColumnNames) # Note that there are no rows of data inserted.
#Results_df['City'] = CityList
#Results_df['Cloudiness'] = CloudinessList
#Results_df['Country'] = CountryList
#Results_df['Date'] = DateList
#Results_df['Humidity'] = HumidityList
#Results_df['Lat'] = LatList
#Results_df['Lng'] = LngList
#Results_df['Max Temp'] = MaxTempList
#Results_df['Wind Speed'] = WindSpeedList
# Take a look:
#Results_df.head()

```
