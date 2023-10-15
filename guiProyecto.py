from tkinter import * 
from funcionesProyecto2 import *
from tkinter import messagebox
import random

ventana = Tk()
totalAdmitidos={"CTLSC":175,"CTLSJ":75,"CAL":75,"CTCC":625,"CAA":50}
estructuraCarrerasCantidad={'CTLSC': [['Bachillerato en Administración de Empresas', 0], ['Bachillerato en Gestión del Turismo Rural Sostenible', 0], ['Bachillerato en Gestión en Sostenibilidad Turística', 0], ['Bachillerato en Ingeniería en Computación', 0], ['Licenciatura en Ingeniería Electrónica', 0], ['Licenciatura en Ingeniería en Agronomía', 0], ['Licenciatura en Ingeniería en Producción Industrial', 0]], 'CTLSJ': [['Bachillerato en Administración de Empresas', 0], ['Bachillerato en Ingeniería en Computación', 0], ['Licenciatura en Arquitectura', 0]], 'CAL': [['Bachillerato en Administración de Empresas', 0], ['Bachillerato en Ingeniería en Computación', 0], ['Bachillerato en Producción Industrial,  Limón', 0]], 'CTCC': [['Bachillerato en Administración de Empresas', 0], ['Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 0], ['Bachillerato en Gestión del Turismo Sostenible', 0], ['Bachillerato en Ingeniería en Biotecnología', 0], ['Bachillerato en Ingeniería en Computación', 0], ['Licenciatura en Administración de Tecnología de Información', 0], ['Licenciatura en Ingeniería Agrícola', 0], ['Licenciatura en Ingeniería Ambiental', 0], ['Licenciatura en Ingeniería Electrónica', 0], ['Licenciatura en Ingeniería en Agronegocios', 0], ['Licenciatura en Ingeniería en Computadores', 0], ['Licenciatura en Ingeniería en Construcción', 0], ['Licenciatura en Ingeniería en Diseño Industrial', 0], ['Licenciatura en Ingeniería en Materiales', 0], ['Licenciatura en Ingeniería en Producción Industrial', 0], ['Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 0], ['Licenciatura en Ingeniería Física', 0], ['Licenciatura en Ingeniería Forestal', 0], ['Licenciatura en Ingeniería Mecatrónica', 0], ['Licenciatura en Mantenimiento Industrial', 0]], 'CAA': [['Bachillerato en Ingeniería en Computación', 0], ['Licenciatura en Ingeniería Electrónica', 0]]}
#estructuraCarrerasCantidad={'CTLSC': [['Bachillerato en Administración de Empresas', 25], ['Bachillerato en Gestión del Turismo Rural Sostenible', 25], ['Bachillerato en Gestión en Sostenibilidad Turística', 25], ['Bachillerato en Ingeniería en Computación', 25], ['Licenciatura en Ingeniería Electrónica', 25], ['Licenciatura en Ingeniería en Agronomía', 25], ['Licenciatura en Ingeniería en Producción Industrial', 25]], 'CTLSJ': [['Bachillerato en Administración de Empresas', 25], ['Bachillerato en Ingeniería en Computación', 25], ['Licenciatura en Arquitectura', 25]], 'CAL': [['Bachillerato en Administración de Empresas', 25], ['Bachillerato en Ingeniería en Computación', 25], ['Bachillerato en Producción Industrial,  Limón', 25]], 'CTCC': [['Bachillerato en Administración de Empresas', 25], ['Bachillerato en Enseñanza de la Matemática con Entornos Tecnológicos', 25], ['Bachillerato en Gestión del Turismo Sostenible', 25], ['Bachillerato en Ingeniería en Biotecnología', 25], ['Bachillerato en Ingeniería en Computación', 25], ['Licenciatura en Administración de Tecnología de Información', 25], ['Licenciatura en Ingeniería Agrícola', 25], ['Licenciatura en Ingeniería Ambiental', 25], ['Licenciatura en Ingeniería Electrónica', 25], ['Licenciatura en Ingeniería en Agronegocios', 25], ['Licenciatura en Ingeniería en Computadores', 25], ['Licenciatura en Ingeniería en Construcción', 25], ['Licenciatura en Ingeniería en Diseño Industrial', 25], ['Licenciatura en Ingeniería en Materiales', 25], ['Licenciatura en Ingeniería en Producción Industrial', 25], ['Licenciatura en Ingeniería en Seguridad Laboral e Higiene Ambiental', 25], ['Licenciatura en Ingeniería Física', 25], ['Licenciatura en Ingeniería Forestal', 25], ['Licenciatura en Ingeniería Mecatrónica', 25], ['Licenciatura en Mantenimiento Industrial', 25]], 'CAA': [['Bachillerato en Ingeniería en Computación', 25], ['Licenciatura en Ingeniería Electrónica', 25]]}

totalCarnets={}
codigosSedes = {"CTLSC": "02", "CTLSJ": "03", "CAL": "05", "CTCC": "01", "CAA": "04"}
totalCarnets = []
totalNumeros = []
totalCorreos = []
diccEstudiantes = {}
diccMentores={}


def crearMentores(diccMentores):
    
    def mostrarInfo():
        for i in range(1, 6):
            for j in range(1, 2):
                matrizLabel[i][j].destroy()
                
        sedes = diccMentores.keys()
        
        for i, sede in enumerate(sedes, start=1):
            for j in range(1, 2):
                contenido = "\n".join([f"{sede[0]}: {sede[1:]}" for sede in diccMentores.get(sede, [])])
                print(contenido)

                text = tk.Text(ventanaMentores, width=130 if j == 1 else 10, height=4, relief="solid")
                text.grid(column=j, row=i)
                text.place(x=51 + (j * 75), y=46 + (i * 70))
                text.insert("1.0", contenido)
                text.tag_configure("center", justify="center")
                text.tag_add("center", "1.0", "end")
                text.config(state="disabled")
                matrizLabel[i][j] = text
    
    def cerrarVentanaMentores():
        ventanaMentores.destroy()
        ventana.deiconify()

    ventanaMentores = tk.Toplevel(ventana)
    ventanaMentores.title("Pestaña de los mentores")
    ventanaMentores.geometry("1185x525")
    ventanaMentores.config(bg="lightblue")
    ventana.withdraw()

    #Texto en la ventana
    label = tk.Label(ventanaMentores, text="Pestaña de los mentores")
    label.config(fg="green", bg="lightgrey", font=("Verdana", 12))
    label.place(x=25, y=10)

    #Botones
    botonVolver = tk.Button(ventanaMentores, text="Volver",font=("Verdana", 10),bg="red",command=cerrarVentanaMentores,fg="white")
    botonVolver.place(x=1110, y=485)

    matrizLabel = [[None for _ in range(2)] for _ in range(6)]

    diccMentores={}
    diccMentores=generarCarnetsMentores(estructuraCarrerasCantidad,codigosSedes,totalCarnets,totalNumeros,totalCorreos,diccMentores)

    diccionarioVacio={(0,0):"Sede", (0,1):"Información de mentores", (1,0):"CTLSC", (2,0):"CTLSJ", (3,0):"CAL", (4,0):"CTCC", (5,0):"CAA"}
    
    for i in range(6):       
        for j in range(2):
            info=diccionarioVacio.get((i,j),"")
            label = tk.Label(ventanaMentores,width=148 if j == 1 else 10,height=4,relief="solid",anchor=CENTER)
            label.grid(column=j, row=i)
            label.place(x=50+(j*75), y=45+(i*69))
            matrizLabel[i][j]=label
            matrizLabel[i][j].config(text=info)

    mostrarInfo()

    #botonActualizar = tk.Button(ventanaMentores,text="Actualizar matriz",font=("Verdana",10),command = mostrarInfo,bg="green",fg="white")
    #botonActualizar.place(x=625,y=485)
    
    
    
      
    


def estudiantesCarreraPorSede(totalCarnets,diccEstudiantes):
    diccEstudiantes={}
    diccEstudiantes=generarCarnetsEstudiantes(totalAdmitidos, estructuraCarrerasCantidad,codigosSedes,totalCarnets,totalNumeros,totalCorreos,diccEstudiantes)
    messagebox.showinfo("Información","Se han insertado satisfactoriamente la información de cada estudiantes admitido")
    return diccEstudiantes


def crearEstructuraEstudiantesCarreraSede():
    info=obtenerSedesCarreras()
    estructuraAdmitidosCarrera={}
    for sede in info.keys():
        listaAdmitidosCarrera=[]
        for carrera in info[sede]:
            listaAdmitidosCarrera.append([carrera,0])
        estructuraAdmitidosCarrera[sede]=listaAdmitidosCarrera
    
    return estructuraAdmitidosCarrera

def estudiantesPorSede():
    
    def distribuirAdmitidos(totalAdmitidos, estructuraCarrerasCantidad):
        for sede, carreras in estructuraCarrerasCantidad.items():
            total_cupos = totalAdmitidos[sede]

            for carrera in carreras[:-1]:
                cupos = total_cupos // random.randint(4, 9)
                carrera[1] = cupos
                total_cupos -= cupos

            carrera = carreras[-1]
            carrera[1] = total_cupos

        return estructuraCarrerasCantidad

    def actualizarMatriz():
        for i in range(1, 6):
            for j in range(1, 3):
                matrizLabel[i][j].destroy()
                
        sedes = totalAdmitidos.keys()
        
        for i, sede in enumerate(sedes, start=1):
            for j in range(1, 3):
                if j == 1:
                    contenido = totalAdmitidos.get(sede, "")
                else:
                    contenido = "\n".join([f"{carrera[0]}: {carrera[1]}" for carrera in estructuraCarrerasCantidad.get(sede, [])])

                text = tk.Text(ventanaEstudiantesSede, width=72 if j == 2 else 10, height=4, relief="solid")
                text.grid(column=j, row=i)
                text.place(x=30 + (j * 75), y=40 + (i * 70))
                text.insert("1.0", contenido)
                text.tag_configure("center", justify="center")
                text.tag_add("center", "1.0", "end")
                text.config(state="disabled")
                matrizLabel[i][j] = text

   
    def verificarAdmitidos():
        for sede in totalAdmitidos.keys():
            if totalAdmitidos[sede]==0:
                return False
        return True

    def recolectarInfo(sede,cajaTexto,menuAdmitidos):
        cantidad=cajaTexto.get()
        if cantidad.isdigit():
            totalAdmitidos[sede]=int(cantidad)
            distribuirAdmitidos(totalAdmitidos,estructuraCarrerasCantidad)
            menuAdmitidos.destroy()
        else:
            messagebox.showerror("Error", "Debe ingresar valores númericos enteros unicamente")
            cajaTexto.delete(0,END)
    
    def menuAdmitidos(sede):
        menuAdmitidos=tk.Toplevel(ventanaEstudiantesSede)
        menuAdmitidos.title("Ingrese cantidad de estudiantes admitidos")
        menuAdmitidos.geometry("400x150")
        menuAdmitidos.config(bg="lightblue")
        cajaTexto = tk.Entry(menuAdmitidos)
        cajaTexto.place(x=100, y=50)
        
        botonAceptar = tk.Button(menuAdmitidos, text="Agregar",font=("Verdana", 10),bg="green",command=lambda:recolectarInfo(sede,cajaTexto,menuAdmitidos),fg="white")
        botonAceptar.place(x=150, y=100)
        
        

    def mostrarMatrizVacia():

        diccionarioVacio={(0,0):"Sede", (0,1):"Admitidos",(0,2):"Cantidad de estudiantes por carrera", (1,0):"CTLSC", (2,0):"CTLSJ", (3,0):"CAL", (4,0):"CTCC", (5,0):"CAA"}
        for i in range(6):       
            for j in range(3):
                info=diccionarioVacio.get((i,j),"")
                label = tk.Label(ventanaEstudiantesSede,width=82 if j==2 else 10,height=4,relief="solid",anchor=CENTER)
                label.grid(column=j, row=i)
                label.place(x=30+(j*75), y=45+(i*69))
                matrizLabel[i][j]=label
                matrizLabel[i][j].config(text=info)
          
    def cerrarVentana():
        if verificarAdmitidos():
            ventanaEstudiantesSede.destroy()
            habilitarOpciones()
            ventana.deiconify()
        else:
            messagebox.showerror("Error", "Debe ingresar al menos una cantidad de estudiantes admitidos por sede")

    #Configuración de la ventana
    ventana.withdraw()
    ventanaEstudiantesSede=tk.Toplevel(ventana)
    ventanaEstudiantesSede.title("Estudiantes por sede")
    ventanaEstudiantesSede.geometry("825x525")
    ventanaEstudiantesSede.config(bg="lightblue") 

    #Texto en la ventana
    label = tk.Label(ventanaEstudiantesSede, text="Estudiantes por sede")
    label.config(fg="green", bg="lightgrey", font=("Verdana", 12))
    label.place(x=25, y=10)

    #Botones
    botonVolver = tk.Button(ventanaEstudiantesSede, text="Volver",font=("Verdana", 10),bg="red",command=cerrarVentana,fg="white")
    botonVolver.place(x=750, y=485)

    #Menu desplegable
    menu = tk.Menu(ventanaEstudiantesSede)
    opciones = tk.Menu(menu,tearoff=0)
    opciones.add_command(label="Sede San Carlos", command=lambda:menuAdmitidos("CTLSC"))
    opciones.add_command(label="Sede San José", command=lambda:menuAdmitidos("CTLSJ"))
    opciones.add_command(label="Sede Limón", command=lambda:menuAdmitidos("CAL"))
    opciones.add_command(label="Sede Cartago", command=lambda:menuAdmitidos("CTCC"))
    opciones.add_command(label="Sede Alajuela", command=lambda:menuAdmitidos("CAA"))
    opciones.add_command(label="Actualizar matriz", command=actualizarMatriz)


    menu.add_cascade(label="Ingresar estudiantes admitidos", menu=opciones)
    ventanaEstudiantesSede.config(menu=menu)
    
    #MatrizVacia
    matrizLabel = [[None for _ in range(3)] for _ in range(6)]
    
    mostrarMatrizVacia()
    

def habilitarOpciones():
    boton2.config(state=tk.NORMAL)
    boton3.config(state=tk.NORMAL)
    boton4.config(state=tk.NORMAL)
    boton5.config(state=tk.NORMAL)
    boton6.config(state=tk.NORMAL)
    boton7.config(state=tk.NORMAL)
    boton8.config(state=tk.NORMAL)

#Personalización de la ventana
ventana.title("Atención a la generación de 2024.")
ventana.geometry("550x300")
#ventana.iconbitmap("logo.ico") para cambiar el icono de la aplicación
ventana.config(bg="lightblue")

#Texto en la ventana
label = tk.Label(ventana, text="Bienvenid@ a la aplicación de atención a la generación 2024.")
label.config(fg="green", bg="lightgrey", font=("Verdana", 12))
label.place(x=25, y=10)

#Creacion botones
boton1 = tk.Button(ventana, text="Estudiantes por sede",font=("Verdana", 10),command=estudiantesPorSede)
boton2 = tk.Button(ventana, text="Estudiantes de carrera por sede",font=("Verdana", 10),state="disabled",command=lambda:estudiantesCarreraPorSede(totalCarnets,diccEstudiantes))
boton3 = tk.Button(ventana, text="Crear mentores",font=("Verdana", 10),state="disabled",command=lambda:crearMentores(diccMentores))
boton4 = tk.Button(ventana, text="Asignar mentores",font=("Verdana", 10),state="disabled")
boton5 = tk.Button(ventana, text="Actualizar estudiante",font=("Verdana", 10),state="disabled")
boton6 = tk.Button(ventana, text="Generar reportes",font=("Verdana", 10),state="disabled")
boton7 = tk.Button(ventana, text="Crear base de datos en Excel",font=("Verdana", 10),state="disabled")
boton8 = tk.Button(ventana, text="Enviar correo",font=("Verdana", 10),state="disabled")
boton9 = tk.Button(ventana, text="Salir",font=("Verdana", 10),bg="red",command=ventana.destroy,fg="white")


#Posicionamiento de los botones
boton1.place(x=85, y=50)
boton2.place(x=45, y=95)
boton3.place(x=90, y=140)
boton4.place(x=85, y=185)
boton5.place(x=325, y=50)
boton6.place(x=335, y=95)
boton7.place(x=305, y=140)
boton8.place(x=335, y=185)
boton9.place(x=475, y=260)

#Creación de la estructura de datos
#estructuraCarrerasCantidad=crearEstructuraEstudiantesCarreraSede()


ventana.mainloop()


