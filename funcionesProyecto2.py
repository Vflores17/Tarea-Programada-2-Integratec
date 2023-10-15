import tkinter as tk
import requests
from bs4 import BeautifulSoup
import random
from faker import Faker

urlSedes="https://www.tec.ac.cr/carreras"
#totalAdmitidos={"CTLSC":175,"CTLSJ":75,"CAL":75,"CTCC":625,"CAA":50}
#estructuraCarrerasCantidad={'CTLSC': [['Bachillerato en Administración de Empresas', 2], ['Bachillerato en Gestión del Turismo Rural Sostenible', 1], ['Bachillerato en Gestión en Sostenibilidad Turística', 1], ['Bachillerato en Ingeniería en Computación',2 ], ['Licenciatura en Ingeniería Electrónica', 1], ['Licenciatura en Ingeniería en Agronomía', 2], ['Licenciatura en Ingeniería en Producción Industrial', 1]], 'CTLSJ': [['Bachillerato en Administración de Empresas', 4], ['Bachillerato en Ingeniería en Computación', 3], ['Licenciatura en Arquitectura', 3]], 'CAL': [['Bachillerato en Administración de Empresas', 3], ['Bachillerato en Ingeniería en Computación', 4], ['Bachillerato en Producción Industrial,  Limón', 3]], 'CTCC': [['Bachillerato en Administración de Empresas', 1], ['Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 1], ['Bachillerato en Gestión del Turismo Sostenible', 1], ['Bachillerato en Ingeniería en Biotecnología', 1], ['Bachillerato en Ingeniería en Computación', 1], ['Licenciatura en Administración de Tecnología de Información', 1], ['Licenciatura en Ingeniería Agrícola', 2], ['Licenciatura en Ingeniería Ambiental', 1], ['Licenciatura en Ingeniería Electrónica', 1], ['Licenciatura en Ingeniería en Agronegocios', 2], ['Licenciatura en Ingeniería en Computadores', 2], ['Licenciatura en Ingeniería en Construcción', 2], ['Licenciatura en Ingeniería en Diseño Industrial', 2], ['Licenciatura en Ingeniería en Materiales', 2], ['Licenciatura en Ingeniería en Producción Industrial', 2], ['Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 2], ['Licenciatura en Ingeniería Física', 2], ['Licenciatura en Ingeniería Forestal', 2], ['Licenciatura en Ingeniería Mecatrónica', 2], ['Licenciatura en Mantenimiento Industrial', 4]], 'CAA': [['Bachillerato en Ingeniería en Computación', 5], ['Licenciatura en Ingeniería Electrónica', 5]]}
estructura={'CTLSC': [['Bachillerato en Administración de Empresas', 25], ['Bachillerato en Gestión del Turismo Rural Sostenible', 25], ['Bachillerato en Gestión en Sostenibilidad Turística', 25], ['Bachillerato en Ingeniería en Computación', 25], ['Licenciatura en Ingeniería Electrónica', 25], ['Licenciatura en Ingeniería en Agronomía', 25], ['Licenciatura en Ingeniería en Producción Industrial', 25]], 'CTLSJ': [['Bachillerato en Administración de Empresas', 25], ['Bachillerato en Ingeniería en Computación', 25], ['Licenciatura en Arquitectura', 25]], 'CAL': [['Bachillerato en Administración de Empresas', 25], ['Bachillerato en Ingeniería en Computación', 25], ['Bachillerato en Producción Industrial,  Limón', 25]], 'CTCC': [['Bachillerato en Administración de Empresas', 25], ['Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 25], ['Bachillerato en Gestión del Turismo Sostenible', 25], ['Bachillerato en Ingeniería en Biotecnología', 25], ['Bachillerato en Ingeniería en Computación', 25], ['Licenciatura en Administración de Tecnología de Información', 25], ['Licenciatura en Ingeniería Agrícola', 25], ['Licenciatura en Ingeniería Ambiental', 25], ['Licenciatura en Ingeniería Electrónica', 25], ['Licenciatura en Ingeniería en Agronegocios', 25], ['Licenciatura en Ingeniería en Computadores', 25], ['Licenciatura en Ingeniería en Construcción', 25], ['Licenciatura en Ingeniería en Diseño Industrial', 25], ['Licenciatura en Ingeniería en Materiales', 25], ['Licenciatura en Ingeniería en Producción Industrial', 25], ['Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 25], ['Licenciatura en Ingeniería Física', 25], ['Licenciatura en Ingeniería Forestal', 25], ['Licenciatura en Ingeniería Mecatrónica', 25], ['Licenciatura en Mantenimiento Industrial', 25]], 'CAA': [['Bachillerato en Ingeniería en Computación', 25], ['Licenciatura en Ingeniería Electrónica', 25]]}
codigosSedes = {"CTLSC": "02", "CTLSJ": "03", "CAL": "05", "CTCC": "01", "CAA": "04"}


def generarCarnetsMentores(estructuraCarrerasCantidad,codigosSedes,totalCarnets,totalNumeros,totalCorreos,diccMentores):
    for sede in estructuraCarrerasCantidad.keys():
        listaMentores=[]
        for i,carrera in enumerate(estructuraCarrerasCantidad[sede]):
                cantidadMentores = round(estructuraCarrerasCantidad[sede][i][1]*0.05)
                

                for j in range(cantidadMentores):
                    nuevoCarnet = None

                    while nuevoCarnet is None or nuevoCarnet in totalCarnets:
                        nuevoCarnet = generarNumCarnet(2,codigosSedes[sede])

                    totalCarnets.append(nuevoCarnet)

                    nombreCompleto , telefono , correo = generarDatos(1,"","")

                    while correo in totalCorreos:
                        correo = generarDatos(3,nombreCompleto[0][1:],nombreCompleto[1])
                    totalCorreos.append(correo)

                    listaMentores.append([nuevoCarnet,nombreCompleto, carrera[0], correo])
                    
        diccMentores[sede] = listaMentores
                    
    return diccMentores


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

def generarNumCarnet(gen,sede):
    numRandom = random.randint(1000, 9999)
    if gen == 1:
        nuevoCarnet = "2024" + sede + str(numRandom)
    else:
        nuevoCarnet = "2023" + sede + str(numRandom)
    return nuevoCarnet

def generarDatos(opcion,pnombre,papellido1):
    if opcion == 1:
        fake=Faker()
        nombre = fake.first_name()
        apellido1 = fake.last_name()
        apellido2 = fake.last_name()
        nombreCompleto = (nombre, apellido1, apellido2)
        telefono = random.randint(60000000, 99999999)
        correo = nombre[:2]+apellido1+"@estudiantec.cr"
        return nombreCompleto,telefono,correo
    elif opcion == 2:
        return random.randint(60000000, 99999999)
    elif opcion == 3:
        num=random.randint(1,9)
        return pnombre[:3]+papellido1+str(num)+"@estudiantec.cr"
        
    



def generarCarnetsEstudiantes(totalAdmitidos, estructuraCarrerasCantidad,codigosSedes,totalCarnets,totalNumeros,totalCorreos,diccEstudiantes):
    
    for sede in totalAdmitidos.keys():
        print("generando carnets de estudiantes")
        for i,carrera in enumerate(estructuraCarrerasCantidad[sede]):
            
            cantidad_admitidos = estructuraCarrerasCantidad[sede][i][1]

            for _ in range(cantidad_admitidos):
                nuevoCarnet = None
                
                while nuevoCarnet is None or nuevoCarnet in totalCarnets:
                    nuevoCarnet = generarNumCarnet(1,codigosSedes[sede])

                totalCarnets.append(nuevoCarnet)

                nombreCompleto , telefono , correo = generarDatos(1,"","")
                
                while telefono in totalNumeros:
                    telefono = generarDatos(2,"","")
                totalNumeros.append(telefono)

                while correo in totalCorreos:
                    correo = generarDatos(3,nombreCompleto[0],nombreCompleto[1])
                totalCorreos.append(correo)


                diccEstudiantes[nuevoCarnet] = [nombreCompleto, telefono, correo, sede, carrera[0],0]

    return diccEstudiantes

def imprimir_diccionario(diccionario):
    for clave, valor in diccionario.items():
        print(clave, ":", valor)

#info={"ctaa":[["Ingeniería en Computadores",0],["Ingeniería en Computación",5100],["Ingeniería en Computación con Énfasis en Sistemas de Información Empresarial,",0]],}
#print(info["ctaa"][1][1])
#estructura=generarCarnetsEstudiantes(totalAdmitidos, estructura,codigosSedes,[],[],[],{})
#imprimir_diccionario(estructura)
#print(generarCarnetsMentores(estructura,codigosSedes,[],[],[],{}))
#estructura=generarCarnetsMentores(estructura,codigosSedes,[],[],[],{})
#imprimir_diccionario(estructura)