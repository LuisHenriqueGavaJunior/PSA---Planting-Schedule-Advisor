import requests
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from datetime import *
import pytz
from PIL import Image, ImageTk


# Tela base

try:
   root=Tk()
   root.title('PSA')
   root.geometry('890x470+300+300')
   root.configure(bg='#203243')
   root.resizable(True, True)


   def zonatempo():

   # Criando as variáveis iniciais

    response = requests.get("https://ipinfo.io")
    data = response.json()

    if "loc" in data:
     Latitude, Longitude = data["loc"].split(",")
    else:
     print("Não foi possível obter as coordenadas de latitude e longitude.")

    API_KEY = '0673f6221928f8d92ba0dd51c09a1409'

    LinkTempoAtual = f'https://api.openweathermap.org/data/2.5/weather?lat={Latitude}&lon={Longitude}&appid={API_KEY}&lang=pt'
    LinkPrevisao = f'https://api.openweathermap.org/data/2.5/forecast?lat={Latitude}&lon={Longitude}&appid={API_KEY}&lang=pt'

   # Pegando a previsão do tempo atual
    Requisicao = requests.get(LinkTempoAtual)
    Requisicao_dic = Requisicao.json()

   # Criando as variáveis para o tempo atual
    Tempo = Requisicao_dic['weather'][0]['description']
    Temperaturabruta = Requisicao_dic['main']['temp']-273.15
    Umidade = Requisicao_dic['main']['humidity']



   # Pegando a previsão do tempo dos próximos dias
    Requisicao2 = requests.get(LinkPrevisao)
    Requisicao_dic2 = Requisicao2.json()

   # Criando as variáveis para a previsão do tempo
    InfosDias = {}

    for previsao in Requisicao_dic2['list']:
        # Obtenha a data da previsão
        data = previsao['dt_txt'].split()[0]

        # Obtenha a temperatura, umidade e descrição desta previsão
        TemperaturaPrev = previsao['main']['temp']-273.15
        UmidadePrev = previsao['main']['humidity']
        TempoPrev = previsao['weather'][0]['description']

        # Se a data ainda não estiver no dicionário, crie um dicionário vazio para o dia
        if data not in InfosDias:
            InfosDias[data] = {
                'temperature': [],
                'humidity': [],
                'description': set(),
            }

        # Adicione as informações à lista do dia
        InfosDias[data]['temperature'].append(TemperaturaPrev)
        InfosDias[data]['humidity'].append(UmidadePrev)
        InfosDias[data]['description'].add(TempoPrev)

    # Exiba as informações gerais de cada dia
    for data, info in InfosDias.items():
        TemperaturaMedia = sum(info['temperature']) / len(info['temperature'])
        UmidadeMedia = sum(info['humidity']) / len(info['humidity'])
        TempoMedio = ', '.join(info['description'])
        print(f'Dia: {data}')
        print(f'Temperatura Média: {TemperaturaMedia:.2f}°C')
        print(f'Umidade Média: {UmidadeMedia:.2f}%')
        print(f'Tempo durante o dia: {TempoMedio}\n')

   # Tratando os dados coletados
    Temperatura = "{:.2f}".format(Temperaturabruta)

    tempolab.config(text=(Tempo))
    temperaturalab.config(text=(Temperatura, '°C'))
    umidadelab.config(text=(Umidade,'%'))
    latitudelab.config(text=(Latitude))
    longitudelab.config(text=(Longitude))

   dadostempobot = tk.Button(root, text="Capturar informações", command=zonatempo)
   dadostempobot.pack()
   dadostempobot.place(x=50, y=260)

   label1=Label(root, text='Tempo', font=('Helvetica', 11), fg='white', bg='#203243')
   label1.place(x=50, y=120)

   label2=Label(root, text='Temperatura', font=('Helvetica', 11), fg='white', bg='#203243')
   label2.place(x=50, y=140)

   label3=Label(root, text='Umidade', font=('Helvetica', 11), fg='white', bg='#203243')
   label3.place(x=50, y=160)

   label4=Label(root, text='Latitude', font=('Helvetica', 11), fg='white', bg='#203243')
   label4.place(x=50, y=180)

   label5=Label(root, text='Longitude', font=('Helvetica', 11), fg='white', bg='#203243')
   label5.place(x=50, y=200)



   tempolab = Label(root, font=('Helvetica', 11), fg='white', bg='#203243')
   tempolab.place(x=170, y=120)

   temperaturalab = Label(root, font=('Helvetica', 11), fg='white', bg='#203243')
   temperaturalab.place(x=170, y=140)

   umidadelab = Label(root, font=('Helvetica', 11), fg='white', bg='#203243')
   umidadelab.place(x=170, y=160)

   latitudelab = Label(root, font=('Helvetica', 11), fg='white', bg='#203243')
   latitudelab.place(x=170, y=180)

   longitudelab = Label(root, font=('Helvetica', 11), fg='white', bg='#203243')
   longitudelab.place(x=170, y=200)
   



# Iniciando tela
   root.mainloop()
   
except Exception as e:
   print(f"Ocorreu um erro: {e}")
