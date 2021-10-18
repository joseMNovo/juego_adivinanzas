import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
from warnings import showwarning




ventana = tk.Tk()


numero_correcto = str(random.randint(1, 8))
print(f"Número correcto: {numero_correcto}")
intentos = 0

caja = ttk.Entry()

########################################
# Etiquetas dinamicas

e_primer_aviso = tk.Label(text = "Primer intento", font = ("Arial", 15), fg = "red")
e_segundo_aviso = tk.Label(text = "Segundo intento", font = ("Arial", 15), fg = "red")
e_tercer_aviso = tk.Label(text = "Tercer intento", font = ("Arial", 15), fg = "red")
e_cuarto_aviso = tk.Label(text = "Ultimo intento", font = ("Arial", 15), fg = "red")
e_perdiste = tk.Label(text = "¡Perdiste!", font = ("Arial", 25), fg = "red")
e_ganaste = tk.Label(text = "¡Acertaste!", font = ("Arial", 25), fg = "green")
e_pista_par = tk.Label(text = "¡Numero par!", font = ("Arial", 10), fg = "blue")
e_pista_impar = tk.Label(text = "¡Numero impar!", font = ("Arial", 10), fg = "blue")


########################################
# Funciones

def borrar_pista_impar():
    if e_pista_impar:
        e_pista_impar.place_forget()


def borrar_pista_par():
    if e_pista_par:
        e_pista_par.place_forget()


def dar_pista():

    if numero_correcto == "1" or numero_correcto == "3" or numero_correcto == "5" or numero_correcto == "7":
        e_pista_impar.place(x = 5, y = 30)
        ventana.after(1100, borrar_pista_impar)
        
    elif numero_correcto == "2" or numero_correcto == "4" or numero_correcto == "6" or numero_correcto == "8":
        e_pista_par.place(x = 5, y = 30)
        ventana.after(1100, borrar_pista_par)
        

def borrar_etiquetas_dinamicas():
    e_primer_aviso.place_forget()
    e_segundo_aviso.place_forget()
    e_tercer_aviso.place_forget()
    e_cuarto_aviso.place_forget()
    e_perdiste.place_forget()


def programa_principal():
    global caja
    global numero_correcto
    global intentos

    print(numero_correcto)


    while intentos < 5:
        interior_caja = caja.get()

        if interior_caja != numero_correcto:
            print(f"Interior caja: {interior_caja}")
            #print("Incorrecto")
            intentos += 1
            caja.delete(0, tk.END)

            if intentos == 1:
                e_primer_aviso.place (x = 250, y = 60)
            elif intentos == 2:
                e_segundo_aviso.place (x = 250, y = 100)
            elif intentos == 3:
                e_tercer_aviso.place (x = 250, y = 140)
            elif intentos == 4:
                e_cuarto_aviso.place (x = 250, y = 180)
                      

            print(f"Intento numero: {intentos}")

            if intentos == 5:
                # Etiqueta
                e_perdiste.place(x= 130, y = 210)

                # Pregunta
                respuesta_perdida = messagebox.askyesno(title = "¡Juego terminado!", message="¿Desea volver a jugar?")

                if respuesta_perdida:
                    borrar_etiquetas_dinamicas()
                    e_ganaste.place_forget()
                    numero_correcto = str(random.randint(1, 8))
                    print(f"Nuevo número correcto: {numero_correcto}")
                    
                    caja.delete(0, tk.END)
                    intentos = -1
                else:
                    messagebox.showinfo(message="Gracias por usar el programa")
                    return quit()
            else:
                break

        elif interior_caja == numero_correcto:
            print(f"Interior caja: {interior_caja}")

            # Etiqueta
            e_ganaste.place(x= 125, y = 210)

            # Pregunta
            respuesta_ganada = messagebox.askyesno(title="¡Ganaste!", message="¿Desea volver a jugar?")

            if respuesta_ganada:
                borrar_etiquetas_dinamicas()
                e_ganaste.place_forget()
                numero_correcto = str(random.randint(1, 8))
                print(f"Nuevo número correcto: {numero_correcto}")

                caja.delete(0, tk.END)
                intentos = 0
                
            else:
                messagebox.showinfo(message="Gracias por usar el programa")
                return quit()
            break 
    return

    


def uno():
    global caja
    global numero_correcto
    global intentos
    caja.insert(tk.END, 1)
    
    
    programa_principal()
        


def dos():
    global caja
    global numero_correcto
    global intentos
    caja.insert(tk.END, 2)

    programa_principal()

        

def tres():
    global caja
    global numero_correcto
    global intentos
    caja.insert(tk.END, 3)

    programa_principal()
        

def cuatro():
    global caja
    global numero_correcto
    global intentos
    caja.insert(tk.END, 4)

    programa_principal()
        

def cinco():
    global caja
    global numero_correcto
    global intentos
    caja.insert(tk.END, 5)

    programa_principal()
        

def seis():
    global caja
    global numero_correcto
    global intentos
    caja.insert(tk.END, 6)

    programa_principal()
        

def siete():
    global caja
    global numero_correcto
    global intentos
    caja.insert(tk.END, 7)

    programa_principal()
        

def ocho():
    global caja
    global numero_correcto
    global intentos
    caja.insert(tk.END, 8)

    programa_principal()
    


########################################
# Ventana 
ventana.config (width = 410, height = 360)
ventana.title ("Juego adivinanza")



########################################
# Etiquetas
e_titulo = tk.Label(text = "---------- Adiviná el número ----------", font = ("Arial", 15 ))
e_titulo.place (x = 50, y = 5)

e_titulo2 = tk.Label(text = "(Tenes cinco intentos)", font = ("Arial", 10))
e_titulo2.place (x = 135, y = 30)

e_signo_pregunta = tk.Label(text = "¿?", font = ("Arial", 80))
e_signo_pregunta.place(x = 30, y = 70)

e_signo_igual = tk.Label(text = "=", font = ("Arial", 20))
e_signo_igual.place(x = 200, y = 115)

e_division = tk.Label(text = "-------------------------------------------------------------------------------")
e_division.place (x = 1, y = 250)



########################################
#  Botones
b_uno = ttk.Button(text = "1", command = uno)
b_uno.place(x = 30, y = 280)

b_dos = ttk.Button(text = "2", command = dos)
b_dos.place(x = 120, y = 280)

b_tres = ttk.Button(text = "3", command = tres)
b_tres.place(x = 210, y = 280)

b_cuatro = ttk.Button(text = "4", command = cuatro)
b_cuatro.place(x = 300, y = 280)

b_cinco = ttk.Button(text = "5", command = cinco)
b_cinco.place(x = 30, y = 320)

b_seis = ttk.Button(text = "6", command = seis)
b_seis.place(x = 120, y = 320)

b_siete = ttk.Button(text = "7", command = siete)
b_siete.place(x = 210, y = 320)

b_ocho = ttk.Button(text = "8", command = ocho)
b_ocho.place(x = 300, y = 320)

b_pista = ttk.Button(text = "Pista", width = 4, command = dar_pista)
b_pista.place(x = 2, y = 2)



ventana.mainloop()