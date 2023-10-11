import requests
import folium
from folium.plugins import LocateControl
# from geolocation.main import GoogleMaps
# from geolocation.distance_matrix.client import DistanceMatrixApiClient

# Instalar bibliotecas na máquina
# py -m pip install requests
# py -m pip install folium
# py -m pip install geolocation-python

# Criando as variáveis iniciais
API_KEY = '0673f6221928f8d92ba0dd51c09a1409'
Latitude = '-22.108567370633455'
Longitude = '-50.19557700423522'
Link = f'https://api.openweathermap.org/data/2.5/weather?lat={Latitude}&lon={Longitude}&appid={API_KEY}'
LinkPrevisao = f'https://api.openweathermap.org/data/2.5/forecast?lat={Latitude}&lon={Longitude}&appid={API_KEY}'
# google_maps = GoogleMaps(api_key='')


# Criando o mapa com a biblioteca Folium
# Criando uma marcação no mapa com o método Marker a partir da latitude e longitude do usuário
Mapa = folium.Map([-16.46, -54.70], zoom_start=5)
LocateControl(auto_start = True, drawMaker = True, markerStyle = dict(color = 'green', weight = 10, opacity = 1, radius = 20)).add_to(Mapa)

# folium.Marker([Latitude, Longitude], tooltip='Você está aqui').add_to(Mapa)


# Pegando a previsão do tempo atual
Requisicao = requests.get(Link)
Requisicao_dic = Requisicao.json()

# Criando as variáveis do tempo
Tempo = Requisicao_dic['weather'][0]['description']
Temperatura = Requisicao_dic['main']['temp']-273
Umidade = Requisicao_dic['main']['humidity']
Vento = Requisicao_dic['wind']['speed']

# Traduzindo a variável 'Tempo' para português
if Tempo == 'clear sky':
  Tempo = 'Céu limpo'

elif Tempo == 'few clouds':
   Tempo = 'Com nuvens'

elif Tempo == 'scattered clouds':
   Tempo = 'Parcialmente nublado'

elif Tempo == 'broken clouds':
   Tempo = 'Nublado'

elif Tempo == 'shower rain':
   Tempo = 'Pancadas de chuva'

elif Tempo == 'moderate rain':
   Tempo = 'Chuva moderada'

elif Tempo == 'rain':
   Tempo = 'Chovendo'

# Exibindo as informações obtidas pelo WebBot e pelo Folium
print('Tempo:', Tempo)
print(f'Temperatura: {Temperatura:.2f}')
print('Umidade:', Umidade)
print('Vento:', Vento)
Mapa




# print(Requisicao_dic)

# Pegando a previsão dos próximos 5 dias
# requisicaoprevisao = requests.get(LinkPrevisao)
# previsao = requisicaoprevisao.json()
# print(previsao)