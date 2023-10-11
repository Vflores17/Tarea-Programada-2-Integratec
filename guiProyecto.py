from tkinter import * 
from funcionesProyecto2 import *
from tkinter import messagebox


ventana = Tk()


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

    def actualizarMatriz():
        for i in range(1,5):
            for j in range(1,3):
                matrizLabel[i][j].destroy()
        for i in range(1,5):
            for j in range(1,3):
                label = tk.Label(ventanaEstudiantesSede,width=45 if j==2 else 10,height=3,relief="solid")
                label.grid(column=j, row=i)
                label.place(x=30+(j*75), y=45+(i*40))
                matrizLabel[i][j]=label
                if i==1 and j==1:
                    matrizLabel[i][j].config(text=estructuraCarrerasCantidad.get("CTLSC",""))
                elif i==2 and j==1:
                    matrizLabel[i][j].config(text=estructuraCarrerasCantidad.get("CTLSJ",""))
                elif i==3 and j==1:
                    matrizLabel[i][j].config(text=estructuraCarrerasCantidad.get("CAL",""))
                elif i==4 and j==1:
                    matrizLabel[i][j].config(text=estructuraCarrerasCantidad.get("CTCC",""))
                elif i==5 and j==1:
                    matrizLabel[i][j].config(text=estructuraCarrerasCantidad.get("CAA",""))

    def verificarAdmitidos():
        for sede in estructuraCarrerasCantidad.keys():
            for carrera in estructuraCarrerasCantidad[sede]:
                if carrera[1]==0:
                    return False
        return True
    
    def recolectarInfo(sede,cajaTexto,menuAdmitidos):
        cantidad=cajaTexto.get()
        if cantidad.isdigit():
            estructuraCarrerasCantidad[sede]=cantidad
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
        for i in range(5):       
            for j in range(3):
                info=diccionarioVacio.get((i,j),"")
                label = tk.Label(ventanaEstudiantesSede,width=45 if j==2 else 10,height=3,relief="solid")
                label.grid(column=j, row=i)
                label.place(x=30+(j*75), y=45+(i*40))
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
    ventanaEstudiantesSede.geometry("550x300")
    ventanaEstudiantesSede.config(bg="lightblue") 

    #Texto en la ventana
    label = tk.Label(ventanaEstudiantesSede, text="Estudiantes por sede")
    label.config(fg="green", bg="lightgrey", font=("Verdana", 12))
    label.place(x=25, y=10)

    #Botones
    botonVolver = tk.Button(ventanaEstudiantesSede, text="Volver",font=("Verdana", 10),bg="red",command=cerrarVentana,fg="white")
    botonVolver.place(x=475, y=260)

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
boton2 = tk.Button(ventana, text="Estudiantes de carrera por sede",font=("Verdana", 10),state="disabled")
boton3 = tk.Button(ventana, text="Crear mentores",font=("Verdana", 10),state="disabled")
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
estructuraCarrerasCantidad=crearEstructuraEstudiantesCarreraSede()


ventana.mainloop()



