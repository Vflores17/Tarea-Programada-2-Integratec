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
formato_archivo="bdIntegraTEC"

urlSedes="https://www.tec.ac.cr/carreras"
#totalAdmitidos={"CTLSC":175,"CTLSJ":75,"CAL":75,"CTCC":625,"CAA":50}
#estructura={'CTLSC': [['Bachillerato en Administración de Empresas', 25], ['Bachillerato en Gestión del Turismo Rural Sostenible', 25], ['Bachillerato en Gestión en Sostenibilidad Turística', 25], ['Bachillerato en Ingeniería en Computación', 25], ['Licenciatura en Ingeniería Electrónica', 25], ['Licenciatura en Ingeniería en Agronomía', 25], ['Licenciatura en Ingeniería en Producción Industrial', 25]], 'CTLSJ': [['Bachillerato en Administración de Empresas', 25], ['Bachillerato en Ingeniería en Computación', 25], ['Licenciatura en Arquitectura', 25]], 'CAL': [['Bachillerato en Administración de Empresas', 25], ['Bachillerato en Ingeniería en Computación', 25], ['Bachillerato en Producción Industrial,  Limón', 25]], 'CTCC': [['Bachillerato en Administración de Empresas', 25], ['Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 25], ['Bachillerato en Gestión del Turismo Sostenible', 25], ['Bachillerato en Ingeniería en Biotecnología', 25], ['Bachillerato en Ingeniería en Computación', 25], ['Licenciatura en Administración de Tecnología de Información', 25], ['Licenciatura en Ingeniería Agrícola', 25], ['Licenciatura en Ingeniería Ambiental', 25], ['Licenciatura en Ingeniería Electrónica', 25], ['Licenciatura en Ingeniería en Agronegocios', 25], ['Licenciatura en Ingeniería en Computadores', 25], ['Licenciatura en Ingeniería en Construcción', 25], ['Licenciatura en Ingeniería en Diseño Industrial', 25], ['Licenciatura en Ingeniería en Materiales', 25], ['Licenciatura en Ingeniería en Producción Industrial', 25], ['Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 25], ['Licenciatura en Ingeniería Física', 25], ['Licenciatura en Ingeniería Forestal', 25], ['Licenciatura en Ingeniería Mecatrónica', 25], ['Licenciatura en Mantenimiento Industrial', 25]], 'CAA': [['Bachillerato en Ingeniería en Computación', 25], ['Licenciatura en Ingeniería Electrónica', 25]]}
#diccMentores={'CTLSC': [['2023027180', ('Stacie', 'Taylor', 'Powell'), 'Bachillerato en Administración de Empresas', 'StTaylor@estudiantec.cr'], ['2023022268', ('Leslie', 'Robbins', 'Garcia'), 'Bachillerato en Gestión del Turismo Rural Sostenible', 'LeRobbins@estudiantec.cr'], ['2023023620', ('Ariel', 'Trujillo', 'Davis'), 'Bachillerato en Gestión en Sostenibilidad Turística', 'ArTrujillo@estudiantec.cr'], ['2023021783', ('Dennis', 'Tanner', 'Hensley'), 'Bachillerato en Ingeniería en Computación', 'DeTanner@estudiantec.cr'], ['2023028595', ('Christopher', 'Williams', 'Fleming'), 'Licenciatura en Ingeniería Electrónica', 'ChWilliams@estudiantec.cr'], ['2023022060', ('Lisa', 'Vang', 'Castaneda'), 'Licenciatura en Ingeniería en Agronomía', 'LiVang@estudiantec.cr'], ['2023023729', ('Vanessa', 'Williamson', 'Smith'), 'Licenciatura en Ingeniería en Producción Industrial', 'VaWilliamson@estudiantec.cr']], 'CTLSJ': [['2023033049', ('Jonathan', 'Lopez', 'Dickerson'), 'Bachillerato en Administración de Empresas', 'JoLopez@estudiantec.cr'], ['2023035141', ('Paula', 'Watts', 'Clark'), 'Bachillerato en Ingeniería en Computación', 'PaWatts@estudiantec.cr'], ['2023035984', ('Robert', 'Giles', 'Marshall'), 'Licenciatura en Arquitectura', 'RoGiles@estudiantec.cr']], 'CAL': [['2023057426', ('Julia', 'Gonzalez', 'Sanders'), 'Bachillerato en Administración de Empresas', 'JuGonzalez@estudiantec.cr'], ['2023057653', ('Marcus', 'Tanner', 'Kim'), 'Bachillerato en Ingeniería en Computación', 'MaTanner@estudiantec.cr'], ['2023056386', ('Tina', 'Collins', 'Rhodes'), 'Bachillerato en Producción Industrial,  Limón', 'TiCollins@estudiantec.cr']], 'CTCC': [['2023016134', ('Joel', 'Higgins', 'Duarte'), 'Bachillerato en Administración de Empresas', 'JoHiggins@estudiantec.cr'], ['2023018883', ('Frederick', 'Ray', 'Torres'), 'Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 'FrRay@estudiantec.cr'], ['2023013656', ('Cristina', 'Stevens', 'Lowery'), 'Bachillerato en Gestión del Turismo Sostenible', 'CrStevens@estudiantec.cr'], ['2023016929', ('Zachary', 'Cardenas', 'Ramirez'), 'Bachillerato en Ingeniería en Biotecnología', 'ZaCardenas@estudiantec.cr'], ['2023017535', ('Michelle', 'Wall', 'Ortiz'), 'Bachillerato en Ingeniería en Computación', 'MiWall@estudiantec.cr'], ['2023013096', ('Douglas', 'Jackson', 'Escobar'), 'Licenciatura en Administración de Tecnología de Información', 'DoJackson@estudiantec.cr'], ['2023013492', ('James', 'Rogers', 'Nichols'), 'Licenciatura en Ingeniería Agrícola', 'JaRogers@estudiantec.cr'], ['2023017427', ('Carol', 'Bates', 'Clark'), 'Licenciatura en Ingeniería Ambiental', 'CaBates@estudiantec.cr'], ['2023018784', ('Victor', 'Chambers', 'Gill'), 'Licenciatura en Ingeniería Electrónica', 'ViChambers@estudiantec.cr'], ['2023018140', ('Christopher', 'Marshall', 'Gates'), 'Licenciatura en Ingeniería en Agronegocios', 'ChMarshall@estudiantec.cr'], ['2023011145', ('Austin', 'Boyd', 'Cox'), 'Licenciatura en Ingeniería en Computadores', 'AuBoyd@estudiantec.cr'], ['2023015984', ('David', 'Martinez', 'Gonzales'), 'Licenciatura en Ingeniería en Construcción', 'DaMartinez@estudiantec.cr'], ['2023011617', ('Adam', 'Alvarez', 'Ross'), 'Licenciatura en Ingeniería en Diseño Industrial', 'AdAlvarez@estudiantec.cr'], ['2023016435', ('James', 'Sanders', 'King'), 'Licenciatura en Ingeniería en Materiales', 'JaSanders@estudiantec.cr'], ['2023015299', ('Phillip', 'Love', 'Thomas'), 'Licenciatura en Ingeniería en Producción Industrial', 'PhLove@estudiantec.cr'], ['2023012068', ('Jerry', 'Rodriguez', 'Leblanc'), 'Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 'JeRodriguez@estudiantec.cr'], ['2023016166', ('Patrick', 'Waller', 'Church'), 'Licenciatura en Ingeniería Física', 'PaWaller@estudiantec.cr'], ['2023016506', ('Elijah', 'Giles', 'Klein'), 'Licenciatura en Ingeniería Forestal', 'ElGiles@estudiantec.cr'], ['2023018453', ('Anna', 'Pruitt', 'Mccullough'), 'Licenciatura en Ingeniería Mecatrónica', 'AnPruitt@estudiantec.cr'], ['2023015802', ('Shannon', 'Cain', 'Houston'), 'Licenciatura en Mantenimiento Industrial', 'ShCain@estudiantec.cr']], 'CAA': [['2023041882', ('Samuel', 'Estrada', 'Reyes'), 'Bachillerato en Ingeniería en Computación', 'SaEstrada@estudiantec.cr'], ['2023049765', ('James', 'Johnson', 'Jones'), 'Licenciatura en Ingeniería Electrónica', 'JaJohnson@estudiantec.cr']]}
#codigosSedes = {"CTLSC": "02", "CTLSJ": "03", "CAL": "05", "CTCC": "01", "CAA": "04"}
formato=r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,}$"
#inicialesSedes={"Campus Tecnológico Local San Carlos": "CTLSC","Campus Tecnológico Local San José": "CTLSJ","Centro Académico de Limón": "CAL","Campus Tecnológico Central Cartago": "CTCC","Centro Académico de Alajuela": "CAA"}

def enviarCorreo(correo):

     # Configuración de la conexión SMTP
    servidor_smtp = 'smtp.gmail.com'  # Reemplaza con el servidor SMTP adecuado
    usuario = 'floresvidal001@gmail.com'  # Reemplaza con tu dirección de correo
    contraseña = 'dwrdpvkpqbsfvfhx'  # Reemplaza con tu contraseña

    # Crear un objeto MIMEMultipart
    mensaje = MIMEMultipart()
    mensaje['From'] = usuario
    mensaje['To'] = correo
    mensaje['Subject'] = 'Correo con las bases de datos IntegraTEC.'

    # Agregar texto al mensaje
    mensaje.attach(MIMEText('Envio de los archivos con las bases de datos del programa integraTEC.'))

    directorio_archivos = os.path.dirname(os.path.abspath(__file__))

    # Listar los archivos en el directorio
    archivos_adjuntos = []
    for nombre_archivo in os.listdir(directorio_archivos):
        if nombre_archivo.startswith(formato_archivo):
            archivo_completo = os.path.join(directorio_archivos, nombre_archivo)
            archivos_adjuntos.append(archivo_completo)

    if not archivos_adjuntos:
        print(f"No se encontraron archivos con el formato '{formato_archivo}' en la carpeta.")
        return
    
    print(archivos_adjuntos)
    
    for archivo_adjunto in archivos_adjuntos:
        with open(archivo_adjunto, 'rb') as adjunto:
            part = MIMEApplication(adjunto.read())
            part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(archivo_adjunto))
            mensaje.attach(part)
    
    # Establecer la conexión SMTP
    servidor = smtplib.SMTP_SSL(servidor_smtp)
    servidor.login(usuario, contraseña)

    # Enviar el correo
    servidor.sendmail(usuario, correo, mensaje.as_string())

    # Cerrar la conexión SMTP
    servidor.quit()

def generarArchivo(estudiantes,mentores,nombre):
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
    carreras=[]
    for sede in estructura.keys():
        for carrera in estructura[sede]:
            if carrera[0] not in carreras:
                carreras.append(carrera[0])
    return carreras

def generarReporteMentor(diccMentores, diccEstudiantes):
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

            for mentor in mentores:
                mentor_nombre = mentor[1][0]
                mentor_carnet = mentor[0]
                reporte.write(f'''<h3>Mentor: {mentor_nombre}</h3>
                              <table border='1'>
                                   <tr bgcolor="0C9208">
                                        <th style="color: white;"> </th>
                                        <th style="color: white;">Carnet del estudiante</th>
                                        <th style="color: white;">Nombre del estudiante</th>     
                                   </tr>\n''')

                estudiantes_asignados = []
                contador = 1  

                for carnet, estudiante_info in diccEstudiantes.items():
                    if estudiante_info[-1] == mentor_carnet:
                        estudiantes_asignados.append((carnet, estudiante_info[0]))

                if estudiantes_asignados:
                    for carnet, nombre_estudiante in estudiantes_asignados:
                        tupla=nombre_estudiante
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
    info=[]
    for estudiante in diccEstudiantes.keys():
        for i in lista:
            if estudiante==i:
                info.append(diccEstudiantes[estudiante])
                continue
    return info

def generarReporteCarrera(estructura, diccEstudiantes, carrera):
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
    info=[]
    for estudiante in diccEstudiantes.keys():
        for i in lista:
            if estudiante==i:
                info.append(diccEstudiantes[estudiante])
                continue
    return info

def generarReporteSede(estructura, diccEstudiantes, inicialesSedes):
    with open("Reporte por sede.html", "w", encoding="utf-8") as reporte:
        reporte.write('''<html>
                           <head>
                               <title>Reporte por sede</title>
                           </head>
                           <body>
                               <h1>Reporte por sede.</h1>''')
        for sede in estructura.keys():
            sede_nombre = obtener_clave_por_valor(inicialesSedes, sede)
            reporte.write(f'<h2>{sede_nombre}</h2>')

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
    mentoresCarrera = []
    for mentor in diccMentores[sede]:
        carreraMentor = mentor[2]
        if carreraMentor == carrera:
            mentoresCarrera.append(mentor)
    return mentoresCarrera

def extraerEstudiantesSedeCarrera(diccEstudiantes, sede, carrera):
    estudiantesCarreraSede = []
    for estudiante in diccEstudiantes.keys():
        sedeEstudiante = diccEstudiantes[estudiante][3]  
        carreraEstudiante = diccEstudiantes[estudiante][4] 
        if sedeEstudiante == sede and carreraEstudiante == carrera:
            estudiantesCarreraSede.append(estudiante)
    return estudiantesCarreraSede

def asignarMentores(diccEstudiantes, diccMentores, estructura):
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
            for mentor in mentores:
                asignarEstudiantes = estudiantesMentor
                if estudiantesSobrantes > 0:
                    asignarEstudiantes += 1
                    estudiantesSobrantes -= 1
                for i in range(asignarEstudiantes):
                    
                    estudiante = estudiantesSedeCarrera[i]
                    diccEstudiantes[estudiante][5] = mentor[0] 
                    i += 1

    return diccEstudiantes

def generarCarnetsMentores(estructuraCarrerasCantidad,codigosSedes,totalCarnets,totalCorreos,diccMentores):
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

    return diccEstudiantes,totalCarnets,totalNumeros,totalCorreos

def validarCorreo(correo):
    if re.match(formato,correo):
        return True
    else:
        return False

def imprimir_diccionario(diccionario):
    print("{")
    for clave, valor in diccionario.items():
        print("'",clave,"'" ":", valor,",")
    print("}")        

def obtener_clave_por_valor(diccionario, valor_buscado):
    for clave, valor in diccionario.items():
        if valor == valor_buscado:
            return clave
    # Si no se encuentra el valor, puedes devolver None u otro valor predeterminado.
    return None
