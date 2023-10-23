######################################################
#  Elaborado por: Vidal Flores                      ##
#  Fecha de Creación: 10/00/2023 12:10              ##
#  Fecha de última Modificación: 27/10/2023 20:56   ##
#  Versión: 3.10.4                                  ##
######################################################

#importación de librerias
from tkinter import * 
from funcionesProyecto2 import *
from tkinter import messagebox
import random
import tkinter as tk

#variables globales
ventana = Tk()
totalAdmitidos={"CTLSC":0,"CTLSJ":0,"CAL":0,"CTCC":0,"CAA":0}
totalCarnets=[]
codigosSedes = {"CTLSC": "02", "CTLSJ": "03", "CAL": "05", "CTCC": "01", "CAA": "04"}
totalCarnets=[]
totalNumeros=[]
totalCorreos=[]
diccEstudiantes={}
diccMentores={}
carnet=""
inicialesSedes={"Campus Tecnológico Local San Carlos": "CTLSC","Campus Tecnológico Local San José": "CTLSJ","Centro Académico de Limón": "CAL","Campus Tecnológico Central Cartago": "CTCC","Centro Académico de Alajuela": "CAA"}
sedeMentor=""

#Definición de funciones

def opcionEnviarCorreo():
    """Funcionamiento: Función para que se ejecute cuando se accione el boton de enviar correo.
        Entradas:
        No tiene entradas.
        Salidas:
        No tiene salidas.
        """

    def opcionEnviarCorreo(cajaTexto):
        """Funcionamiento: Esta función es la función principal que se llama al hacer clic en el botón "Enviar" en la ventana de correo. Obtiene el valor de correo de la caja de texto, valida si es una dirección de correo válida y envía un correo si es válido. Muestra un mensaje de éxito o error en función de la validación.
        Entradas:
        - cajaTexto [tk.Entry]: La caja de texto donde el usuario ingresa la dirección de correo.
        Salidas:
        No tiene salidas directas, pero muestra mensajes de éxito o error mediante messagebox.showinfo.    
        """   
        correo=cajaTexto.get()
        if len(correo)>0 and validarCorreo(correo):
            enviarCorreo(correo)
            messagebox.showinfo("Correo enviado", "El correo se ha enviado con éxito.")
            cajaTexto.delete(0, tk.END)
        else:
            messagebox.showinfo("Error", "El correo ingresado no es válido.")
            cajaTexto.delete(0, tk.END)

    def cerrarVentanaCorreo():
        """Funcionamiento: Esta función se encarga de cerrar la ventana de correo (ventanaCorreo) y restaurar la ventana principal (ventana) cuando el usuario hace clic en el botón "Volver".
        Entradas:
        No tiene entradas.
        Salidas:
        No tiene salidas.
        """
        ventanaCorreo.destroy()
        ventana.deiconify()

    ventana.withdraw()
    ventanaCorreo = tk.Toplevel(ventana)
    ventanaCorreo.title("Enviar correo")
    ventanaCorreo.geometry("420x205")
    ventanaCorreo.config(bg="lightblue")

    label = tk.Label(ventanaCorreo, text="Ventana para enviar bases de datos por correo.")
    label.config(fg="green", bg="lightgrey", font=("Verdana", 12))
    label.place(x=15, y=10)

    cajaTexto = tk.Entry(ventanaCorreo, width=50)
    cajaTexto.place(x=35, y=80)

    botonVolver = tk.Button(ventanaCorreo, text="Volver",font=("Verdana", 10),bg="red",command=cerrarVentanaCorreo,fg="white")
    botonVolver.place(x=355, y=165)

    botonEnviar = tk.Button(ventanaCorreo, text="Enviar",font=("Verdana", 10),bg="green",fg="white",command=lambda: opcionEnviarCorreo(cajaTexto))
    botonEnviar.place(x=155, y=125)

def opcionBaseDatos():
    """Funcionamiento: Esta función se encarga de crear una base de datos utilizando las variables globales diccEstudiantes y diccMentores. Luego, muestra un mensaje de información que indica que la base de datos se ha creado con éxito.
        Entradas:
            No tiene entradas explícitas, pero utiliza las siguientes variables globales:
            diccEstudiantes: Un diccionario que parece contener información de estudiantes.
            diccMentores: Un diccionario que parece contener información de mentores.
        Salidas:
            No tiene salidas directas, pero muestra un mensaje de éxito mediante messagebox.showinfo.
    """
    global diccEstudiantes
    global diccMentores
    crearBaseDatos(diccEstudiantes, diccMentores)
    messagebox.showinfo("Base de datos creada", "La base de datos se ha creado con éxito.")

def opcionGenerarReportes():
    """Funcionamiento: Esta función es la función principal que se muestra al usuario cuando desea generar reportes. Permite al usuario seleccionar entre tres opciones de generación de reportes: reporte por mentor, reporte por carrera y reporte por sede. Cada opción ejecuta una función específica que genera el informe correspondiente y muestra un mensaje de éxito.
        Entradas:
            No tiene entradas directas, pero utiliza las siguientes variables globales y funciones:
            diccMentores: Un diccionario que parece contener información de mentores.
            diccEstudiantes: Un diccionario que parece contener información de estudiantes.
            estructuraCarrerasCantidad: Una estructura que parece contener información sobre carreras y cantidades.
            inicialesSedes: Una variable que parece contener información sobre iniciales de sedes.
        Salidas:
            No tiene salidas directas, pero muestra mensajes de éxito mediante messagebox.showinfo.
    """

    def opcionReporteMentor():
        """Funcionamiento: Esta función se encarga de generar un informe de mentor utilizando las variables globales diccMentores y diccEstudiantes. Luego, muestra un mensaje de información que indica que el informe se ha generado con éxito.
        Entradas:
            No tiene entradas directas, pero utiliza las variables globales diccMentores y diccEstudiantes.
        Salidas:
            No tiene salidas directas, pero muestra un mensaje de éxito mediante messagebox.showinfo.
        """
        global diccMentores
        global diccEstudiantes
        generarReporteMentor(diccMentores, diccEstudiantes)
        messagebox.showinfo("Reporte generado", "El reporte se ha generado con éxito.")

    def opcionReporteCarrera():
        """Funcionamiento: Esta función permite al usuario seleccionar una carrera específica de un menú desplegable. Luego, genera un informe de esa carrera utilizando las variables globales estructuraCarrerasCantidad y diccEstudiantes. Finalmente, muestra un mensaje de información que indica que el informe se ha generado con éxito.
        Entradas:
            No tiene entradas directas, pero utiliza las variables globales estructuraCarrerasCantidad.
        Salidas:
            No tiene salidas directas, pero muestra un mensaje de éxito mediante messagebox.showinfo.
        """
        def generarReporte(carrera):
            """Funcionamiento: Esta función se encarga de generar un informe específico de una carrera dada. Utiliza las variables globales diccEstudiantes y estructuraCarrerasCantidad para generar el informe de la carrera especificada. Luego, muestra un mensaje de información que indica que el informe se ha generado con éxito y cierra la ventana que permitió la selección de la carrera.
                Entradas:
                    carrera [str]: El nombre de la carrera para la cual se generará el informe.
                Salidas:
                    No tiene salidas directas, pero muestra un mensaje de éxito mediante messagebox.showinfo.
                    Cierra la ventana que se utiliza para seleccionar la carrera (ventanaCarrera).
            """
            global diccEstudiantes
            global estructuraCarrerasCantidad
            generarReporteCarrera(estructuraCarrerasCantidad, diccEstudiantes, carrera)
            messagebox.showinfo("Reporte generado", "El reporte se ha generado con éxito.")
            ventanaCarrera.destroy()

        global estructuraCarrerasCantidad
        carreras = sorted(obtenerCarreras(estructuraCarrerasCantidad))

      
        ventanaCarrera = tk.Toplevel(ventana)
        ventanaCarrera.title("Selección de Carrera")
        ventanaCarrera.geometry("365x455")

        menu_carreras = tk.Menu(ventanaCarrera)

        for carrera in carreras:
            
            menu_carreras.add_command(label=carrera, command=lambda c=carrera: generarReporte(c))

       
        ventanaCarrera.config(menu=menu_carreras)

    def opcionReporteSede():
        """Funcionamiento: Esta función se encarga de generar un informe de sede utilizando las variables globales estructuraCarrerasCantidad, diccEstudiantes y inicialesSedes. Luego, muestra un mensaje de información que indica que el informe se ha generado con éxito.
        Entradas:
            No tiene entradas directas, pero utiliza las variables globales estructuraCarrerasCantidad y inicialesSedes.
        Salidas:
            No tiene salidas directas, pero muestra un mensaje de éxito mediante messagebox.showinfo.
        """
        global diccEstudiantes
        global estructuraCarrerasCantidad
        global inicialesSedes
        generarReporteSede(estructuraCarrerasCantidad, diccEstudiantes, inicialesSedes)
        messagebox.showinfo("Reporte generado", "El reporte se ha generado con éxito.")

    def cerrarVentanaReportes():
        """Funcionamiento: Esta función se encarga de cerrar la ventana de reportes (ventanaReportes) y restaurar la ventana principal (ventana) cuando el usuario hace clic en el botón "Volver".
        Entradas:
            No tiene entradas.
        Salidas:
            No tiene salidas.
        """
        ventanaReportes.destroy()
        ventana.deiconify()

    ventanaReportes= tk.Toplevel(ventana)
    ventanaReportes.title("Ventana para generar reportes.")
    ventanaReportes.geometry("550x300")
    ventanaReportes.config(bg="lightblue")
    ventana.withdraw()

    label = tk.Label(ventanaReportes, text="Aqui puedes generar los reportes.")
    label.config(fg="green", bg="lightgrey", font=("Verdana", 12))
    label.place(x=25, y=10)

    botonVolver = tk.Button(ventanaReportes, text="Volver",font=("Verdana", 10),bg="red",command=cerrarVentanaReportes,fg="white")
    botonVolver.place(x=490, y=265)

    menu = tk.Menu(ventanaReportes)
    opciones = tk.Menu(menu,tearoff=0)
    opciones.add_command(label="Reporte por sede",command=opcionReporteSede)
    opciones.add_command(label="Reporte por carrera",command=opcionReporteCarrera)
    opciones.add_command(label="Reporte por Mentor",command=opcionReporteMentor)


    menu.add_cascade(label="Opciones para generar los reportes.", menu=opciones)
    ventanaReportes.config(menu=menu)

def opcionActualizarEstudiante():
    """Funcionamiento: Esta función se utiliza para habilitar las opciones de actualización de información para estudiantes. Activa un menú desplegable con opciones para actualizar el nombre, los apellidos, el número de teléfono o el correo electrónico de un estudiante.
            Entradas: 
                No tiene entradas.
            Salidas:
                No tiene salidas directas, pero habilita las opciones de actualización en un menú desplegable.
    """
    def actualizarInfo(ventanaActualizarNombre,cajaTexto,seccion):
        """Funcionamiento: Esta función se encarga de actualizar la información de un estudiante o mentor con el carnet dado en función de la sección proporcionada. Puede actualizar el nombre, los apellidos, el número de teléfono o el correo electrónico del estudiante o mentor. Luego de la actualización, cierra la ventana de actualización.
            Entradas:
                ventanaActualizarNombre [tk.Toplevel]: La ventana que se utiliza para ingresar la nueva información.
                cajaTexto [tk.Entry]: La caja de texto donde se ingresa la nueva información.
                seccion [int]: Un valor que representa la sección de información a actualizar (0 para nombre, 1 para primer apellido, 2 para segundo apellido, 3 para teléfono, 4 para correo).
            Salidas:
                No tiene salidas directas, pero actualiza la información del estudiante o mentor en el diccionario diccEstudiantes y cierra la ventana de actualización.
        """
        global carnet
        info=cajaTexto.get()
        if len(info)>0 and seccion>=0 and seccion <=2 :
            if carnet[:4]=="2024":
                nombreCompleto=list(diccEstudiantes[carnet][0])
                if seccion == 0:
                    nombreCompleto[0]=info
                elif seccion == 1:
                    nombreCompleto[1]=info
                elif seccion == 2:
                    nombreCompleto[2]=info
                nombreCompleto=tuple(nombreCompleto)
                diccEstudiantes[carnet][0]=nombreCompleto
            else:
                global sedeMentor
                mentores=diccMentores[sedeMentor]
                for mentor in mentores:
                    if mentor[0]==carnet:
                        nombreCompleto=list(mentor[1])
                        if seccion == 0:
                            nombreCompleto[0]=info
                        elif seccion == 1:
                            nombreCompleto[1]=info
                        elif seccion == 2:
                            nombreCompleto[2]=info
                        nombreCompleto=tuple(nombreCompleto)
                        mentor[1]=nombreCompleto
                        break
            ventanaActualizarNombre.destroy()
        
        elif len(info)>0 and seccion==3:
            global totalNumeros
            try:
                if info.isdigit() and len(info)==8:
                    if int(info) not in totalNumeros:
                        diccEstudiantes[carnet][1]=int(info)
                        ventanaActualizarNombre.destroy()
                    else:
                        messagebox.showerror("Error", "El número ingresado ya existe.")
                        cajaTexto.delete(0,END)
                else:
                    messagebox.showerror("Error", "El número ingresado no tiene el formato correcto.") 
                    cajaTexto.delete(0,END)
            except:
                messagebox.showerror("Error", "El número ingresado no es válido.")  
                cajaTexto.delete(0,END)
        elif len(info)>0 and seccion==4:
            global totalCorreos
            if validarCorreo(info):
                if info not in totalCorreos:
                    diccEstudiantes[carnet][2]=info
                    ventanaActualizarNombre.destroy()
                else:
                    messagebox.showerror("Error", "El correo ingresado ya existe.")
                    cajaTexto.delete(0,END)
            else:
                messagebox.showerror("Error", "El correo ingresado no tiene el formato correcto.")
                cajaTexto.delete(0,END)    
        else:
            messagebox.showerror("Error", "La información ingresada no es válida.")
            cajaTexto.delete(0,END)
        if carnet[:4]=="2024":
                    mostrarInfoEstudiante(carnet)
        else:
            mostrarInfoMentor(carnet)

    def habilitarOpciones():
        """Funcionamiento: Esta función habilita las opciones de actualización en un menú desplegable para que el usuario pueda seleccionar la sección de información que desea actualizar.
            Entradas:
                No tiene entradas.
            Salidas:
                No tiene salidas directas, pero habilita las opciones de actualización en un menú desplegable.
        """
        opciones.entryconfig("Actualizar nombre", state=NORMAL)
        opciones.entryconfig("Actualizar primer apellido", state=NORMAL)
        opciones.entryconfig("Actualizar segundo apellido", state=NORMAL)
        opciones.entryconfig("Actualizar teléfono", state=NORMAL)
        opciones.entryconfig("Actualizar correo", state=NORMAL)

    def opcionActualizarCorreo():
        """Funcionamiento: Esta función muestra una ventana para que el usuario ingrese el nuevo correo a registrar. Luego, llama a la función actualizarInfo con la sección 4 (correo) como parámetro.
            Entradas:
                No tiene entradas.
            Salidas:
                No tiene salidas directas, pero llama a la función actualizarInfo con la sección 4 (correo) como parámetro.
        """
        ventanaActualizarNombre=tk.Toplevel(ventanaActualizarInfo)
        ventanaActualizarNombre.title("Ingresa el nuevo correo a registrar.")
        ventanaActualizarNombre.geometry("400x150")
        ventanaActualizarNombre.config(bg="lightblue")
        cajaTexto = tk.Entry(ventanaActualizarNombre,width=30)
        cajaTexto.place(x=110, y=50)
        botonAceptar = tk.Button(ventanaActualizarNombre, text="Actualizar",font=("Verdana", 10),bg="green",command=lambda:actualizarInfo(ventanaActualizarNombre,cajaTexto,4),fg="white")
        botonAceptar.place(x=150, y=100)

    def opcionActualizarTelefono():
        """Funcionamiento: Esta función muestra una ventana para que el usuario ingrese el nuevo número de teléfono a registrar. Luego, llama a la función actualizarInfo con la sección 3 (teléfono) como parámetro.
            Entradas:
                No tiene entradas.
            Salidas:
                No tiene salidas directas, pero llama a la función actualizarInfo con la sección 3 (teléfono) como parámetro.
        """
        ventanaActualizarNombre=tk.Toplevel(ventanaActualizarInfo)
        ventanaActualizarNombre.title("Ingresa el nuevo número a registrar.")
        ventanaActualizarNombre.geometry("400x150")
        ventanaActualizarNombre.config(bg="lightblue")
        cajaTexto = tk.Entry(ventanaActualizarNombre)
        cajaTexto.place(x=100, y=50)
        botonAceptar = tk.Button(ventanaActualizarNombre, text="Actualizar",font=("Verdana", 10),bg="green",command=lambda:actualizarInfo(ventanaActualizarNombre,cajaTexto,3),fg="white")
        botonAceptar.place(x=150, y=100)

    def opcionActualizarApellido(pos):
        """
        Funcionamiento: Esta función muestra una ventana para que el usuario ingrese el nuevo apellido a registrar (ya sea primer o segundo apellido, dependiendo de la posición). Luego, llama a la función actualizarInfo con la sección 1 o 2 (primer o segundo apellido) como parámetro.
            Entradas:
                pos [int]: Un valor que indica si se debe actualizar el primer o segundo apellido (1 para primer apellido, 2 para segundo apellido).
            Salidas:
                No tiene salidas directas, pero llama a la función actualizarInfo con la sección 1 o 2 (primer o segundo apellido) como parámetro.
        """
        ventanaActualizarNombre=tk.Toplevel(ventanaActualizarInfo)
        ventanaActualizarNombre.title("Ingresa el nuevo apellido a registrar.")
        ventanaActualizarNombre.geometry("400x150")
        ventanaActualizarNombre.config(bg="lightblue")
        cajaTexto = tk.Entry(ventanaActualizarNombre)
        cajaTexto.place(x=100, y=50)
        if pos == 1:
            botonAceptar = tk.Button(ventanaActualizarNombre, text="Actualizar",font=("Verdana", 10),bg="green",command=lambda:actualizarInfo(ventanaActualizarNombre,cajaTexto,1),fg="white")
            botonAceptar.place(x=150, y=100)
        else:
            botonAceptar = tk.Button(ventanaActualizarNombre, text="Actualizar",font=("Verdana", 10),bg="green",command=lambda:actualizarInfo(ventanaActualizarNombre,cajaTexto,2),fg="white")
            botonAceptar.place(x=150, y=100)

    def opcionActualizarNombre():
        """Funcionamiento: Esta función muestra una ventana para que el usuario ingrese el nuevo nombre a registrar. Luego, llama a la función actualizarInfo con la sección 0 (nombre) como parámetro.
            Entradas:
                No tiene entradas.
            Salidas:
                No tiene salidas directas, pero llama a la función actualizarInfo con la sección 0 (nombre) como parámetro.
        """
        ventanaActualizarNombre=tk.Toplevel(ventanaActualizarInfo)
        ventanaActualizarNombre.title("Ingresa el nuevo nombre a registrar.")
        ventanaActualizarNombre.geometry("400x150")
        ventanaActualizarNombre.config(bg="lightblue")
        cajaTexto = tk.Entry(ventanaActualizarNombre)
        cajaTexto.place(x=100, y=50)
        
        botonAceptar = tk.Button(ventanaActualizarNombre, text="Actualizar",font=("Verdana", 10),bg="green",command=lambda:actualizarInfo(ventanaActualizarNombre,cajaTexto,0),fg="white")
        botonAceptar.place(x=150, y=100)

    def mostrarInfoMentor(carnet):
        """Funcionamiento: Esta función muestra la información de un mentor con el carnet dado en la ventana de actualización. La información incluye el nombre, los apellidos, el correo, el tipo (estudiante mentor) y se muestra en etiquetas en la ventana.
            Entradas:
                carnet [str]: El carnet del mentor del cual se mostrará la información.
            Salidas:
                No tiene salidas directas, pero muestra la información del mentor en la ventana de actualización.
        """
        for widget in ventanaActualizarInfo.winfo_children():
            if widget.winfo_class() == 'Label' and widget.cget("text")!="Ventana para actualizar información de los estudiantes.":
                widget.destroy()
        global sedeMentor
        for sede in diccMentores.keys():
                for mentor in diccMentores.get(sede, []):
                    if mentor[0] == carnet:
                        nombre = mentor[1][0]
                        primerApellido = mentor[1][1]
                        segundoApellido = mentor[1][2]
                        correo = mentor[3]
                        tipo= "Estudiante mentor"
                        sedeMentor=sede
                        break 
        
        labelNombre = tk.Label(ventanaActualizarInfo, text=f"Nombre: {nombre}")
        labelNombre.config(fg="green", bg="lightgrey", font=("Verdana", 12))
        labelNombre.place(x=75, y=50)
        labelPrimerApellido = tk.Label(ventanaActualizarInfo, text=f"Primer apellido: {primerApellido}")
        labelPrimerApellido.config(fg="green", bg="lightgrey", font=("Verdana", 12))
        labelPrimerApellido.place(x=75, y=80)
        labelSegundoApellido = tk.Label(ventanaActualizarInfo, text=f"Segundo apellido: {segundoApellido}")
        labelSegundoApellido.config(fg="green", bg="lightgrey", font=("Verdana", 12))
        labelSegundoApellido.place(x=75, y=110)
        labelCorreo = tk.Label(ventanaActualizarInfo, text=f"Correo: {correo}")
        labelCorreo.config(fg="green", bg="lightgrey", font=("Verdana", 12))
        labelCorreo.place(x=75, y=170)
        labelTipo = tk.Label(ventanaActualizarInfo, text=f"Tipo: {tipo}")
        labelTipo.config(fg="green", bg="lightgrey", font=("Verdana", 12))
        labelTipo.place(x=75, y=200)
                                
    def mostrarInfoEstudiante(carnet):
        """Funcionamiento: Esta función muestra la información de un estudiante con el carnet dado en la ventana de actualización. La información incluye el nombre, los apellidos, el teléfono, el correo, el tipo ("Primer ingreso") y se muestra en etiquetas en la ventana.
        Entradas:
            carnet [str]: El carnet del estudiante del cual se mostrará la información.
        Salidas:
            No tiene salidas directas, pero muestra la información del estudiante en la ventana de actualización.
        """       
        for widget in ventanaActualizarInfo.winfo_children():
            if widget.winfo_class() == 'Label' and widget.cget("text")!="Ventana para actualizar información de los estudiantes.":
                widget.destroy()

        informacion = diccEstudiantes.get(carnet, [])
        nombre = informacion[0][0]
        primerApellido = informacion[0][1]
        segundoApellido = informacion[0][2]
        telefono = informacion[1]
        correo = informacion[2]
        tipo = "Primer ingreso"

        labelNombre = tk.Label(ventanaActualizarInfo, text=f"Nombre: {nombre}")
        labelNombre.config(fg="green", bg="lightgrey", font=("Verdana", 12))
        labelNombre.place(x=75, y=50)

        labelPrimerApellido = tk.Label(ventanaActualizarInfo, text=f"Primer apellido: {primerApellido}")
        labelPrimerApellido.config(fg="green", bg="lightgrey", font=("Verdana", 12))
        labelPrimerApellido.place(x=75, y=80)

        labelSegundoApellido = tk.Label(ventanaActualizarInfo, text=f"Segundo apellido: {segundoApellido}")
        labelSegundoApellido.config(fg="green", bg="lightgrey", font=("Verdana", 12))
        labelSegundoApellido.place(x=75, y=110)

        labelTelefono = tk.Label(ventanaActualizarInfo, text=f"Teléfono: {telefono}")
        labelTelefono.config(fg="green", bg="lightgrey", font=("Verdana", 12))
        labelTelefono.place(x=75, y=140)

        labelCorreo = tk.Label(ventanaActualizarInfo, text=f"Correo: {correo}")
        labelCorreo.config(fg="green", bg="lightgrey", font=("Verdana", 12))
        labelCorreo.place(x=75, y=170)

        labelTipo = tk.Label(ventanaActualizarInfo, text=f"Tipo: {tipo}")
        labelTipo.config(fg="green", bg="lightgrey", font=("Verdana", 12))
        labelTipo.place(x=75, y=200)


  
    def obtenerCarnet(buscarEstudiantetxt,cajaTexto):
        """Funcionamiento: Esta función obtiene el número de carnet ingresado por el usuario y verifica si es válido. Luego, llama a las funciones mostrarInfoEstudiante o mostrarInfoMentor según el formato del carnet y si se encuentra registrado. Además, habilita las opciones de actualización y retorna el carnet.
            Entradas:
                buscarEstudiantetxt [tk.Toplevel]: La ventana utilizada para ingresar el número de carnet.
                cajaTexto [tk.Entry]: La caja de texto donde se ingresa el número de carnet.
            Salidas:
                carnet [str]: El número de carnet ingresado y validado. Si es válido, se utiliza para mostrar la información del estudiante o mentor y habilitar las opciones de actualización.
        """
        global carnet
        global totalCarnets
        pcarnet=cajaTexto.get()
        if len(pcarnet)==10:
            if pcarnet in totalCarnets:
                carnet=pcarnet
                if carnet[:4]=="2024":
                    mostrarInfoEstudiante(carnet)
                else:
                    mostrarInfoMentor(carnet)
                buscarEstudiantetxt.destroy()
                habilitarOpciones()
                return carnet
            else:
                messagebox.showerror("Error", "El carnet ingresado no se encuentra registrado.")
                cajaTexto.delete(0,END)
        else:
            messagebox.showerror("Error", "El formato del carnet es incorrecto. Debes al menos 10 valores numéricos.")
            cajaTexto.delete(0,END)

    def buscarEstudiante():
        """Funcionamiento: Esta función muestra una ventana para que el usuario ingrese el número de carnet del estudiante a buscar. Luego, llama a la función obtenerCarnet para obtener y validar el carnet ingresado.
            Entradas:
                No tiene entradas.
            Salidas:
                No tiene salidas directas, pero muestra una ventana para ingresar el número de carnet y llama a obtenerCarnet para validar y obtener el carnet.
        """
        buscarEstudiantetxt=tk.Toplevel(ventanaActualizarInfo)
        buscarEstudiantetxt.title("Ingrese el número de carnet del estudiante a buscar.")
        buscarEstudiantetxt.geometry("400x150")
        buscarEstudiantetxt.config(bg="lightblue")
        cajaTexto = tk.Entry(buscarEstudiantetxt)
        cajaTexto.place(x=100, y=50)
        
        botonAceptar = tk.Button(buscarEstudiantetxt, text="Buscar",font=("Verdana", 10),bg="green",command=lambda:obtenerCarnet(buscarEstudiantetxt,cajaTexto),fg="white")
        botonAceptar.place(x=150, y=100)

    def cerrarVentanaActualizarInfo():
        """Funcionamiento: Esta función se encarga de cerrar la ventana de actualización de información (ventanaActualizarInfo) y restaurar la ventana principal (ventana) cuando el usuario hace clic en el botón "Volver".
            Entradas:
                No tiene entradas.
            Salidas:
                No tiene salidas.
        """
        ventanaActualizarInfo.destroy()
        ventana.deiconify()
    


    ventanaActualizarInfo = tk.Toplevel(ventana)
    ventanaActualizarInfo.title("Ventana de actualización de información.")
    ventanaActualizarInfo.geometry("550x300")
    ventanaActualizarInfo.config(bg="lightblue")
    ventana.withdraw()

    #Texto en la ventana
    label = tk.Label(ventanaActualizarInfo, text="Ventana para actualizar información de los estudiantes.")
    label.config(fg="green", bg="lightgrey", font=("Verdana", 12))
    label.place(x=25, y=10)

    #Botones
    botonVolver = tk.Button(ventanaActualizarInfo, text="Volver",font=("Verdana", 10),bg="red",command=cerrarVentanaActualizarInfo,fg="white")
    botonVolver.place(x=490, y=265)

    #Menu desplegable
    menu = tk.Menu(ventanaActualizarInfo)
    opciones = tk.Menu(menu,tearoff=0)
    opciones.add_command(label="Buscar estudiante",command=buscarEstudiante)
    opciones.add_command(label="Actualizar nombre",command=opcionActualizarNombre,state=DISABLED)
    opciones.add_command(label="Actualizar primer apellido",command=lambda:opcionActualizarApellido(1),state=DISABLED)
    opciones.add_command(label="Actualizar segundo apellido",command=lambda:opcionActualizarApellido(2),state=DISABLED)
    opciones.add_command(label="Actualizar teléfono",command=opcionActualizarTelefono,state=DISABLED)
    opciones.add_command(label="Actualizar correo",command=opcionActualizarCorreo,state=DISABLED)


    menu.add_cascade(label="Opciones para actualizar información", menu=opciones)
    ventanaActualizarInfo.config(menu=menu)    

def opcionAsignarMentores():
    """Funcionamiento: Esta función se encarga de asignar mentores a los estudiantes y actualizar el diccionario diccEstudiantes con esta asignación. Luego, retorna el diccionario actualizado.
        Entradas: 
            No tiene entradas.
        Salidas:
            diccEstudiantes [dict]: El diccionario actualizado de estudiantes con la asignación de mentores.
    """
    global diccEstudiantes
    global diccMentores
    global estructuraCarrerasCantidad
    diccEstudiantes=asignarMentores(diccEstudiantes,diccMentores,estructuraCarrerasCantidad)
    return diccEstudiantes

def crearMentores():
    """Funcionamiento: Esta función se utiliza para crear la interfaz de usuario de la pestaña de mentores. Muestra la información de los mentores por sede en una ventana gráfica.
        Entradas: 
            No tiene entradas.
        Salidas: 
            No tiene salidas directas, pero crea la interfaz de usuario para mostrar la información de los mentores por sede.
    """    
    def mostrarInfo(diccMentores):
        """Funcionamiento: Esta función se encarga de mostrar la información de los mentores en la ventana gráfica de la pestaña de mentores. Borra la información anterior y muestra la información actualizada de los mentores por sede.
        Entradas:
            diccMentores [dict]: El diccionario que contiene la información de los mentores por sede.
        Salidas: 
            No tiene salidas directas, pero muestra la información de los mentores en la ventana gráfica.
        """
        for i in range(1, 6):
            for j in range(1, 2):
                matrizLabel[i][j].destroy()
                
        sedes = diccMentores.keys()
        
        for i, sede in enumerate(sedes, start=1):
            for j in range(1, 2):
                contenido = "\n".join([f"{sede[0]}: {sede[1:]}" for sede in diccMentores.get(sede, [])])

                text = tk.Text(ventanaMentores, width=130 if j == 1 else 10, height=4, relief="solid")
                text.grid(column=j, row=i)
                text.place(x=51 + (j * 75), y=46 + (i * 70))
                text.insert("1.0", contenido)
                text.tag_configure("center", justify="center")
                text.tag_add("center", "1.0", "end")
                text.config(state="disabled")
                matrizLabel[i][j] = text
        return 
    
    def cerrarVentanaMentores():
        """Funcionamiento: Esta función se encarga de cerrar la ventana de la pestaña de mentores y restaurar la ventana principal cuando el usuario hace clic en el botón "Volver".
            Entradas: 
                No tiene entradas.
            Salidas: 
                No tiene salidas directas, pero cierra la ventana de la pestaña de mentores y restaura la ventana principal.
        """
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

    global diccMentores
    global totalCarnets
    global totalCorreos
    global estructuraCarrerasCantidad
    global codigosSedes

    diccMentores,totalCarnetsFun,totalCorreosFun=generarCarnetsMentores(estructuraCarrerasCantidad,codigosSedes,totalCarnets,totalCorreos,diccMentores)
    totalCarnets.append(totalCarnetsFun)
    totalCorreos.append(totalCorreosFun)
    diccionarioVacio={(0,0):"Sede", (0,1):"Información de mentores", (1,0):"CTLSC", (2,0):"CTLSJ", (3,0):"CAL", (4,0):"CTCC", (5,0):"CAA"}
    
    for i in range(6):       
        for j in range(2):
            info=diccionarioVacio.get((i,j),"")
            label = tk.Label(ventanaMentores,width=148 if j == 1 else 10,height=4,relief="solid",anchor=CENTER)
            label.grid(column=j, row=i)
            label.place(x=50+(j*75), y=45+(i*69))
            matrizLabel[i][j]=label
            matrizLabel[i][j].config(text=info)

    mostrarInfo(diccMentores)
  
def estudiantesCarreraPorSede():
    """Funcionamiento: Esta función se encarga de generar e insertar la información de los estudiantes admitidos por carrera y sede en el diccionario diccEstudiantes. Además, muestra un mensaje de información al usuario y retorna el diccionario actualizado.
        Entradas: 
            No tiene entradas.
        Salidas:
            diccEstudiantes [dict]: El diccionario actualizado de estudiantes por carrera y sede.
    """
    global diccEstudiantes
    global totalCarnets
    global totalNumeros
    global totalCorreos
    global estructuraCarrerasCantidad

    diccEstudiantes={}
    diccEstudiantes,totalCarnetsSec,totalNumerosSec,totalCorreosSec=generarCarnetsEstudiantes(totalAdmitidos, estructuraCarrerasCantidad,codigosSedes,totalCarnets,totalNumeros,totalCorreos,diccEstudiantes)
    totalCarnets.append(totalCarnetsSec)
    totalNumeros.append(totalNumerosSec)
    totalCorreos.append(totalCorreosSec)
    messagebox.showinfo("Información","Se han insertado satisfactoriamente la información de cada estudiantes admitido")
    return diccEstudiantes

def crearEstructuraEstudiantesCarreraSede():
    """Funcionamiento: Esta función crea una estructura de datos que representa la cantidad de estudiantes admitidos por carrera y sede. Inicializa una estructura de diccionario que contiene listas de carreras por sede, inicialmente con 0 estudiantes admitidos en cada una.
        Entradas: 
            No tiene entradas.
        Salidas:
            estructuraAdmitidosCarrera [dict]: La estructura de datos que contiene la cantidad de estudiantes admitidos por carrera y sede.
    """
    info=obtenerSedesCarreras(inicialesSedes)
    estructuraAdmitidosCarrera={}
    for sede in info.keys():
        listaAdmitidosCarrera=[]
        for carrera in info[sede]:
            listaAdmitidosCarrera.append([carrera,0])
        estructuraAdmitidosCarrera[sede]=listaAdmitidosCarrera
    
    return estructuraAdmitidosCarrera

def estudiantesPorSede():
    """Funcionamiento: Esta función se encarga de distribuir la cantidad de estudiantes admitidos en cada sede y carrera según una lógica específica. Luego, actualiza la información en una matriz y la muestra en una ventana gráfica.
        Entradas: 
            No tiene entradas.
        Salidas: 
            No tiene salidas directas, pero distribuye y muestra la información de estudiantes admitidos en la ventana gráfica.
    """
    
    def distribuirAdmitidos(totalAdmitidos, estructuraCarrerasCantidad):
        """
        Funcionamiento: Esta función distribuye la cantidad de estudiantes admitidos en cada sede y carrera según una lógica específica, teniendo en cuenta la cantidad total de cupos.
        Entradas:
            totalAdmitidos [dict]: Un diccionario que contiene la cantidad total de estudiantes admitidos por sede.
            estructuraCarrerasCantidad [dict]: Una estructura de datos que representa la cantidad de estudiantes admitidos por carrera y sede.
        Salidas:
            estructuraCarrerasCantidad [dict]: La estructura actualizada de la cantidad de estudiantes admitidos por carrera y sede.
        """
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
        """Funcionamiento: Esta función se encarga de actualizar y mostrar la información de estudiantes admitidos en la ventana gráfica.
        Entradas: 
            No tiene entradas.
        Salidas: 
            No tiene salidas directas, pero actualiza y muestra la información en la ventana gráfica.
        """
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
    """Funcionamiento: Esta función se encarga de habilitar las opciones en un entorno gráfico. En particular, habilita una serie de botones con las opciones disponibles para el usuario.
        Entradas: 
            No tiene entradas.
        Salidas: 
            No tiene salidas directas, pero habilita los botones para permitir al usuario realizar diversas acciones en el entorno gráfico.
    """
    boton2.config(state=tk.NORMAL)
    boton3.config(state=tk.NORMAL)
    boton4.config(state=tk.NORMAL)
    boton5.config(state=tk.NORMAL)
    boton6.config(state=tk.NORMAL)
    boton7.config(state=tk.NORMAL)
    boton8.config(state=tk.NORMAL)


#Programa principal
ventana.title("Atención a la generación de 2024.")
ventana.geometry("550x300")
ventana.config(bg="lightblue")

label = tk.Label(ventana, text="Bienvenid@ a la aplicación de atención a la generación 2024.")
label.config(fg="green", bg="lightgrey", font=("Verdana", 12))
label.place(x=25, y=10)

boton1 = tk.Button(ventana, text="Estudiantes por sede",font=("Verdana", 10),command=estudiantesPorSede)
boton2 = tk.Button(ventana, text="Estudiantes de carrera por sede",font=("Verdana", 10),state="disabled",command=estudiantesCarreraPorSede)
boton3 = tk.Button(ventana, text="Crear mentores",font=("Verdana", 10),state="disabled",command=crearMentores)
boton4 = tk.Button(ventana, text="Asignar mentores",font=("Verdana", 10),state="disabled",command=opcionAsignarMentores)
boton5 = tk.Button(ventana, text="Actualizar estudiante",font=("Verdana", 10),command=opcionActualizarEstudiante,state="disabled")
boton6 = tk.Button(ventana, text="Generar reportes",font=("Verdana", 10),command=opcionGenerarReportes,state="disabled")
boton7 = tk.Button(ventana, text="Crear base de datos en Excel",font=("Verdana", 10),command=opcionBaseDatos,state="disabled")
boton8 = tk.Button(ventana, text="Enviar correo",font=("Verdana", 10),command=opcionEnviarCorreo,state="disabled")
boton9 = tk.Button(ventana, text="Salir",font=("Verdana", 10),bg="red",command=ventana.destroy,fg="white")


boton1.place(x=85, y=50)
boton2.place(x=45, y=95)
boton3.place(x=90, y=140)
boton4.place(x=85, y=185)
boton5.place(x=325, y=50)
boton6.place(x=335, y=95)
boton7.place(x=305, y=140)
boton8.place(x=335, y=185)
boton9.place(x=475, y=260)

estructuraCarrerasCantidad=crearEstructuraEstudiantesCarreraSede()
ventana.mainloop()


