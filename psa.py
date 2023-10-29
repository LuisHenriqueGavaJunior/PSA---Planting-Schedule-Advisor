import requests
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from datetime import *
import locale

locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")

# Tela base
try:
   root=Tk()
   root.title('PSA')
   root.geometry('990x570+400+400')
   root.configure(bg='#203243')
   root.resizable(False, False)

   def mostrarjaneladicas():
    root.withdraw()  # Esconda a janela principal
    dicasjan.deiconify()  # Exiba a segunda janela

   def voltartelainicial():
    dicasjan.withdraw()  # Esconda a segunda janela
    root.deiconify()  # Exiba a janela principal

   def atualizar_data():
    # Função para atualizar a data
    data_atual = datetime.now()
    data_formatada = data_atual.strftime("%d/%m/%Y -")
    dia_da_semana = data_atual.strftime(" %A")

    hora_atual = datetime.now().strftime("%H:%M")
    label_hora.config(text=hora_atual, fg='white', bg='#203243')
    label_data.config(text=data_formatada + dia_da_semana, fg='white', bg='#203243')
    root.after(1000, atualizar_data) 

   def zonatempo():
   # Criando o botão para pegar as informações baseadas na localização do usuário

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
    umidadelab.config(text=(Umidade, '%'))
    latitudelab.config(text=(Latitude))
    longitudelab.config(text=(Longitude))


   # Tela inicial
   dadostempobot = tk.Button(root, text="Capturar informações por localização", command=zonatempo)
   dadostempobot.pack()
   dadostempobot.place(x=50, y=300)

   dicasbotao = tk.Button(root, text="Abrir Outra Janela", command=mostrarjaneladicas)
   dicasbotao.pack()
   dicasbotao.place(x=600, y=300)

   pesquisaarea = tk.Canvas(root, width=1500, height=110)
   pesquisaarea.place(x=0, y=0)
   pesquisaarea.create_rectangle (0, 0, 986, 500, fill="#203243", width=2)


   label1=Label(root, text='Tempo', font=('Helvetica', 13), fg='white', bg='#203243')
   label1.place(x=50, y=130)

   label2=Label(root, text='Temperatura', font=('Helvetica', 13), fg='white', bg='#203243')
   label2.place(x=50, y=160)

   label3=Label(root, text='Umidade', font=('Helvetica', 13), fg='white', bg='#203243')
   label3.place(x=50, y=190)

   label4=Label(root, text='Latitude', font=('Helvetica', 13), fg='white', bg='#203243')
   label4.place(x=50, y=220)

   label5=Label(root, text='Longitude', font=('Helvetica', 13), fg='white', bg='#203243')
   label5.place(x=50, y=250)

   tempolab = Label(root, font=('Helvetica', 13), fg='white', bg='#203243')
   tempolab.place(x=170, y=130)

   temperaturalab = Label(root, font=('Helvetica', 13), fg='white', bg='#203243')
   temperaturalab.place(x=170, y=160)

   umidadelab = Label(root, font=('Helvetica', 13), fg='white', bg='#203243')
   umidadelab.place(x=170, y=190)

   latitudelab = Label(root, font=('Helvetica', 13), fg='white', bg='#203243')
   latitudelab.place(x=170, y=220)

   longitudelab = Label(root, font=('Helvetica', 13), fg='white', bg='#203243')
   longitudelab.place(x=170, y=250)


   previsaoarea = tk.Canvas(root, width=160, height=200)
   previsaoarea.place(x=50, y=350)
   previsaoarea.create_rectangle (0.5, 0.5, 200, 200, fill="#14212e")

   previsaoarea2 = tk.Canvas(root, width=160, height=200)
   previsaoarea2.place(x=230, y=350)
   previsaoarea2.create_rectangle (0.5, 0.5, 200, 200, fill="#14212e")

   previsaoarea3 = tk.Canvas(root, width=160, height=200)
   previsaoarea3.place(x=410, y=350)
   previsaoarea3.create_rectangle (0.5, 0.5, 200, 200, fill="#14212e")

   previsaoarea4 = tk.Canvas(root, width=160, height=200)
   previsaoarea4.place(x=590, y=350)
   previsaoarea4.create_rectangle (0.5, 0.5, 200, 200, fill="#14212e")

   previsaoarea5 = tk.Canvas(root, width=160, height=200)
   previsaoarea5.place(x=770, y=350)
   previsaoarea5.create_rectangle (0.5, 0.5, 200, 200, fill="#14212e")

   label_data = tk.Label(root, text="", font=("Helvetica", 16))
   label_hora = tk.Label(root, text="", font=("Helvetica", 30))
   label_data.place(x=728, y=125)
   label_hora.place(x=835, y=160)
   atualizar_data()











   # Tela de dicas
   dicasjan = tk.Toplevel(root)
   dicasjan.title("PSA")
   dicasjan.withdraw() 
   dicasjan.geometry('990x570+400+400')
   dicasjan.configure(bg='#203243')
   dicasjan.resizable(False, False)

   titulodicas = tk.Label(dicasjan, text="Informações e dicas sobre a cultura do amendoim", font=('Helvetica', 11), fg='white', bg='#203243')
   titulodicas.place(x=280, y=10)

   pesquisaarea = tk.Canvas(dicasjan, width=1500, height=110)
   pesquisaarea.place(x=0, y=0)
   pesquisaarea.create_rectangle (0, 0, 986, 500, fill="#203243", width=2)

   botaoinicio = tk.Button(dicasjan, text="Voltar para Janela Principal", command=voltartelainicial)
   botaoinicio.place(x=25, y=350)

   relatoriolocal = tk.Canvas(dicasjan, width=260, height=390)
   relatoriolocal.place(x=200, y=150)
   relatoriolocal.create_rectangle (0.5, 0.5, 400, 400, fill="#14212e")
   labelrelatoriolocal=Label(dicasjan, text='Relatório do local', font=('Helvetica', 13), fg='white', bg='#203243')
   labelrelatoriolocal.place(x=200, y=170)

   relatoriogeral = tk.Canvas(dicasjan, width=260, height=390)
   relatoriogeral.place(x=540, y=150)
   relatoriogeral.create_rectangle (0.5, 0.5, 400, 400, fill="#14212e")
   labelrelatoriogeral=Label(dicasjan, text='Relatório Geral', font=('Helvetica', 13), fg='white', bg='#203243')
   labelrelatoriogeral.place(x=540, y=170)


# Iniciando tela
   root.mainloop()
   
except Exception as e:
   print(f"Ocorreu um erro: {e}")
