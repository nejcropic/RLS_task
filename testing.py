
from urllib.request import urlopen
from bs4 import BeautifulSoup




url = 'https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/en/observation_si/index.html'
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
url_list = []

for i in soup.find_all('a', href=True):
    if i['href'][-12:] == "history.html":
        url_list.append(i['href'])

print(url_list[0])
url = "https://meteo.arso.gov.si" + url_list[0]
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# temperature
temperature_list = []
for i in soup.find_all('td', {"class": "t"}):
    temperature_list.append(i.get_text())

# wind icon
wind_icon_list = []
for i in soup.find_all('td', {"class": "ff_val"}):
    wind_icon_list.append(i.get_text())
    """
    label = QLabel(self)
    pixmap = QPixmap('logo.png')
    label.setPixmap(pixmap)
    self.resize(pixmap.width(), pixmap.height())
    """

# wind speed
wind_speed_list = []
for i in soup.find_all('td', {"class": "ff_val"}):
    wind_speed_list.append(i.get_text())

# pressure
pressure_list = []
for i in soup.find_all('td', {"class": "msl"}):
    pressure_list.append(i.get_text())


local_database = {}
database = []
for i in range(len(temperature_list)):
    local_database = {"temperature": temperature_list[i],
                      "wind_direction": wind_icon_list[i],
                      "wind_speed": wind_speed_list[i],
                      "pressure": pressure_list[i]}
    database.append(local_database)

print(temperature_list)
print(wind_speed_list)
print(pressure_list)
"""for i in city.find_all('td', {"class": "t"}):
    self.temperature_list.append(i.get_text())

# get wind direction
for i in city.find_all('td', {"class": "ff_val"}):
    self.wind_icon_list.append(i.get_text())

# get wind speed
for i in city.find_all('td', {"class": "ff_val"}):
    self.wind_speed_list.append(i.get_text())

# get pressure
for i in city.find_all('td', {"class": "ff_val"}):
    self.pressure_list.append(i.get_text())"""