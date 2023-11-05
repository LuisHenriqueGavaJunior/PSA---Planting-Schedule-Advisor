import requests
from tkinter import *
import tkinter as tk
from datetime import *
import locale
from geopy.geocoders import Nominatim
import csv
from tkinter import messagebox
from tkinter import ttk


locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')

# Tela base
try:
   root=Tk()
   root.title('PSA')
   root.geometry('990x570+400+400')
   root.configure(bg='#EAC696')
   root.resizable(False, False)
   icone = tk.PhotoImage(file="imagens/icone.ppm")
   root.iconphoto(True, icone)



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
    LinkPrevisao = f'http://api.openweathermap.org/data/2.5/forecast?lat={Latitude}&lon={Longitude}&appid={API_KEY}&lang=pt'


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
        


    # Previsão do tempo dos próximos 5 dias
    RequisicaoPrev = requests.get(LinkPrevisao)
    RequisicaoPrev_dic = RequisicaoPrev.json()

    dia1 = datetime.now()

    # ====================== Dia 2
    dia2 = Label(root, font=('Helvetica', 13, 'bold'), bg="#765827", fg="black")
    dia2.place(x=55, y=355)
    TempoDia2label = Label(root, font=('Helvetica', 10, 'bold'), bg="#765827", fg="black")
    TempoDia2label.place(x=55, y=380)
    TemperaturaMaxDia2label = Label(root, font=('Helvetica', 10, 'bold'), bg="#765827", fg="black")
    TemperaturaMaxDia2label.place(x=55, y=400)
    UmidadeDia2label = Label(root, font=('Helvetica', 10, 'bold'), bg="#765827", fg="black")
    UmidadeDia2label.place(x=55, y=420)

    segundo = dia1+timedelta(days=1)
    TemperaturaMaxDia2Bruta = RequisicaoPrev_dic['list'][0]['main']['temp_max']-273.15
    UmidadeDia2 = RequisicaoPrev_dic['list'][0]['main']['humidity']
    TempoDia2 = RequisicaoPrev_dic['list'][0]['weather'][0]['description']

    TemperaturaMaxDia2 = "{:.2f}".format(TemperaturaMaxDia2Bruta)

    dia2.config(text=segundo.strftime("-%A"))
    TempoDia2label.config(text=(TempoDia2))
    TemperaturaMaxDia2label.config(text=('Temperatura:',TemperaturaMaxDia2, '°C'))
    UmidadeDia2label.config(text=('Umidade:', UmidadeDia2, '%'))


    # ====================== Dia 3
    dia3 = Label(root, font=('Helvetica', 13, 'bold'), bg="#765827", fg="black")
    dia3.place(x=235, y=355)
    TempoDia3label = Label(root, font=('Helvetica', 10, 'bold'), bg="#765827", fg="black")
    TempoDia3label.place(x=235, y=380)
    TemperaturaMaxDia3label = Label(root, font=('Helvetica', 10, 'bold'), bg="#765827", fg="black")
    TemperaturaMaxDia3label.place(x=235, y=400)
    UmidadeDia3label = Label(root, font=('Helvetica', 10, 'bold'), bg="#765827", fg="black")
    UmidadeDia3label.place(x=235, y=420)

    terceiro = dia1+timedelta(days=2)
    TemperaturaMaxDia3Bruta = RequisicaoPrev_dic['list'][8]['main']['temp_max']-273.15
    UmidadeDia3 = RequisicaoPrev_dic['list'][8]['main']['humidity']
    TempoDia3 = RequisicaoPrev_dic['list'][8]['weather'][0]['description']

    TemperaturaMaxDia3 = "{:.2f}".format(TemperaturaMaxDia3Bruta)

    dia3.config(text=terceiro.strftime("-%A"))
    TempoDia3label.config(text=(TempoDia3))
    TemperaturaMaxDia3label.config(text=('Temperatura:',TemperaturaMaxDia3, '°C'))
    UmidadeDia3label.config(text=('Umidade:', UmidadeDia3, '%'))


    # ====================== Dia 4
    dia4 = Label(root, font=('Helvetica', 13, 'bold'), bg="#765827", fg="black")
    dia4.place(x=415, y=355)
    TempoDia4label = Label(root, font=('Helvetica', 10, 'bold'), bg="#765827", fg="black")
    TempoDia4label.place(x=415, y=380)
    TemperaturaMaxDia4label = Label(root, font=('Helvetica', 10, 'bold'), bg="#765827", fg="black")
    TemperaturaMaxDia4label.place(x=415, y=400)
    UmidadeDia4label = Label(root, font=('Helvetica', 10, 'bold'), bg="#765827", fg="black")
    UmidadeDia4label.place(x=415, y=420)

    quarto = dia1+timedelta(days=3)
    TemperaturaMaxDia4Bruta = RequisicaoPrev_dic['list'][16]['main']['temp_max']-273.15
    UmidadeDia4 = RequisicaoPrev_dic['list'][16]['main']['humidity']
    TempoDia4 = RequisicaoPrev_dic['list'][16]['weather'][0]['description']

    TemperaturaMaxDia4 = "{:.2f}".format(TemperaturaMaxDia4Bruta)

    dia4.config(text=quarto.strftime("-%A"))
    TempoDia4label.config(text=(TempoDia4))
    TemperaturaMaxDia4label.config(text=('Temperatura:',TemperaturaMaxDia4, '°C'))
    UmidadeDia4label.config(text=('Umidade:', UmidadeDia4, '%'))


    # ====================== Dia 5
    dia5 = Label(root, font=('Helvetica', 13, 'bold'), bg="#765827", fg="black")
    dia5.place(x=595, y=355)
    TempoDia5label = Label(root, font=('Helvetica', 10, 'bold'), bg="#765827", fg="black")
    TempoDia5label.place(x=595, y=380)
    TemperaturaMaxDia5label = Label(root, font=('Helvetica', 10, 'bold'), bg="#765827", fg="black")
    TemperaturaMaxDia5label.place(x=595, y=400)
    UmidadeDia5label = Label(root, font=('Helvetica', 10, 'bold'), bg="#765827", fg="black")
    UmidadeDia5label.place(x=595, y=420)

    quinto = dia1+timedelta(days=4)
    TemperaturaMaxDia5Bruta = RequisicaoPrev_dic['list'][24]['main']['temp_max']-273.15
    UmidadeDia5 = RequisicaoPrev_dic['list'][24]['main']['humidity']
    TempoDia5 = RequisicaoPrev_dic['list'][24]['weather'][0]['description']

    TemperaturaMaxDia5 = "{:.2f}".format(TemperaturaMaxDia5Bruta)

    dia5.config(text=quinto.strftime("-%A"))
    TempoDia5label.config(text=(TempoDia5))
    TemperaturaMaxDia5label.config(text=('Temperatura:',TemperaturaMaxDia5, '°C'))
    UmidadeDia5label.config(text=('Umidade:', UmidadeDia5, '%'))


    # ====================== Dia 6
    dia6 = Label(root, font=('Helvetica', 13, 'bold'), bg="#765827", fg="black")
    dia6.place(x=775, y=355)
    TempoDia6label = Label(root, font=('Helvetica', 10, 'bold'), bg="#765827", fg="black")
    TempoDia6label.place(x=775, y=380)
    TemperaturaMaxDia6label = Label(root, font=('Helvetica', 10, 'bold'), bg="#765827", fg="black")
    TemperaturaMaxDia6label.place(x=775, y=400)
    UmidadeDia6label = Label(root, font=('Helvetica', 10, 'bold'), bg="#765827", fg="black")
    UmidadeDia6label.place(x=775, y=420)

    sexto = dia1+timedelta(days=5)
    TemperaturaMaxDia6Bruta = RequisicaoPrev_dic['list'][32]['main']['temp_max']-273.15
    UmidadeDia6 = RequisicaoPrev_dic['list'][32]['main']['humidity']
    TempoDia6 = RequisicaoPrev_dic['list'][32]['weather'][0]['description']

    TemperaturaMaxDia6 = "{:.2f}".format(TemperaturaMaxDia6Bruta)

    dia6.config(text=sexto.strftime("-%A"))
    TempoDia6label.config(text=(TempoDia6))
    TemperaturaMaxDia6label.config(text=('Temperatura:',TemperaturaMaxDia6, '°C'))
    UmidadeDia6label.config(text=('Umidade:', UmidadeDia6, '%'))


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
    datalabrelatorio.config(text=(data_formatada + dia_da_semana), fg='black', bg='#765827')

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

   def modal_dica1():
    modal1 = tk.Toplevel(root)
    modal1.title("Dica")
    modal1.geometry("500x220")
    modal1.configure(bg='#EAC696')
    modal1.resizable(False, False)
    
    espaco1 = ttk.Label(modal1, text="", background='#EAC696')
    textodica1pt1 = ttk.Label(modal1, text="Antes de plantar, é necessário arar, gradear e nivelar o", background='#EAC696', foreground='black')
    textodica1pt2 = ttk.Label(modal1, text="solo para criar uma superfície uniforme para as sementes.", background='#EAC696', foreground='black') 
    textodica1pt3 = ttk.Label(modal1, text="A profundidade da aração deve ser de 20 a 30 cm, resultando", background='#EAC696', foreground='black') 
    textodica1pt4 = ttk.Label(modal1, text="em um solo bem solto e bem ventilado.", background='#EAC696', foreground='black') 
    textodica1pt5 = ttk.Label(modal1, text="A temperatura ideal do solo para o plantio varia de 21°C a 29°C.", background='#EAC696', foreground='black') 
    textodica1pt6 = ttk.Label(modal1, text="Certifique-se de que o solo esteja aquecido o suficiente para", background='#EAC696', foreground='black') 
    textodica1pt7 = ttk.Label(modal1, text="estimular a germinação das sementes.", background='#EAC696', foreground='black') 
    
    espaco1.pack()
    textodica1pt1.pack()
    textodica1pt2.pack()
    textodica1pt3.pack()
    textodica1pt4.pack()
    textodica1pt5.pack()
    textodica1pt6.pack()
    textodica1pt7.pack()

    botaofechar1 = ttk.Button(modal1, text="Fechar", command=modal1.destroy)
    botaofechar1.pack(pady=20)

   def modal_dica2():
    modal2 = tk.Toplevel(root)
    modal2.title("Dica")
    modal2.geometry("500x190")
    modal2.configure(bg='#EAC696')
    modal2.resizable(False, False)
    
    espaco2 = ttk.Label(modal2, text="", background='#EAC696')
    textodica2pt1 = ttk.Label(modal2, text="É crucial escolher sementes de alta qualidade,", background='#EAC696', foreground='black')
    textodica2pt2 = ttk.Label(modal2, text="garantindo que estejam saudáveis.", background='#EAC696', foreground='black') 
    textodica2pt3 = ttk.Label(modal2, text="Além disso, as sementes devem ser tratadas", background='#EAC696', foreground='black') 
    textodica2pt4 = ttk.Label(modal2, text="com fungicida antes do plantio para protegê-las", background='#EAC696', foreground='black') 
    textodica2pt5 = ttk.Label(modal2, text="contra doenças.", background='#EAC696', foreground='black') 
    textodica2pt6 = ttk.Label(modal2, text="", background='#EAC696') 
    
    espaco2.pack()
    textodica2pt1.pack()
    textodica2pt2.pack()
    textodica2pt3.pack()
    textodica2pt4.pack()
    textodica2pt5.pack()
    textodica2pt6.pack()
    
    botaofechar2 = ttk.Button(modal2, text="Fechar", command=modal2.destroy)
    botaofechar2.pack()

   def modal_dica3():
    modal3 = tk.Toplevel(root)
    modal3.title("Dica")
    modal3.geometry("500x210")
    modal3.configure(bg='#EAC696')
    modal3.resizable(False, False)
    
    espaco3 = ttk.Label(modal3, text="", background='#EAC696')
    textodica3pt1 = ttk.Label(modal3, text="O espaçamento médio entre linhas recomendado é de 60 cm", background='#EAC696', foreground='black')
    textodica3pt2 = ttk.Label(modal3, text="e a densidade de semeadura é de 18 a 20 sementes por", background='#EAC696', foreground='black') 
    textodica3pt3 = ttk.Label(modal3, text="metro de linha.", background='#EAC696', foreground='black') 
    textodica3pt4 = ttk.Label(modal3, text="Nas lavouras mecanizadas, é comum o plantio de três", background='#EAC696', foreground='black') 
    textodica3pt5 = ttk.Label(modal3, text="linhas espaçadas de 50 a 55 cm, deixando-se um intervalo", background='#EAC696', foreground='black') 
    textodica3pt6 = ttk.Label(modal3, text="de 70 cm, para a entrelinha de trânsito do trator.", background='#EAC696', foreground='black') 
    textodica3pt7 = ttk.Label(modal3, text="", background='#EAC696') 
    
    espaco3.pack()
    textodica3pt1.pack()
    textodica3pt2.pack()
    textodica3pt3.pack()
    textodica3pt4.pack()
    textodica3pt5.pack()
    textodica3pt6.pack()
    textodica3pt7.pack()
    
    botaofechar3 = ttk.Button(modal3, text="Fechar", command=modal3.destroy)
    botaofechar3.pack()

   def modal_dica4():
    modal4 = tk.Toplevel(root)
    modal4.title("Dica")
    modal4.geometry("500x240")
    modal4.configure(bg='#EAC696')
    modal4.resizable(False, False)
    
    espaco4 = ttk.Label(modal4, text="", background='#EAC696')
    textodica4pt1 = ttk.Label(modal4, text="O espaçamento médio entre linhas deve ser de 80 a 90 cm, deixando-se cair", background='#EAC696', foreground='black')
    textodica4pt2 = ttk.Label(modal4, text="14 a 15 sementes por metro. Ou seja, esses cultivares garantem sua máxima", background='#EAC696', foreground='black') 
    textodica4pt3 = ttk.Label(modal4, text="produtividade com menos plantas por área do que os amendoins de porte ereto.", background='#EAC696', foreground='black') 
    textodica4pt4 = ttk.Label(modal4, text="O esquema de plantio mais usual para cultivares rasteiros, no Sudeste brasileiro, é de", background='#EAC696', foreground='black') 
    textodica4pt5 = ttk.Label(modal4, text="“linhas simples” com 90 cm de entrelinhas. Este espaçamento é o que melhor se adapta ao", background='#EAC696', foreground='black') 
    textodica4pt6 = ttk.Label(modal4, text="arranquio mecanizado, produzindo um bom enleiramento das plantas.", background='#EAC696', foreground='black') 
    textodica4pt7 = ttk.Label(modal4, text="Plantas de amendoim rasteiro podem apresentar variações no crescimento da parte aérea,", background='#EAC696', foreground='black') 
    textodica4pt8 = ttk.Label(modal4, text="principalmente em função de fatores climáticos.", background='#EAC696', foreground='black') 

    espaco4.pack()
    textodica4pt1.pack()
    textodica4pt2.pack()
    textodica4pt3.pack()
    textodica4pt4.pack()
    textodica4pt5.pack()
    textodica4pt6.pack()
    textodica4pt7.pack()
    textodica4pt8.pack()
    
    botaofechar4 = ttk.Button(modal4, text="Fechar", command=modal4.destroy)
    botaofechar4.pack(pady=20)

#====================================================

   def modal_dica5():
    modal5 = tk.Toplevel(root)
    modal5.title("Dica")
    modal5.geometry("500x130")
    modal5.configure(bg='#EAC696')
    modal5.resizable(False, False)
    
    espaco5 = ttk.Label(modal5, text="", background='#EAC696')
    textodica5pt1 = ttk.Label(modal5, text="As sementes de amendoim devem ser inseridas no solo a ", background='#EAC696', foreground='black')
    textodica5pt2 = ttk.Label(modal5, text="uma profundidade de 3 a 5 cm, com a extremidade", background='#EAC696', foreground='black') 
    textodica5pt3 = ttk.Label(modal5, text="voltada para baixo e o broto apontando para cima.", background='#EAC696', foreground='black') 
    textodica5pt4 = ttk.Label(modal5, text="", background='#EAC696') 

    espaco5.pack()
    textodica5pt1.pack()
    textodica5pt2.pack()
    textodica5pt3.pack()
    textodica5pt4.pack()
    
    botaofechar5 = ttk.Button(modal5, text="Fechar", command=modal5.destroy)
    botaofechar5.pack()

   def modal_dica6():
    modal6 = tk.Toplevel(root)
    modal6.title("Dica")
    modal6.geometry("500x150")
    modal6.configure(bg='#EAC696')
    modal6.resizable(False, False)
    
    espaco6 = ttk.Label(modal6, text="", background='#EAC696')
    textodica6pt1 = ttk.Label(modal6, text="Após o plantio, é fundamental garantir que as sementes sejam regadas", background='#EAC696', foreground='black')
    textodica6pt2 = ttk.Label(modal6, text="adequadamente para manter o solo úmido, evitando, no entanto, o encharcamento.", background='#EAC696', foreground='black') 
    textodica6pt3 = ttk.Label(modal6, text="A irrigação deve ser realizada regularmente durante todo o período ", background='#EAC696', foreground='black') 
    textodica6pt4 = ttk.Label(modal6, text="de crescimento da planta.", background='#EAC696', foreground='black') 
    textodica6pt5 = ttk.Label(modal6, text="", background='#EAC696') 
    
    espaco6.pack()
    textodica6pt1.pack()
    textodica6pt2.pack()
    textodica6pt3.pack()
    textodica6pt4.pack()
    textodica6pt5.pack()
    
    botaofechar6 = ttk.Button(modal6, text="Fechar", command=modal6.destroy)
    botaofechar6.pack()

   def modal_dica7():
    modal7 = tk.Toplevel(root)
    modal7.title("Dica")
    modal7.geometry("500x200")
    modal7.configure(bg='#EAC696')
    modal7.resizable(False, False)
    
    espaco7 = ttk.Label(modal7, text="", background='#EAC696')
    textodica7pt1 = ttk.Label(modal7, text="A adubagem no plantio de amendoim é um aspecto essencial para", background='#EAC696', foreground='black')
    textodica7pt2 = ttk.Label(modal7, text="promover o crescimento saudável e a produtividade da cultura.", background='#EAC696', foreground='black') 
    textodica7pt3 = ttk.Label(modal7, text="É importante ressaltar que as recomendações de adubação podem variar dependendo", background='#EAC696', foreground='black') 
    textodica7pt4 = ttk.Label(modal7, text="da região, das condições locais e das características da variedade de amendoim.", background='#EAC696', foreground='black') 
    textodica7pt5 = ttk.Label(modal7, text="Portanto, é aconselhável consultar um agrônomo ou técnico agrícola para orientações", background='#EAC696', foreground='black') 
    textodica7pt6 = ttk.Label(modal7, text="específicas e personalizadas para a sua plantação de amendoim.", background='#EAC696', foreground='black') 
    textodica7pt7 = ttk.Label(modal7, text="", background='#EAC696') 
    
    espaco7.pack()
    textodica7pt1.pack()
    textodica7pt2.pack()
    textodica7pt3.pack()
    textodica7pt4.pack()
    textodica7pt5.pack()
    textodica7pt6.pack()
    textodica7pt7.pack()
    
    botaofechar7 = ttk.Button(modal7, text="Fechar", command=modal7.destroy)
    botaofechar7.pack()

   def modal_dica8():
    modal8 = tk.Toplevel(root)
    modal8.title("Dica")
    modal8.geometry("550x240")
    modal8.configure(bg='#EAC696')
    modal8.resizable(False, False)
    
    espaco8 = ttk.Label(modal8, text="", background='#EAC696')
    textodica8pt1 = ttk.Label(modal8, text="Durante o ciclo de crescimento do amendoim, é essencial manter o controle das plantas daninhas", background='#EAC696', foreground='black')
    textodica8pt2 = ttk.Label(modal8, text="para evitar a competição por nutrientes e água.", background='#EAC696', foreground='black') 
    textodica8pt3 = ttk.Label(modal8, text="Para o manejo eficaz das pragas na plantação de amendoim, é importante adotar práticas de", background='#EAC696', foreground='black') 
    textodica8pt4 = ttk.Label(modal8, text="controle integrado, incluindo o monitoramento regular, o uso de variedades resistentes quando", background='#EAC696', foreground='black') 
    textodica8pt5 = ttk.Label(modal8, text="disponíveis, o uso criterioso de inseticidas quando necessário, a rotação de culturas e a ", background='#EAC696', foreground='black') 
    textodica8pt6 = ttk.Label(modal8, text="manutenção de boas práticas de manejo agrícola.", background='#EAC696', foreground='black') 
    textodica8pt7 = ttk.Label(modal8, text="O controle biológico também pode ser uma opção sustentável para combater pragas em culturas de", background='#EAC696', foreground='black') 
    textodica8pt8 = ttk.Label(modal8, text="amendoim.", background='#EAC696', foreground='black') 

    
    espaco8.pack()
    textodica8pt1.pack()
    textodica8pt2.pack()
    textodica8pt3.pack()
    textodica8pt4.pack()
    textodica8pt5.pack()
    textodica8pt6.pack()
    textodica8pt7.pack()
    textodica8pt8.pack()

    
    botaofechar8 = ttk.Button(modal8, text="Fechar", command=modal8.destroy)
    botaofechar8.pack(pady=20)

#====================================================

   def modal_dica9():
    modal9 = tk.Toplevel(root)
    modal9.title("Dica")
    modal9.geometry("580x260")
    modal9.configure(bg='#EAC696')
    modal9.resizable(False, False)
    
    espaco9 = ttk.Label(modal9, text="", background='#EAC696')
    espaco9_2 = ttk.Label(modal9, text="", background='#EAC696')
    espaco9_3 = ttk.Label(modal9, text="", background='#EAC696')

    textodica9pt1 = ttk.Label(modal9, text="A colheita do amendoim é realizada quando os frutos atingem a maturidade. Isso é indicado pelo", background='#EAC696', foreground='black')
    textodica9pt2 = ttk.Label(modal9, text="amarelecimento das folhas e cascas, e pelas vagens que começam a secar. O momento ideal para a", background='#EAC696', foreground='black') 
    textodica9pt3 = ttk.Label(modal9, text="colheita é quando cerca de 80% das vagens estão maduras.", background='#EAC696', foreground='black') 
    textodica9pt4 = ttk.Label(modal9, text="Colheita manual: Em algumas regiões, a colheita do amendoim é realizada manualmente.", background='#EAC696', foreground='black') 
    textodica9pt5 = ttk.Label(modal9, text="Os trabalhadores arrancam as plantas do solo e batem as vagens para soltá-las.", background='#EAC696', foreground='black') 
    textodica9pt6 = ttk.Label(modal9, text="Colheita mecanizada: Em áreas maiores, a colheita mecanizada é comum. Máquinas escavadoras puxam", background='#EAC696', foreground='black') 
    textodica9pt7 = ttk.Label(modal9, text="as plantas do solo e as depositam em fileiras. Em seguida, máquinas colheitadeiras retiram as vagens.", background='#EAC696', foreground='black') 
    
    espaco9.pack()
    textodica9pt1.pack()
    textodica9pt2.pack()
    textodica9pt3.pack()
    espaco9_2.pack()
    textodica9pt4.pack()
    textodica9pt5.pack()
    espaco9_3.pack()
    textodica9pt6.pack()
    textodica9pt7.pack()
    
    botaofechar9 = ttk.Button(modal9, text="Fechar", command=modal9.destroy)
    botaofechar9.pack(pady=20)

   def modal_dica10():
    modal10 = tk.Toplevel(root)
    modal10.title("Dica")
    modal10.geometry("550x400")
    modal10.configure(bg='#EAC696')
    modal10.resizable(False, False)
    
    espaco10 = ttk.Label(modal10, text="", background='#EAC696')
    espaco10_2 = ttk.Label(modal10, text="", background='#EAC696')
    espaco10_3 = ttk.Label(modal10, text="", background='#EAC696')
    espaco10_4 = ttk.Label(modal10, text="", background='#EAC696')
    espaco10_5 = ttk.Label(modal10, text="", background='#EAC696')

    textodica10pt1 = ttk.Label(modal10, text="Secagem: Após a colheita, as vagens de amendoim são deixadas ao sol para secar.", background='#EAC696', foreground='black')
    textodica10pt2 = ttk.Label(modal10, text="Isso ajuda a reduzir o teor de umidade dos grãos, o que é importante para evitar ", background='#EAC696', foreground='black') 
    textodica10pt3 = ttk.Label(modal10, text="o desenvolvimento de fungos e para a conservação dos produtos.", background='#EAC696', foreground='black') 
    textodica10pt4 = ttk.Label(modal10, text="Armazenamento: Após a secagem, os grãos de amendoim são armazenados em locais", background='#EAC696', foreground='black') 
    textodica10pt5 = ttk.Label(modal10, text="adequados, como celeiros ou armazéns, para evitar infestações por pragas e", background='#EAC696', foreground='black') 
    textodica10pt6 = ttk.Label(modal10, text="garantir a manutenção da qualidade.", background='#EAC696', foreground='black') 
    textodica10pt7 = ttk.Label(modal10, text="Limpeza: Antes de serem comercializados ou processados, os grãos de amendoim passam", background='#EAC696', foreground='black') 
    textodica10pt8 = ttk.Label(modal10, text="por uma etapa de limpeza para remover detritos, sujeira e quaisquer impurezas.", background='#EAC696', foreground='black') 
    textodica10pt9 = ttk.Label(modal10, text="Beneficiamento: Nessa etapa, os grãos de amendoim são separados das vagens e", background='#EAC696', foreground='black')     
    textodica10pt10 = ttk.Label(modal10, text="preparados para comercialização ou processamento adicional.", background='#EAC696', foreground='black') 
    textodica10pt11 = ttk.Label(modal10, text="Embalagem: Os grãos de amendoim beneficiados são embalados em sacos adequados para", background='#EAC696', foreground='black') 
    textodica10pt12 = ttk.Label(modal10, text="o armazenamento ou para venda ao consumidor.", background='#EAC696', foreground='black') 

    espaco10.pack()
    textodica10pt1.pack()
    textodica10pt2.pack()
    textodica10pt3.pack()
    espaco10_2.pack()
    textodica10pt4.pack()
    textodica10pt5.pack()
    textodica10pt6.pack()
    espaco10_3.pack()
    textodica10pt7.pack()
    textodica10pt8.pack()
    espaco10_4.pack()
    textodica10pt9.pack()
    textodica10pt10.pack()
    espaco10_5.pack()
    textodica10pt11.pack()
    textodica10pt12.pack()
    
    botaofechar10 = ttk.Button(modal10, text="Fechar", command=modal10.destroy)
    botaofechar10.pack(pady=20)

   def modal_dica11():
    modal11 = tk.Toplevel(root)
    modal11.title("Dica")
    modal11.geometry("550x410")
    modal11.configure(bg='#EAC696')
    modal11.resizable(False, False)
    
    espaco11 = ttk.Label(modal11, text="", background='#EAC696')
    espaco11_2 = ttk.Label(modal11, text="", background='#EAC696')
    espaco11_3 = ttk.Label(modal11, text="", background='#EAC696')
    espaco11_4 = ttk.Label(modal11, text="", background='#EAC696')
    espaco11_5 = ttk.Label(modal11, text="", background='#EAC696')
    espaco11_6 = ttk.Label(modal11, text="", background='#EAC696')

    textodica11pt1 = ttk.Label(modal11, text="Existem vários tipos de amendoim, diferindo em tamanho, forma, cor e sabor.", background='#EAC696', foreground='black')
    textodica11pt2 = ttk.Label(modal11, text="Alguns dos principais tipos incluem:", background='#EAC696', foreground='black') 
    textodica11pt3 = ttk.Label(modal11, text="Amendoim Comum ou Espanhol: É o tipo mais comum, com casca fina e vermelha,", background='#EAC696', foreground='black') 
    textodica11pt4 = ttk.Label(modal11, text="usado na produção de pasta de amendoim, óleo e snacks.", background='#EAC696', foreground='black') 
    textodica11pt5 = ttk.Label(modal11, text="Amendoim Tatuí: Possui sabor mais acentuado e um teor de óleo mais elevado,", background='#EAC696', foreground='black') 
    textodica11pt6 = ttk.Label(modal11, text="sendo usado na produção de óleo e na culinária.", background='#EAC696', foreground='black') 
    textodica11pt7 = ttk.Label(modal11, text="Amendoim Runner: Tem uma forma mais alongada e casca mais grossa, sendo", background='#EAC696', foreground='black') 
    textodica11pt8 = ttk.Label(modal11, text="amplamente utilizado na produção de snacks, pasta de amendoim e óleo.", background='#EAC696', foreground='black')   
    textodica11pt9 = ttk.Label(modal11, text="Amendoim Valência: Possui formato mais redondo e sabor suave, sendo", background='#EAC696', foreground='black') 
    textodica11pt10 = ttk.Label(modal11, text="usado na produção de amendoim caramelizado e torrado.", background='#EAC696', foreground='black')   
    textodica11pt11 = ttk.Label(modal11, text="Amendoim Doce Japonês: É popular na culinária japonesa, com um", background='#EAC696', foreground='black') 
    textodica11pt12 = ttk.Label(modal11, text="revestimento de açúcar e sabor adocicado.", background='#EAC696', foreground='black')  

    espaco11.pack()
    textodica11pt1.pack()
    textodica11pt2.pack()
    espaco11_2.pack()
    textodica11pt3.pack()
    textodica11pt4.pack()
    espaco11_3.pack()
    textodica11pt5.pack()
    textodica11pt6.pack()
    espaco11_4.pack()
    textodica11pt7.pack()
    textodica11pt8.pack()
    espaco11_5.pack()
    textodica11pt9.pack()
    textodica11pt10.pack()
    espaco11_6.pack()
    textodica11pt11.pack()
    textodica11pt12.pack()



    botaofechar11 = ttk.Button(modal11, text="Fechar", command=modal11.destroy)
    botaofechar11.pack(pady=20)


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
   botaodica1 = tk.Button(dicasjanela, text="Ver dica", command=modal_dica1)
   botaodica1.place(x=127, y=210)

   dica2quadro = tk.Canvas(dicasjanela, width=200, height=100)
   dica2quadro.place(x=280, y=150)
   dica2quadro.create_rectangle (0.5, 0.5, 210, 110, fill="#765827")
   labeldica2=Label(dicasjanela, text='Seleção de sementes', font=('Helvetica', 12, 'bold'), fg='Black', bg='#765827')
   labeldica2.place(x=300, y=165)
   botaodica2 = tk.Button(dicasjanela, text="Ver dica", command=modal_dica2)
   botaodica2.place(x=357, y=210)

   dica3quadro = tk.Canvas(dicasjanela, width=200, height=100)
   dica3quadro.place(x=510, y=150)
   dica3quadro.create_rectangle (0.5, 0.5, 210, 110, fill="#765827")
   labeldica3=Label(dicasjanela, text='Cultivares porte ereto', font=('Helvetica', 12, 'bold'), fg='Black', bg='#765827')
   labeldica3.place(x=525, y=165)
   botaodica3 = tk.Button(dicasjanela, text="Ver dica", command=modal_dica3)
   botaodica3.place(x=587, y=210)

   dica4quadro = tk.Canvas(dicasjanela, width=200, height=100)
   dica4quadro.place(x=740, y=150)
   dica4quadro.create_rectangle (0.5, 0.5, 210, 110, fill="#765827")
   labeldica4=Label(dicasjanela, text='Cultivares porte rasteiro', font=('Helvetica', 12, 'bold'), fg='Black', bg='#765827')
   labeldica4.place(x=747, y=165)
   botaodica4 = tk.Button(dicasjanela, text="Ver dica", command=modal_dica4)
   botaodica4.place(x=817, y=210)

# ============Fileira 2

   dica5quadro = tk.Canvas(dicasjanela, width=200, height=100)
   dica5quadro.place(x=50, y=270)
   dica5quadro.create_rectangle (0.5, 0.5, 210, 110, fill="#765827")
   labeldica5=Label(dicasjanela, text='Plantio', font=('Helvetica', 12, 'bold'), fg='Black', bg='#765827')
   labeldica5.place(x=124, y=285)
   botaodica5 = tk.Button(dicasjanela, text="Ver dica", command=modal_dica5)
   botaodica5.place(x=127, y=330)

   dica6quadro = tk.Canvas(dicasjanela, width=200, height=100)
   dica6quadro.place(x=280, y=270)
   dica6quadro.create_rectangle (0.5, 0.5, 210, 110, fill="#765827")
   labeldica6=Label(dicasjanela, text='Irrigação', font=('Helvetica', 12, 'bold'), fg='Black', bg='#765827')
   labeldica6.place(x=344, y=285)
   botaodica6 = tk.Button(dicasjanela, text="Ver dica", command=modal_dica6)
   botaodica6.place(x=357, y=330)
   
   dica7quadro = tk.Canvas(dicasjanela, width=200, height=100)
   dica7quadro.place(x=510, y=270)
   dica7quadro.create_rectangle (0.5, 0.5, 210, 110, fill="#765827")
   labeldica7=Label(dicasjanela, text='Adubagem', font=('Helvetica', 12, 'bold'), fg='Black', bg='#765827')
   labeldica7.place(x=565, y=285)
   botaodica7 = tk.Button(dicasjanela, text="Ver dica", command=modal_dica7)
   botaodica7.place(x=587, y=330)

   dica8quadro = tk.Canvas(dicasjanela, width=200, height=100)
   dica8quadro.place(x=740, y=270)
   dica8quadro.create_rectangle (0.5, 0.5, 210, 110, fill="#765827")
   labeldica8=Label(dicasjanela, text='Controle de pragas', font=('Helvetica', 12, 'bold'), fg='Black', bg='#765827')
   labeldica8.place(x=765, y=285)
   botaodica8 = tk.Button(dicasjanela, text="Ver dica", command=modal_dica8)
   botaodica8.place(x=817, y=330)

# ============Fileira 3

   dica9quadro = tk.Canvas(dicasjanela, width=200, height=100)
   dica9quadro.place(x=50, y=390)
   dica9quadro.create_rectangle (0.5, 0.5, 210, 110, fill="#765827")
   labeldica9=Label(dicasjanela, text='Colheita', font=('Helvetica', 12, 'bold'), fg='Black', bg='#765827')
   labeldica9.place(x=120, y=405)
   botaodica9 = tk.Button(dicasjanela, text="Ver dica", command=modal_dica9)
   botaodica9.place(x=127, y=450)

   dica10quadro = tk.Canvas(dicasjanela, width=200, height=100)
   dica10quadro.place(x=280, y=390)
   dica10quadro.create_rectangle (0.5, 0.5, 210, 110, fill="#765827")
   labeldica10=Label(dicasjanela, text='Pós-colheita', font=('Helvetica', 12, 'bold'), fg='Black', bg='#765827')
   labeldica10.place(x=335, y=405)
   botaodica10 = tk.Button(dicasjanela, text="Ver dica", command=modal_dica10)
   botaodica10.place(x=357, y=450)
   
   dica11quadro = tk.Canvas(dicasjanela, width=200, height=100)
   dica11quadro.place(x=510, y=390)
   dica11quadro.create_rectangle (0.5, 0.5, 210, 110, fill="#765827")
   labeldica11=Label(dicasjanela, text='Variedades de amendoim', font=('Helvetica', 12, 'bold'), fg='Black', bg='#765827')
   labeldica11.place(x=513, y=405)
   botaodica11 = tk.Button(dicasjanela, text="Ver dica", command=modal_dica11)
   botaodica11.place(x=587, y=450)


# Iniciando tela
   root.mainloop()
   
except Exception as e:
  messagebox.showerror('Erro', f'Ocorreu um erro ao iniciar o projeto: {e}')
