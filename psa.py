import requests
from tkinter import *
import tkinter as tk
from datetime import *
import locale
from geopy.geocoders import Nominatim
import csv
from tkinter import messagebox


locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")

# Tela base
try:
   root=Tk()
   root.title('PSA')
   root.geometry('990x570+400+400')
   root.configure(bg='#EAC696')
   root.resizable(False, False)

   def mostrarjanelarelatorios():
    root.withdraw()  # Esconda a janela principal
    relatjanela.deiconify()  # Exiba a segunda janela

   def mostrarjaneladicas():
    root.withdraw()  # Esconda a janela principal
    dicasjanela.deiconify()  # 

   def voltartelainicial():
    relatjanela.withdraw()  # Esconda a segunda janela
    root.deiconify()  # Exiba a janela principal

   def atualizar_data():
    # Função para atualizar a data
    data_atual = datetime.now()
    data_formatada = data_atual.strftime("%d/%m/%Y -")
    dia_da_semana = data_atual.strftime(" %A")

    hora_atual = datetime.now().strftime("%H:%M")
    label_hora.config(text=hora_atual, fg='black', bg='#EAC696')
    label_data.config(text=data_formatada + dia_da_semana, fg='black', bg='#EAC696')
    root.after(1000, atualizar_data) 

   def zonatempo():
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

    # Tratando os dados coletados
    Temperatura = "{:.2f}".format(Temperaturabruta)

    tempolab.config(text=(Tempo))
    temperaturalab.config(text=(Temperatura, '°C'))
    umidadelab.config(text=(Umidade, '%'))
    latitudelab.config(text=(Latitude))
    longitudelab.config(text=(Longitude))

   def relatorios():
    response = requests.get("https://ipinfo.io")
    data = response.json()

    if "loc" in data:
     Latitude, Longitude = data["loc"].split(",")
    else:
     print("Não foi possível obter as coordenadas de latitude e longitude.")

    API_KEY = '0673f6221928f8d92ba0dd51c09a1409'
    LinkTempoAtual = f'https://api.openweathermap.org/data/2.5/weather?lat={Latitude}&lon={Longitude}&appid={API_KEY}&lang=pt'

   # Convertendo a localização em um estado
    def coordenadas_para_estado(Latitude, Longitude):
     geolocator = Nominatim(user_agent="geoapiExercises")
     localizacao = geolocator.reverse(f"{Latitude}, {Longitude}", exactly_one=True)
    
     if localizacao:
         endereco = localizacao.raw['address']
         Estado = endereco.get('state', '')
         return Estado
     else:
         return None

    Estado = coordenadas_para_estado(Latitude, Longitude)

    # Pegando a previsão do tempo atual
    Requisicao = requests.get(LinkTempoAtual)
    Requisicao_dic = Requisicao.json()

    # Criando as variáveis para o tempo atual
    Tempo = Requisicao_dic['weather'][0]['description']
    Temperaturabruta = Requisicao_dic['main']['temp']-273.15
    Umidade = Requisicao_dic['main']['humidity']

    # Tratando os dados coletados
    Temperatura = "{:.2f}".format(Temperaturabruta)
 
    tempolabrelatorio.config(text=('Tempo: ' + Tempo))
    temperaturalabrelatorio.config(text=('Temperatura:', Temperatura, '°C'))
    umidadelabrelatorio.config(text=('Umidade:', Umidade, '%'))
    latitudelabrelatorio.config(text=('Latitude:', Latitude))
    longitudelabrelatorio.config(text=('Longitude:', Longitude))
    estadolabrelatorio.config(text=('Estado: ' + Estado))
    
    data_atual = datetime.now()
    mes = data_atual.strftime("%m")
    
    data_formatada = data_atual.strftime("Data: %d/%m/%Y -")
    dia_da_semana = data_atual.strftime(" %A")

    hora_atual = datetime.now().strftime("%H:%M")
    horalabrelatorio.config(text=('Hora:', hora_atual), fg='black', bg='#765827')
    datalabrelatorio.config(text=(data_formatada, dia_da_semana), fg='black', bg='#765827')

    data_relatorio = data_atual.strftime("%d/%m/%Y")
    dia_relatorio = data_atual.strftime("%A")
    # Teste para ver recomendação do plantio

    momento_para_plantio = "" 
    motivolinha1 = ""
    motivolinha2 = ""
    motivolinha3 = ""
    motivolinha4 = ""
    motivolinha5 = ""
    motivo = ""

    if (mes == '01' or mes == '02' or mes == '07' or mes == '08' or mes == '12') and (Estado == "Acre" or Estado == "Roraima" or Estado == "Amapá" or Estado == "Amazonas" or Estado == "Rondônia"):
      momento_para_plantio = "Condições ruins:"
      motivolinha1 = "O local onde o plantio será realizado"
      motivolinha2 = "não é bom para o amendoim."
      motivolinha3 = "Além disso, não estamos num momento"
      motivolinha4 = "adequado para o plantio desta cultura."
      motivolinha5 = ""
      motivo = "O local onde o plantio será realizado não é bom para o amendoim. Além disso, não estamos num momento adequado para o plantio desta cultura."
    
    elif (mes == '03' or mes == '04' or mes == '09' or mes == '10') and (Estado == "Acre" or Estado == "Roraima" or Estado == "Amapá" or Estado == "Amazonas" or Estado == "Rondônia"):
      momento_para_plantio = "Condições medianas:"
      motivolinha1 = "O local onde o plantio será realizado"
      motivolinha2 = "é ruim para o amendoim, mas é uma boa"
      motivolinha3 = "época para esta cultura. É necessário"
      motivolinha4 = "uma análise mais profunda com um"
      motivolinha5 = "profissional antes de começar a plantar."
      motivo = "O local onde o plantio será realizado é ruim para o amendoim, mas é uma boa época para esta cultura. É necessário uma análise mais profunda com um profissional antes de começar a plantar."

    elif (mes == '01' or mes == '02' or mes == '07' or mes == '08' or mes == '12') and (Estado == "Bahia" or Estado == "Pernambuco" or Estado == "Maranhão" or Estado == "Piauí" or Estado == "Ceará"):
      momento_para_plantio = "Condições medianas:"
      motivolinha1 = "O local onde o plantio será realizado"
      motivolinha2 = "é bom para o amendoim, mas é uma péssima"
      motivolinha3 = "época para esta cultura. É recomendável"
      motivolinha4 = "esperar uma época melhor para começar a"
      motivolinha5 = "plantar."
      motivo = "O local onde o plantio será realizado é bom para o amendoim, mas é uma péssima época para esta cultura. É recomendável esperar uma época melhor para começar a plantar."

    elif (mes == '01' or mes == '02' or mes == '07' or mes == '08' or mes == '12') and (Estado == "São Paulo" or Estado == "Minas Gerais" or Estado == "Goiás" or Estado == "Mato Grosso do Sul" or Estado == "Santa Catarina"):
      momento_para_plantio = "Condições medianas:"
      motivolinha1 = "O local onde o plantio será realizado"
      motivolinha2 = "é excelente para o amendoim, mas é uma"
      motivolinha3 = "péssima época para esta cultura."
      motivolinha4 = "É recomendável esperar uma época melhor"
      motivolinha5 = "para começar a plantar."
      motivo = "O local onde o plantio será realizado é excelente para o amendoim, mas é uma péssima época para esta cultura. É recomendável esperar uma época melhor para começar a plantar."

    elif (mes == '05' or mes == '06' or mes == '11') and (Estado == "Acre" or Estado == "Roraima" or Estado == "Amapá" or Estado == "Amazonas" or Estado == "Rondônia"):
      momento_para_plantio = "Condições medianas:"
      motivolinha1 = "O local onde o plantio será realizado"
      motivolinha2 = "é ruim para o amendoim, mas é uma"
      motivolinha3 = "excelente época para esta cultura."
      motivolinha4 = "É necessário uma análise mais profunda com"
      motivolinha5 = "um profissional antes de começar a plantar."
      motivo = "O local onde o plantio será realizado é ruim para o amendoim, mas é uma excelente época para esta cultura. É necessário uma análise mais profunda com um profissional antes de começar a plantar."

    elif (mes == '03' or mes == '04' or mes == '09' or mes == '10') and (Estado == "Bahia" or Estado == "Pernambuco" or Estado == "Maranhão" or Estado == "Piauí" or Estado == "Ceará"):
      momento_para_plantio = "Condições boas:"
      motivolinha1 = "O local onde o plantio será realizado"
      motivolinha2 = "é bom para o amendoim, e é uma boa"
      motivolinha3 = "época para esta cultura."
      motivolinha4 = "É um bom momento para começar a"
      motivolinha5 = "plantar!"
      motivo = "O local onde o plantio será realizado é bom para o amendoim, e é uma boa época para esta cultura. É um bom momento para começar a plantar!"

    elif (mes == '03' or mes == '04' or mes == '09' or mes == '10') and (Estado == "São Paulo" or Estado == "Minas Gerais" or Estado == "Goiás" or Estado == "Mato Grosso do Sul" or Estado == "Santa Catarina"):
      momento_para_plantio = "Condições muito boas:"
      motivolinha1 = "O local onde o plantio será realizado"
      motivolinha2 = "é excelente para o amendoim, e é "
      motivolinha3 = "uma boa época para esta cultura."
      motivolinha4 = "É um ótimo momento para começar"
      motivolinha5 = "a plantar!"
      motivo = "O local onde o plantio será realizado é excelente para o amendoim, e é uma boa época para esta cultura. É um ótimo momento para começar a plantar!"

    elif (mes == '05' or mes == '06' or mes == '11') and (Estado == "Bahia" or Estado == "Pernambuco" or Estado == "Maranhão" or Estado == "Piauí" or Estado == "Ceará"):
      momento_para_plantio = "Condições muito boas:"
      motivolinha1 = "O local onde o plantio será realizado"
      motivolinha2 = "é bom para o amendoim, e é a melhor"
      motivolinha3 = "época para esta cultura."
      motivolinha4 = "É um ótimo momento para começar"
      motivolinha5 = "a plantar!"
      motivo = "O local onde o plantio será realizado é bom para o amendoim, e é a melhor época para esta cultura. É um ótimo momento para começar a plantar!"

    elif (mes == '05' or mes == '06' or mes == '11') and (Estado == "São Paulo" or Estado == "Minas Gerais" or Estado == "Goiás" or Estado == "Mato Grosso do Sul" or Estado == "Santa Catarina"):
      momento_para_plantio = "Condições perfeitas:"
      motivolinha1 = "O local onde o plantio será realizado"
      motivolinha2 = "é excelente para o amendoim, e o"
      motivolinha3 = "momento é perfeito para o plantio."
      motivolinha4 = "Essas são as melhores condições"
      motivolinha5 = "possíveis para começar a plantar!"
      motivo = "O local onde o plantio será realizado é excelente para o amendoim, e o momento é perfeito para o plantio. Essas são as melhores condições possíveis para começar a plantar!"

    else: 
      momento_para_plantio = "Condições desconhecidas"

    momentoplantiolab.config(text=(momento_para_plantio))
    motivoplantiolab1.config(text=(motivolinha1))
    motivoplantiolab2.config(text=(motivolinha2))
    motivoplantiolab3.config(text=(motivolinha3))
    motivoplantiolab4.config(text=(motivolinha4))
    motivoplantiolab5.config(text=(motivolinha5))

    tempolabrelatoriogeral.config(text=('Tempo: ' + Tempo))
    temperaturalabrelatoriogeral.config(text=('Temperatura:', Temperatura, '°C'))
    umidadelabrelatoriogeral.config(text=('Umidade:', Umidade, '%'))
    latitudelabrelatoriogeral.config(text=('Latitude:', Latitude))
    longitudelabrelatoriogeral.config(text=('Longitude:', Longitude))
    estadolabrelatoriogeral.config(text=('Estado: ' + Estado))
    horalabrelatoriogeral.config(text=('Hora:', hora_atual), fg='black', bg='#765827')
    datalabrelatoriogeral.config(text=(data_formatada + dia_da_semana), fg='black', bg='#765827')

    try:
        with open("relatorio", 'w', newline='') as arquivo_csv:
          escritor = csv.writer(arquivo_csv)
          escritor.writerow([data_relatorio, dia_relatorio, Tempo, Temperatura, Umidade, Latitude, Longitude, Estado, momento_para_plantio, motivo])

        messagebox.showinfo('Sucesso', 'Relatórios exportados para o arquivo relatorios.csv com sucesso!')
    except Exception as e:
        messagebox.showerror('Erro', f'Ocorreu um erro ao exportar o relatório: {e}')

   # Tela inicial
   dadostempobot = tk.Button(root, text="Capturar informações", command=zonatempo)
   dadostempobot.pack()
   dadostempobot.place(x=50, y=300)

   relatbotao = tk.Button(root, text="Analise de campo", command=mostrarjanelarelatorios)
   relatbotao.pack()
   relatbotao.place(x=829, y=300)

   dicasbotao = tk.Button(root, text=" Dicas de manejo ", command=mostrarjaneladicas)
   dicasbotao.pack()
   dicasbotao.place(x=829, y=265)

   pesquisaarea = tk.Canvas(root, width=1500, height=110)
   pesquisaarea.place(x=0, y=0)
   pesquisaarea.create_rectangle (0, 0, 986, 500, fill="#765827", width=2)

   label1=Label(root, text='Tempo', font=('Helvetica', 13, 'bold'), fg='black', bg='#EAC696')
   label1.place(x=50, y=140)

   label2=Label(root, text='Temperatura', font=('Helvetica', 13, 'bold'), fg='black', bg='#EAC696')
   label2.place(x=50, y=170)

   label3=Label(root, text='Umidade', font=('Helvetica', 13, 'bold'), fg='black', bg='#EAC696')
   label3.place(x=50, y=200)

   label4=Label(root, text='Latitude', font=('Helvetica', 13, 'bold'), fg='black', bg='#EAC696')
   label4.place(x=50, y=230)

   label5=Label(root, text='Longitude', font=('Helvetica', 13, 'bold'), fg='black', bg='#EAC696')
   label5.place(x=50, y=260)

   tempolab = Label(root, font=('Helvetica', 13, 'bold'), fg='black', bg='#EAC696')
   tempolab.place(x=170, y=140)

   temperaturalab = Label(root, font=('Helvetica', 13, 'bold'), fg='black', bg='#EAC696')
   temperaturalab.place(x=170, y=170)

   umidadelab = Label(root, font=('Helvetica', 13, 'bold'), fg='black', bg='#EAC696')
   umidadelab.place(x=170, y=200)

   latitudelab = Label(root, font=('Helvetica', 13, 'bold'), fg='black', bg='#EAC696')
   latitudelab.place(x=170, y=230)

   longitudelab = Label(root, font=('Helvetica', 13, 'bold'), fg='black', bg='#EAC696')
   longitudelab.place(x=170, y=260)




   previsaoarea = tk.Canvas(root, width=160, height=200)
   previsaoarea.place(x=50, y=350)
   previsaoarea.create_rectangle (0.5, 0.5, 200, 200, fill="#765827")

   previsaoarea2 = tk.Canvas(root, width=160, height=200)
   previsaoarea2.place(x=230, y=350)
   previsaoarea2.create_rectangle (0.5, 0.5, 200, 200, fill="#765827")

   previsaoarea3 = tk.Canvas(root, width=160, height=200)
   previsaoarea3.place(x=410, y=350)
   previsaoarea3.create_rectangle (0.5, 0.5, 200, 200, fill="#765827")

   previsaoarea4 = tk.Canvas(root, width=160, height=200)
   previsaoarea4.place(x=590, y=350)
   previsaoarea4.create_rectangle (0.5, 0.5, 200, 200, fill="#765827")

   previsaoarea5 = tk.Canvas(root, width=160, height=200)
   previsaoarea5.place(x=770, y=350)
   previsaoarea5.create_rectangle (0.5, 0.5, 200, 200, fill="#765827")

   label_data = tk.Label(root, text="", font=("Helvetica", 16))
   label_hora = tk.Label(root, text="", font=("Helvetica", 30))
   label_data.place(x=727, y=125)
   label_hora.place(x=835, y=160)
   atualizar_data()











   # Tela de relatórios
   relatjanela = tk.Toplevel(root)
   relatjanela.title("PSA")
   relatjanela.withdraw() 
   relatjanela.geometry('990x570+400+400')
   relatjanela.configure(bg='#EAC696')
   relatjanela.resizable(False, False)

   pesquisaarea = tk.Canvas(relatjanela, width=1500, height=110)
   pesquisaarea.place(x=0, y=0)
   pesquisaarea.create_rectangle (0, 0, 986, 500, fill="#765827", width=2)

   botaoinicio = tk.Button(relatjanela, text="Voltar para Janela Principal", command=voltartelainicial)
   botaoinicio.place(x=25, y=350)

   botaorelatorio = tk.Button(relatjanela, text="Gerar relatórios", command=relatorios)
   botaorelatorio.pack()
   botaorelatorio.place(x=25, y=300)


   relatoriolocal = tk.Canvas(relatjanela, width=260, height=390)
   relatoriolocal.place(x=200, y=150)
   relatoriolocal.create_rectangle (0.5, 0.5, 400, 400, fill="#765827")
   labelrelatoriolocal=Label(relatjanela, text='Relatório do local', font=('Helvetica', 16, 'bold'), fg='Black', bg='#765827')
   labelrelatoriolocal.place(x=240, y=170)

   relatoriogeral = tk.Canvas(relatjanela, width=260, height=390)
   relatoriogeral.place(x=540, y=150)
   relatoriogeral.create_rectangle (0.5, 0.5, 400, 400, fill="#765827")
   labelrelatoriogeral=Label(relatjanela, text='Relatório Geral', font=('Helvetica', 16, 'bold'), fg='Black', bg='#765827')
   labelrelatoriogeral.place(x=595, y=170)


# Relatório Local

   datalabrelatorio = Label(relatjanela, font=('Helvetica', 13), fg='black', bg='#765827')
   datalabrelatorio.place(x=215, y=200)

   horalabrelatorio = tk.Label(relatjanela, text="", font=("Helvetica", 13), fg='black', bg='#765827')
   horalabrelatorio.place(x=215, y=225)

   tempolabrelatorio = Label(relatjanela, font=('Helvetica', 13), fg='black', bg='#765827')
   tempolabrelatorio.place(x=215, y=250)

   temperaturalabrelatorio = Label(relatjanela, font=('Helvetica', 13), fg='black', bg='#765827')
   temperaturalabrelatorio.place(x=215, y=275)

   umidadelabrelatorio = Label(relatjanela, font=('Helvetica', 13), fg='black', bg='#765827')
   umidadelabrelatorio.place(x=215, y=300)

   latitudelabrelatorio = Label(relatjanela, font=('Helvetica', 13), fg='black', bg='#765827')
   latitudelabrelatorio.place(x=215, y=325)

   longitudelabrelatorio = Label(relatjanela, font=('Helvetica', 13), fg='black', bg='#765827')
   longitudelabrelatorio.place(x=215, y=350)

   estadolabrelatorio = Label(relatjanela, font=('Helvetica', 13), fg='black', bg='#765827')
   estadolabrelatorio.place(x=215, y=375)



# Relatório Geral

   datalabrelatoriogeral = Label(relatjanela, font=('Helvetica', 13), fg='black', bg='#765827')
   datalabrelatoriogeral.place(x=555, y=200)

   horalabrelatoriogeral = tk.Label(relatjanela, text="", font=("Helvetica", 13), fg='black', bg='#765827')
   horalabrelatoriogeral.place(x=555, y=225)

   tempolabrelatoriogeral = Label(relatjanela, font=('Helvetica', 13), fg='black', bg='#765827')
   tempolabrelatoriogeral.place(x=555, y=250)

   temperaturalabrelatoriogeral = Label(relatjanela, font=('Helvetica', 13), fg='black', bg='#765827')
   temperaturalabrelatoriogeral.place(x=555, y=275)

   umidadelabrelatoriogeral = Label(relatjanela, font=('Helvetica', 13), fg='black', bg='#765827')
   umidadelabrelatoriogeral.place(x=555, y=300)

   latitudelabrelatoriogeral = Label(relatjanela, font=('Helvetica', 13), fg='black', bg='#765827')
   latitudelabrelatoriogeral.place(x=555, y=325)

   longitudelabrelatoriogeral = Label(relatjanela, font=('Helvetica', 13), fg='black', bg='#765827')
   longitudelabrelatoriogeral.place(x=555, y=350)

   estadolabrelatoriogeral = Label(relatjanela, font=('Helvetica', 13), fg='black', bg='#765827')
   estadolabrelatoriogeral.place(x=555, y=375)

   momentoplantiolab = Label(relatjanela, font=('Helvetica', 13, 'bold'), fg='black', bg='#765827')
   momentoplantiolab.place(x=555, y=400)

   motivoplantiolab1 = Label(relatjanela, font=('Helvetica', 10), fg='black', bg='#765827')
   motivoplantiolab1.place(x=555, y=420)
   motivoplantiolab2 = Label(relatjanela, font=('Helvetica', 10), fg='black', bg='#765827')
   motivoplantiolab2.place(x=555, y=440)
   motivoplantiolab3 = Label(relatjanela, font=('Helvetica', 10), fg='black', bg='#765827')
   motivoplantiolab3.place(x=555, y=460)
   motivoplantiolab4 = Label(relatjanela, font=('Helvetica', 10), fg='black', bg='#765827')
   motivoplantiolab4.place(x=555, y=480)
   motivoplantiolab5 = Label(relatjanela, font=('Helvetica', 10), fg='black', bg='#765827')
   motivoplantiolab5.place(x=555, y=500)


# Tela de dicas
   dicasjanela = tk.Toplevel(root)
   dicasjanela.title("PSA")
   dicasjanela.withdraw() 
   dicasjanela.geometry('990x570+400+400')
   dicasjanela.configure(bg='#EAC696')
   dicasjanela.resizable(False, False)

   pesquisaarea = tk.Canvas(dicasjanela, width=1500, height=110)
   pesquisaarea.place(x=0, y=0)
   pesquisaarea.create_rectangle (0, 0, 986, 500, fill="#765827", width=2)

   botaoinicio = tk.Button(dicasjanela, text="Voltar para Janela Principal", command=voltartelainicial)
   botaoinicio.place(x=770, y=405)

# ============Fileira 1

   dica1quadro = tk.Canvas(dicasjanela, width=200, height=100)
   dica1quadro.place(x=50, y=150)
   dica1quadro.create_rectangle (0.5, 0.5, 210, 110, fill="#765827")
   labeldica1=Label(dicasjanela, text='Preparação do solo', font=('Helvetica', 12, 'bold'), fg='Black', bg='#765827')
   labeldica1.place(x=75, y=165)
   botaodica1 = tk.Button(dicasjanela, text="Ver dica")
   botaodica1.place(x=127, y=210)

   dica2quadro = tk.Canvas(dicasjanela, width=200, height=100)
   dica2quadro.place(x=280, y=150)
   dica2quadro.create_rectangle (0.5, 0.5, 210, 110, fill="#765827")
   labeldica2=Label(dicasjanela, text='Seleção de sementes', font=('Helvetica', 12, 'bold'), fg='Black', bg='#765827')
   labeldica2.place(x=300, y=165)
   botaodica2 = tk.Button(dicasjanela, text="Ver dica")
   botaodica2.place(x=357, y=210)

   dica3quadro = tk.Canvas(dicasjanela, width=200, height=100)
   dica3quadro.place(x=510, y=150)
   dica3quadro.create_rectangle (0.5, 0.5, 210, 110, fill="#765827")
   labeldica3=Label(dicasjanela, text='Cultivares porte ereto', font=('Helvetica', 12, 'bold'), fg='Black', bg='#765827')
   labeldica3.place(x=525, y=165)
   botaodica3 = tk.Button(dicasjanela, text="Ver dica")
   botaodica3.place(x=587, y=210)

   dica4quadro = tk.Canvas(dicasjanela, width=200, height=100)
   dica4quadro.place(x=740, y=150)
   dica4quadro.create_rectangle (0.5, 0.5, 210, 110, fill="#765827")
   labeldica4=Label(dicasjanela, text='Cultivares porte rasteiro', font=('Helvetica', 12, 'bold'), fg='Black', bg='#765827')
   labeldica4.place(x=747, y=165)
   botaodica4 = tk.Button(dicasjanela, text="Ver dica")
   botaodica4.place(x=817, y=210)

# ============Fileira 2

   dica5quadro = tk.Canvas(dicasjanela, width=200, height=100)
   dica5quadro.place(x=50, y=270)
   dica5quadro.create_rectangle (0.5, 0.5, 210, 110, fill="#765827")
   labeldica5=Label(dicasjanela, text='Plantio', font=('Helvetica', 12, 'bold'), fg='Black', bg='#765827')
   labeldica5.place(x=124, y=285)
   botaodica5 = tk.Button(dicasjanela, text="Ver dica")
   botaodica5.place(x=127, y=330)

   dica6quadro = tk.Canvas(dicasjanela, width=200, height=100)
   dica6quadro.place(x=280, y=270)
   dica6quadro.create_rectangle (0.5, 0.5, 210, 110, fill="#765827")
   labeldica6=Label(dicasjanela, text='Irrigação', font=('Helvetica', 12, 'bold'), fg='Black', bg='#765827')
   labeldica6.place(x=344, y=285)
   botaodica6 = tk.Button(dicasjanela, text="Ver dica")
   botaodica6.place(x=357, y=330)
   
   dica7quadro = tk.Canvas(dicasjanela, width=200, height=100)
   dica7quadro.place(x=510, y=270)
   dica7quadro.create_rectangle (0.5, 0.5, 210, 110, fill="#765827")
   labeldica7=Label(dicasjanela, text='Adubagem', font=('Helvetica', 12, 'bold'), fg='Black', bg='#765827')
   labeldica7.place(x=565, y=285)
   botaodica7 = tk.Button(dicasjanela, text="Ver dica")
   botaodica7.place(x=587, y=330)

   dica8quadro = tk.Canvas(dicasjanela, width=200, height=100)
   dica8quadro.place(x=740, y=270)
   dica8quadro.create_rectangle (0.5, 0.5, 210, 110, fill="#765827")
   labeldica8=Label(dicasjanela, text='Controle de pragas', font=('Helvetica', 12, 'bold'), fg='Black', bg='#765827')
   labeldica8.place(x=765, y=285)
   botaodica8 = tk.Button(dicasjanela, text="Ver dica")
   botaodica8.place(x=817, y=330)

# ============Fileira 3

   dica9quadro = tk.Canvas(dicasjanela, width=200, height=100)
   dica9quadro.place(x=50, y=390)
   dica9quadro.create_rectangle (0.5, 0.5, 210, 110, fill="#765827")
   labeldica9=Label(dicasjanela, text='Colheita', font=('Helvetica', 12, 'bold'), fg='Black', bg='#765827')
   labeldica9.place(x=120, y=405)
   botaodica9 = tk.Button(dicasjanela, text="Ver dica")
   botaodica9.place(x=127, y=450)

   dica10quadro = tk.Canvas(dicasjanela, width=200, height=100)
   dica10quadro.place(x=280, y=390)
   dica10quadro.create_rectangle (0.5, 0.5, 210, 110, fill="#765827")
   labeldica10=Label(dicasjanela, text='Pós-colheita', font=('Helvetica', 12, 'bold'), fg='Black', bg='#765827')
   labeldica10.place(x=335, y=405)
   botaodica10 = tk.Button(dicasjanela, text="Ver dica")
   botaodica10.place(x=357, y=450)
   
   dica11quadro = tk.Canvas(dicasjanela, width=200, height=100)
   dica11quadro.place(x=510, y=390)
   dica11quadro.create_rectangle (0.5, 0.5, 210, 110, fill="#765827")
   labeldica11=Label(dicasjanela, text='Variedades de amendoim', font=('Helvetica', 12, 'bold'), fg='Black', bg='#765827')
   labeldica11.place(x=513, y=405)
   botaodica11 = tk.Button(dicasjanela, text="Ver dica")
   botaodica11.place(x=587, y=450)


# Iniciando tela
   root.mainloop()
   
except Exception as e:
  messagebox.showerror('Erro', f'Ocorreu um erro ao iniciar o projeto: {e}')
