import requests
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from datetime import *
import pytz
from PIL import Image, ImageTk
from timezonefinder import TimezoneFinder

# Tela base
root=Tk()
root.title('PSA')
root.geometry('890x470+300+300')
root.configure(bg='#203243')
root.resizable(True, True)



def zonatempo():

   # cidade = textfield.get()

   # geolocator = Nominatim(user_agent='geoapi')
   # localizacao = geolocator.geocode(cidade)
   # obj = TimezoneFinder


   # Criando as variáveis iniciais
   API_KEY = '0673f6221928f8d92ba0dd51c09a1409'
   Latitude = '-22.108567370633455'
   Longitude = '-50.19557700423522'
   Link = f'https://api.openweathermap.org/data/2.5/weather?lat={Latitude}&lon={Longitude}&appid={API_KEY}'
   LinkPrevisao = f'https://api.openweathermap.org/data/2.5/forecast?lat={Latitude}&lon={Longitude}&appid={API_KEY}'
   
   # Pegando a previsão do tempo atual
   Requisicao = requests.get(Link)
   Requisicao_dic = Requisicao.json()

   # Criando as variáveis do tempo
   Tempo = Requisicao_dic['weather'][0]['description']
   Temperatura = Requisicao_dic['main']['temp']-273
   Umidade = Requisicao_dic['main']['humidity']

   tempolab.config(text=(Tempo))
   temperaturalab.config(text=(Temperatura, '°C'))
   umidadelab.config(text=(Umidade, '%'))

   # Traduzindo a variável 'Tempo' para português
   if Tempo == 'clear sky':
      Tempo = 'Céu limpo'
   elif Tempo == 'few clouds':
      Tempo = 'Com nuvens'
   elif Tempo == 'scattered clouds':
      Tempo = 'Parcialmente nublado'
   elif Tempo == 'overcast clouds':
      Tempo = 'Nublado'
   elif Tempo == 'shower rain':
      Tempo = 'Pancadas de chuva'
   elif Tempo == 'moderate rain':
      Tempo = 'Chuva moderada'
   elif Tempo == 'rain':
      Tempo = 'Chovendo'



label1=Label(root, text='Tempo', font=('Helvetica', 11), fg='white', bg='#203243')
label1.place(x=50, y=120)

label2=Label(root, text='Temperatura', font=('Helvetica', 11), fg='white', bg='#203243')
label2.place(x=50, y=140)

label3=Label(root, text='Umidade', font=('Helvetica', 11), fg='white', bg='#203243')
label3.place(x=50, y=160)

tempolab = Label(root, font=('Helvetica', 11), fg='white', bg='#203243')
tempolab.place(x=170, y=120)

temperaturalab = Label(root, font=('Helvetica', 11), fg='white', bg='#203243')
temperaturalab.place(x=170, y=140)

umidadelab = Label(root, font=('Helvetica', 11), fg='white', bg='#203243')
umidadelab.place(x=170, y=160)






# Iniciando tela
root.mainloop()

