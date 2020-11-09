import requests

import PySimpleGUI as sg

req = requests.session()

sg.theme("Reddit")
# Layout
layout = [
        [sg.Text("Seu CEP: "), sg.InputText(key="sCEP")],
        [sg.Text("CEP:"), sg.Text(key="rCEP", size=(9, 1))],
        [sg.Text("Logradouro:"), sg.Text(key="rLog", size=(39, 1))],
        [sg.Text("Complemento:"), sg.Text(key="rComple", size=(25, 1))],
        [sg.Text("Bairro:"), sg.Text(key="rBair", size=(20, 1))],
        [sg.Text("Localidade:"), sg.Text(key="rLoca", size=(20, 1))],
        [sg.Text("Estado:"), sg.Text(key="rUf", size=(3, 1))],
        [sg.Button("Buscar"), sg.Text(key="success", size=(25, 1))],
]
# Janela
janela = sg.Window("Buscador de CEP", layout, font="arial")
# Ler os eventos
while True:
    eventos, valores = janela.read()

    if(eventos == sg.WINDOW_CLOSED):
        break
    if(eventos == "Buscar"):
            if(len(valores["sCEP"]) < 8):
                 janela["success"].update("Erro! o cep tem que ter 8 digitos")
            elif(len(valores["sCEP"]) > 8):
                janela["success"].update("Erro! o cep tem que ter 8 digitos")
            else:
                url = "https://viacep.com.br/ws/{}/json/".format(valores["sCEP"])
                source = req.get(url)
                result = source.json()
                janela["rCEP"].update(result["cep"])
                janela["rLog"].update(result["logradouro"])
                janela["rComple"].update(result["complemento"])
                janela["rBair"].update(result["bairro"])
                janela["rLoca"].update(result["localidade"])
                janela["rUf"].update(result["uf"])

                janela["success"].update("CEP buscado com sucesso")

