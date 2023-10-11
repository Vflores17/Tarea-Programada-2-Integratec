import tkinter as tk
import requests
from bs4 import BeautifulSoup

urlSedes="https://www.tec.ac.cr/carreras"

def obtenerSedesCarreras():
    carrerasSede = {}
    inicialesSedes={"Campus Tecnológico Local San Carlos": "CTLSC","Campus Tecnológico Local San José": "CTLSJ","Centro Académico de Limón": "CAL","Campus Tecnológico Central Cartago": "CTCC","Centro Académico de Alajuela": "CAA"}
    resp = requests.get(urlSedes)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, "html.parser")
        carrerasPorSede = soup.find_all("div", class_="view-content")[0]
        for sede in carrerasPorSede.find_all("div", class_="group"):
            nombreSede=sede.find("a").text
            lugar=inicialesSedes.get(nombreSede)
            carrerasSede[lugar]=[]
            for carrera in sede.find_all("div", class_="title"):
               nombre_carrera = carrera.find("a").text
               carrerasSede[lugar].append(nombre_carrera)
    return carrerasSede

#info={"ctaa":[["Ingeniería en Computadores",0],["Ingeniería en Computación",5100],["Ingeniería en Computación con Énfasis en Sistemas de Información Empresarial,",0]],}
#print(info["ctaa"][1][1])