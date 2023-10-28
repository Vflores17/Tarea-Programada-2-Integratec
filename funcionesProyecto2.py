######################################################
#  Elaborado por: Vidal Flores                      ##
#  Fecha de Creación: 10/00/2023 12:10              ##
#  Fecha de última Modificación: 27/10/2023 20:56   ##
#  Versión: 3.10.4                                  ##
######################################################

#importación de librerias
import requests
from bs4 import BeautifulSoup
import random
from faker import Faker
import re
import datetime
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

#variables globales
formatoArchivo="bdIntegraTEC"
urlSedes="https://www.tec.ac.cr/carreras"
formato=r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,}$"

#Definición de funciones

def enviarCorreo(correo):
    servidor = 'smtp.gmail.com'  
    usuario = 'floresvidal001@gmail.com'  
    contra = 'dwrdpvkpqbsfvfhx' 

    
    mensaje = MIMEMultipart()
    mensaje['From'] = usuario
    mensaje['To'] = correo
    mensaje['Subject'] = 'Correo con las bases de datos IntegraTEC.'

    mensaje.attach(MIMEText('Envio de los archivos con las bases de datos del programa integraTEC.'))

    directorioArchivos = os.path.dirname(os.path.abspath(__file__))

    archivosAdjuntos = []
    for nombreArchivo in os.listdir(directorioArchivos):
        if nombreArchivo.startswith(formatoArchivo):
            archivo_completo = os.path.join(directorioArchivos, nombreArchivo)
            archivosAdjuntos.append(archivo_completo)

    if not archivosAdjuntos:
        print("No se encontraron archivos con el formato "+formatoArchivo+" en la carpeta.")
        return
    
    print(archivosAdjuntos)
    
    for archivoAdjunto in archivosAdjuntos:
        with open(archivoAdjunto, 'rb') as adjunto:
            part = MIMEApplication(adjunto.read())
            part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(archivoAdjunto))
            mensaje.attach(part)
    
    
    servidor = smtplib.SMTP_SSL(servidor)
    servidor.login(usuario, contra)

    servidor.sendmail(usuario, correo, mensaje.as_string())

    servidor.quit()

def generarArchivo(estudiantes,mentores,nombre):
    """Funcionamiento: Esta función se encarga de generar un archivo CSV con datos de estudiantes y mentores. Los datos se proporcionan en forma de listas y se organizan en el archivo CSV con encabezados específicos.
        Entradas:
            estudiantes [list]: Una lista que contiene los datos de los estudiantes a incluir en el archivo CSV.
            mentores [list]: Una lista que contiene los datos de los mentores a incluir en el archivo CSV.
            nombre [str]: El nombre del archivo CSV que se generará.
        Salidas: 
            No tiene salidas directas, pero crea un archivo CSV con los datos de estudiantes y mentores organizados en columnas, con los encabezados apropiados.
  """
    encabezadosEstudiantes = ["Sede", "Carrera", "Carnet", "Nombre", "Correo", "Teléfono", "Estudiante"]
    encabezadosMentores = ["Sede", "Carrera", "Carnet", "Nombre", "Correo", "Mentor"]
    with open(f"{nombre}.csv", mode='w', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(encabezadosEstudiantes) 
        for estudiante in estudiantes:
            writer.writerow(estudiante)

        writer.writerow(encabezadosMentores)

        for mentor in mentores:
            writer.writerow(mentor)  

def crearBaseDatos(diccEstudiantes,diccMentores):
    """Funcionamiento: Esta función crea una base de datos con información de estudiantes y mentores y guarda los datos en un archivo CSV. Los datos se toman de los diccionarios diccEstudiantes y diccMentores, y se organizan en el archivo de salida.
        Entradas:
            diccEstudiantes [dict]: Un diccionario con información de estudiantes.
            diccMentores [dict]: Un diccionario con información de mentores.
        Salidas: 
            No tiene salidas directas, pero genera un archivo CSV con los datos de estudiantes y mentores.
    """
    
    fecha=datetime.datetime.now().strftime("%d-%m-%Y_%H-%M")
    infoEstudiantes=[]
    infoMentores=[]
    nombre="bdIntegraTEC"+fecha
    for estudiante in diccEstudiantes.keys():
        info=[]
        info=[diccEstudiantes[estudiante][3],diccEstudiantes[estudiante][4],estudiante,diccEstudiantes[estudiante][0],diccEstudiantes[estudiante][2],diccEstudiantes[estudiante][1],True]
        infoEstudiantes.append(info)
    for sede in diccMentores.keys():
        for mentor in diccMentores[sede]:
            info=[]
            info=[sede,mentor[2],mentor[0],mentor[1],mentor[3],False]
            infoMentores.append(info)
    print(nombre)
    generarArchivo(infoEstudiantes,infoMentores,nombre)

    print("Base de datos creada con éxito.")
        
def obtenerCarreras(estructura):
    """Funcionamiento: Esta función recopila una lista de todas las carreras disponibles a partir de una estructura dada. La estructura es un diccionario que contiene información sobre las carreras en diferentes sedes.
        Entradas:
            estructura [dict]: Un diccionario que contiene información sobre las carreras en diferentes sedes.
        Salidas: 
            Una lista que contiene los nombres de todas las carreras disponibles.
    """
    carreras=[]
    for sede in estructura.keys():
        for carrera in estructura[sede]:
            if carrera[0] not in carreras:
                carreras.append(carrera[0])
    return carreras

def generarReporteMentor(diccMentores, diccEstudiantes):
    """Funcionamiento: Esta función genera un reporte en formato HTML que muestra información sobre los mentores y los estudiantes asignados a cada mentor. Utiliza los diccionarios diccMentores y diccEstudiantes para obtener los datos.
        Entradas:
            diccMentores [dict]: Un diccionario con información de los mentores.
            diccEstudiantes [dict]: Un diccionario con información de los estudiantes.
        Salidas: 
            No tiene salidas directas, pero crea un archivo HTML que contiene el reporte.
    """
    with open("Reporte por mentor.html", "w", encoding="utf-8") as reporte:
        reporte.write('''<html>
                           <head>
                               <title>Reporte de mentores</title>
                           </head>
                           <body>
                               <h1>Reporte de los mentores carrera.</h1>
                               ''')

        for sede, mentores in diccMentores.items():
            reporte.write(f'<h2>Sede: {sede}</h2>')

            if not mentores:
                reporte.write('<p>No hay mentores para esta sede.</p>')
            else:
                for mentor in mentores:
                    mentorNombre = mentor[1][0]
                    mentorCarnet = mentor[0]
                    reporte.write(f'''<h3>Mentor: {mentorNombre}</h3>
                                  <table border='1'>
                                       <tr bgcolor="0C9208">
                                            <th style="color: white;"> </th>
                                            <th style="color: white;">Carnet del estudiante</th>
                                            <th style="color: white;">Nombre del estudiante</th>     
                                       </tr>\n''')

                    estudiantesAsignados = []
                    contador = 1  

                    for carnet, estudianteInfo in diccEstudiantes.items():
                        if estudianteInfo[-1] == mentorCarnet:
                            estudiantesAsignados.append((carnet, estudianteInfo[0]))

                    if estudiantesAsignados:
                        for carnet, nombreEstudiante in estudiantesAsignados:
                            tupla=nombreEstudiante
                            nombre=tupla[0]
                            papellido=tupla[1]
                            sapellido= tupla[2]
                            reporte.write(f'''
                                        <tr  style="background-color: #D7BCE9;">
                                        <td align="center">{contador}</td>
                                        <td align="center">{carnet}</td>
                                        <td align="center">{nombre + " " + papellido + " "+ sapellido}</td>
                                    </tr>\n''')
                            contador += 1
                    else:
                        reporte.write('<p>No hay estudiantes asignados a este mentor.</p>')
                    reporte.write('''</table>\n''')

        reporte.write('''</body>
                        </html>''')

    print("Reporte por mentor generado con éxito.")

def extraerInfoCarrera(diccEstudiantes,lista):
    """Funcionamiento: Esta función extrae información específica de los estudiantes cuyos carnets coinciden con los elementos de una lista dada. La información se obtiene del diccionario diccEstudiantes.
        Entradas:
            diccEstudiantes [dict]: Un diccionario con información de estudiantes.
            lista [list]: Una lista de carnets de estudiantes de interés.
        Salidas: 
            Una lista que contiene la información de los estudiantes cuyos carnets coinciden con los elementos de la lista proporcionada.
    """
    info=[]
    for estudiante in diccEstudiantes.keys():
        for i in lista:
            if estudiante==i:
                info.append(diccEstudiantes[estudiante])
                continue
    return info

def generarReporteCarrera(estructura, diccEstudiantes, carrera):
    """Funcionamiento: Esta función genera un informe en formato HTML que muestra información sobre estudiantes inscritos en una carrera específica. Utiliza la estructura de carreras, el diccionario diccEstudiantes y el nombre de la carrera como entrada. El informe incluye detalles como el nombre del estudiante, teléfono, correo institucional, sede del estudiante y carnet del mentor.
        Entradas:
            estructura [dict]: Un diccionario que contiene información sobre las carreras en diferentes sedes.
            diccEstudiantes [dict]: Un diccionario con información de los estudiantes.
            carrera [str]: El nombre de la carrera de interés.
        Salidas: 
            No tiene salidas directas, pero crea un archivo HTML que contiene el informe.
    """
    with open("Reporte por carrera.html", "w", encoding="utf-8") as reporte:
        reporte.write('''<html>
                           <head>
                               <title>Reporte por carrera</title>
                           </head>
                           <body>
                               <h1>Reporte por carrera.</h1>
                               <h2>{}</h2>
                               <table border='1'>
                                   <tr bgcolor="0C9208">
                                        <th style="color: white;">Nombre del estudiante</th>
                                        <th style="color: white;">Teléfono</th>
                                        <th style="color: white;">Correo institucional</th>
                                        <th style="color: white;">Sede del estudiante</th>
                                        <th style="color: white;">Carnet del mentor</th>
                                   </tr>\n'''.format(carrera))

        i = 1

        for sede in estructura.keys():
            info = extraerInfoCarrera(diccEstudiantes, extraerEstudiantesSedeCarrera(diccEstudiantes, sede, carrera))
            for infoCompleta in info:
                tupla = infoCompleta[0]
                nombre=tupla[0]
                papellido=tupla[1]
                sapellido= tupla[2]
                telefono = infoCompleta[1]
                correo = infoCompleta[2]
                sede = infoCompleta[3]
                mentor = infoCompleta[5]
                reporte.write(f'''<tr  style="background-color: #D7BCE9;">
                                    <td align="center">{i}. {nombre + " " + papellido +" "+ sapellido}</td>
                                    <td align="center">{telefono}</td>
                                    <td align="center">{correo}</td>
                                    <td align="center">{sede}</td>
                                    <td align="center">{mentor}</td>
                                </tr>\n''')
                i += 1  
            
        reporte.write('''</table>
                        </body>
                        </html>''')

    print("Reporte por carrera generado con éxito.")

def extraerInformacionSede(diccEstudiantes,lista):
    """Funcionamiento: Esta función extrae información específica de los estudiantes cuyos carnets coinciden con los elementos de una lista dada. La información se obtiene del diccionario diccEstudiantes.
        Entradas:
            diccEstudiantes [dict]: Un diccionario con información de estudiantes.
            lista [list]: Una lista de carnets de estudiantes de interés.
        Salidas: 
            Una lista que contiene la información de los estudiantes cuyos carnets coinciden con los elementos de la lista proporcionada.
    """
    info=[]
    for estudiante in diccEstudiantes.keys():
        for i in lista:
            if estudiante==i:
                info.append(diccEstudiantes[estudiante])
                continue
    return info

def generarReporteSede(estructura, diccEstudiantes, inicialesSedes):
    """Funcionamiento: Esta función genera un informe en formato HTML que muestra información sobre estudiantes inscritos en diferentes carreras y sedes. Utiliza la estructura de carreras, el diccionario diccEstudiantes, y las iniciales de las sedes como entrada. El informe incluye detalles como el nombre del estudiante, teléfono, correo institucional, carrera, y carnet del mentor.
        Entradas:
            estructura [dict]: Un diccionario que contiene información sobre las carreras en diferentes sedes.
            diccEstudiantes [dict]: Un diccionario con información de los estudiantes.
            inicialesSedes [dict]: Un diccionario que relaciona iniciales de sedes con nombres completos de sedes.
        Salidas: 
            No tiene salidas directas, pero crea un archivo HTML que contiene el informe.
    """
    with open("Reporte por sede.html", "w", encoding="utf-8") as reporte:
        reporte.write('''<html>
                           <head>
                               <title>Reporte por sede</title>
                           </head>
                           <body>
                               <h1>Reporte por sede.</h1>''')
        for sede in estructura.keys():
            sedeNombre = extraerLlavePorValor(inicialesSedes, sede)
            reporte.write(f'<h2>{sedeNombre}</h2>')

            reporte.write('''<table border='1'>
                               <tr bgcolor="0C9208">
                                   <th style="color: white;">Carrera</th>
                                   <th style="color: white;">Nombre del estudiante</th>
                                   <th style="color: white;">Teléfono</th>
                                   <th style="color: white;">Correo institucional</th>
                                   <th style="color: white;">Carnet del mentor</th>
                               </tr>\n''')
            for pos, carrera in enumerate(estructura[sede]):
                estudiantes = extraerInformacionSede(diccEstudiantes, extraerEstudiantesSedeCarrera(diccEstudiantes, sede, carrera[0]))

                for idx, estudiante in enumerate(estudiantes):
                    tupla = estudiante[0]
                    nombre = tupla[0]
                    papellido = tupla[1]
                    sapellido = tupla[2]
                    telefono = estudiante[1]
                    correo = estudiante[2]
                    mentor = estudiante[5]

                    reporte.write(f'<tr style="background-color: #D7BCE9;">')
                    if idx == 0:
                        
                        reporte.write(f'<td align="center" rowspan="{len(estudiantes)}">{carrera[0]}</td>')

                    reporte.write(f'''<td align="center">{nombre + " " + papellido + " " + sapellido}</td>
                                    <td align="center">{telefono}</td>
                                    <td align="center">{correo}</td>
                                    <td align="center">{mentor}</td>
                                </tr>\n''')

            reporte.write('</table>')

        reporte.write('''</body>
                            </html>''')

    print("Reporte por sede generado con éxito.")

def extraerMentoresSedeCarrera(diccMentores, sede, carrera):
    """Funcionamiento: Esta función extrae a los mentores de una sede y carrera específica del diccionario diccMentores.
        Entradas:
            diccMentores [dict]: Un diccionario con información de los mentores.
            sede [str]: La sede de interés.
            carrera [str]: La carrera de interés.
        Salidas: 
            Una lista de mentores que corresponden a la sede y carrera especificadas.
    """
    mentoresCarrera = []
    for mentor in diccMentores[sede]:
        carreraMentor = mentor[2]
        if carreraMentor == carrera:
            mentoresCarrera.append(mentor)
    return mentoresCarrera

def extraerEstudiantesSedeCarrera(diccEstudiantes, sede, carrera):
    """Funcionamiento: Esta función extrae a los estudiantes de una sede y carrera específica del diccionario diccEstudiantes.
        Entradas:
            diccEstudiantes [dict]: Un diccionario con información de estudiantes.
            sede [str]: La sede de interés.
            carrera [str]: La carrera de interés.
        Salidas: 
            Una lista de carnets de estudiantes que corresponden a la sede y carrera especificadas.
    """
    estudiantesCarreraSede = []
    for estudiante in diccEstudiantes.keys():
        sedeEstudiante = diccEstudiantes[estudiante][3]  
        carreraEstudiante = diccEstudiantes[estudiante][4] 
        if sedeEstudiante == sede and carreraEstudiante == carrera:
            estudiantesCarreraSede.append(estudiante)
    return estudiantesCarreraSede

def asignarMentores(diccEstudiantes, diccMentores, estructura):
    """Funcionamiento: Esta función asigna mentores a los estudiantes en base a la estructura de carreras y sedes, asegurándose de que los estudiantes se asignen de manera equitativa a los mentores disponibles, con un máximo de 5 estudiantes por mentor.
        Entradas:
            diccEstudiantes [dict]: Un diccionario con información de los estudiantes.
            diccMentores [dict]: Un diccionario con información de los mentores.
            estructura [dict]: Un diccionario que contiene información sobre las carreras en diferentes sedes.
        Salidas: 
            Un diccionario actualizado de estudiantes con los carnets de sus mentores asignados.
    """
    for sede in estructura.keys():
        for carrera in estructura[sede]:
            estudiantesSedeCarrera = extraerEstudiantesSedeCarrera(diccEstudiantes, sede, carrera[0])
            mentores = extraerMentoresSedeCarrera(diccMentores, sede, carrera[0])
            cantidadEstudiantes = len(estudiantesSedeCarrera)
            cantidadMentores = len(mentores)
            if cantidadMentores == 0:
                print("No hay mentores para la carrera", carrera[0], "en la sede", sede)
                continue
            estudiantesMentor = cantidadEstudiantes // cantidadMentores
            estudiantesSobrantes = cantidadEstudiantes % cantidadMentores
            i = 0
            estudiantes_asignados = 0
            for mentor in mentores:
                asignarEstudiantes = estudiantesMentor
                if estudiantesSobrantes > 0:
                    asignarEstudiantes += 1
                    estudiantesSobrantes -= 1
                for i in range(asignarEstudiantes):
                    if estudiantes_asignados < 5:
                        estudiante = estudiantesSedeCarrera[i]
                        diccEstudiantes[estudiante][5] = mentor[0]
                        i += 1
                        estudiantes_asignados += 1

    return diccEstudiantes


def generarCarnetsMentores(estructuraCarrerasCantidad,codigosSedes,totalCarnets,totalCorreos,diccMentores):
    """Funcionamiento: Esta función genera carnets para los mentores. Utiliza la estructura de carreras y sedes, así como un conjunto de carnets y correos existentes, para asignar un carnet único a cada mentor y garantizar que no haya duplicados. Los datos generados se almacenan en el diccionario diccMentores.
        Entradas:
            estructuraCarrerasCantidad [dict]: Un diccionario con información sobre la cantidad de mentores que se generarán para cada carrera en cada sede.
            codigosSedes [dict]: Un diccionario con códigos de sedes.
            totalCarnets [list]: Una lista que contiene todos los carnets existentes.
            totalCorreos [list]: Una lista que contiene todos los correos existentes.
            diccMentores [dict]: Un diccionario que almacenará los datos de los mentores.
        Salidas: 
            El diccionario diccMentores actualizado con la información de los mentores y las listas totalCarnets y totalCorreos que contienen los nuevos carnets y correos generados.
    """
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
                    
    return diccMentores,totalCarnets,totalCorreos

def obtenerSedesCarreras(inicialesSedes):
    """Funcionamiento: Esta función obtiene información sobre las carreras en diferentes sedes a partir de una URL. Utiliza solicitudes web para acceder al contenido de la URL y BeautifulSoup para analizar el HTML y extraer los nombres de las carreras por sede.
        Entradas:
            inicialesSedes [dict]: Un diccionario que relaciona las iniciales de las sedes con los nombres completos de las sedes.
        Salidas: 
            Un diccionario que contiene las carreras por sede.
    """
    carrerasSede = {}
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
    """Funcionamiento: Esta función genera un número de carnet basado en una sede y un número aleatorio. La estructura del carnet varía dependiendo del valor del argumento gen.
        Entradas:
            gen [int]: Un valor que determina la estructura del carnet (1 o 2).
            sede [str]: Un código de sede.
        Salidas: 
            Un número de carnet generado de acuerdo a la estructura.
    """
    numRandom = random.randint(1000, 9999)
    if gen == 1:
        nuevoCarnet = "2024" + sede + str(numRandom)
    else:
        nuevoCarnet = "2023" + sede + str(numRandom)
    return nuevoCarnet

def generarDatos(opcion,pnombre,papellido1):
    """Funcionamiento: Esta función genera datos aleatorios como nombres, apellidos, teléfonos y correos electrónicos basados en las opciones proporcionadas.
        Entradas:
            opcion [int]: Un valor que determina qué tipo de dato se generará (1, 2 o 3).
            pnombre [str]: El primer nombre (solo para opción 3).
            papellido1 [str]: El primer apellido (solo para opción 3).
        Salidas:
            Para opción 1: una tupla que contiene un nombre completo, un número de teléfono y un correo electrónico.
            Para opción 2: un número de teléfono aleatorio.
            Para opción 3: un correo electrónico generado con base en el primer nombre y primer apellido dados.
    """
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
    """Funcionamiento: Esta función genera carnets para los estudiantes. Utiliza la estructura de carreras y sedes, así como un conjunto de carnets, números de teléfono y correos existentes, para asignar un carnet único a cada estudiante y garantizar que no haya duplicados. Los datos generados se almacenan en el diccionario diccEstudiantes.
        Entradas:
            totalAdmitidos [dict]: Un diccionario que contiene la cantidad de admitidos por sede.
            estructuraCarrerasCantidad [dict]: Un diccionario con información sobre la cantidad de estudiantes que se generarán para cada carrera en cada sede.
            codigosSedes [dict]: Un diccionario con códigos de sedes.
            totalCarnets [list]: Una lista que contiene todos los carnets existentes.
            totalNumeros [list]: Una lista que contiene todos los números de teléfono existentes.
            totalCorreos [list]: Una lista que contiene todos los correos existentes.
            diccEstudiantes [dict]: Un diccionario que almacenará los datos de los estudiantes.
        Salidas: 
            El diccionario diccEstudiantes actualizado con la información de los estudiantes y las listas totalCarnets, totalNumeros y totalCorreos que contienen los nuevos carnets, números de teléfono y correos generados.
    """
    
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

    return diccEstudiantes,totalCarnets,totalNumeros,totalCorreos

def validarCorreo(correo):
    """Funcionamiento: Esta función valida si una dirección de correo electrónico cumple con un formato determinado utilizando una expresión regular. Si el correo cumple con el formato, la función devuelve True, de lo contrario, devuelve False.
        Entradas:
            correo [str]: La dirección de correo electrónico que se va a validar.
        Salidas:
            True si el correo cumple con el formato especificado.
            False si el correo no cumple con el formato especificado.
    """
    if re.match(formato,correo):
        return True
    else:
        return False
       
def extraerLlavePorValor(diccionario, valorBuscado):
    """Funcionamiento: Esta función busca una clave en un diccionario que corresponda a un valor específico. Recorre el diccionario y compara el valor deseado con los valores de las claves. Si encuentra una coincidencia, devuelve la clave. Si no se encuentra ninguna coincidencia, se devuelve None.
        Entradas:
            diccionario [dict]: El diccionario en el que se busca la clave.
            valorBuscado [any]: El valor que se desea encontrar en el diccionario.
        Salidas:
            La clave que corresponde al valor buscado.
            None si no se encuentra una clave que coincida con el valor buscado.
    """
    for clave, valor in diccionario.items():
        if valor == valorBuscado:
            return clave
    return None
