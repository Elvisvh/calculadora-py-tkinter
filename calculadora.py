import tkinter as tk
from lib import func as fc

ventana = tk.Tk() #se crea la ventana
ventana.geometry("250x300")
ventana.title("Calculadora")


#para crear una etiqueta en pantalla
etiqueta = tk.Entry(ventana)
#etiqueta.pack() #podemos usar side para poder ubicar la etiqueta
#.pack(side=tk.right)
etiqueta.grid(row = 0, column = 0, columnspan = 4, padx =5, pady = 5)



boton1 = tk.Button(ventana, text = "1", width = 2, heigh = 2, command = lambda: fc.Calcular(1,etiqueta))
boton2 = tk.Button(ventana, text = "2", width = 2, heigh = 2, command = lambda: fc.Calcular(2,etiqueta))
boton3 = tk.Button(ventana, text = "3", width = 2, heigh = 2, command = lambda: fc.Calcular(3,etiqueta))
boton4 = tk.Button(ventana, text = "4", width = 2, heigh = 2, command = lambda: fc.Calcular(4,etiqueta))
boton5 = tk.Button(ventana, text = "5", width = 2, heigh = 2, command = lambda: fc.Calcular(5,etiqueta))
boton6 = tk.Button(ventana, text = "6", width = 2, heigh = 2, command = lambda: fc.Calcular(6,etiqueta))
boton7 = tk.Button(ventana, text = "7", width = 2, heigh = 2, command = lambda: fc.Calcular(7,etiqueta))
boton8 = tk.Button(ventana, text = "8", width = 2, heigh = 2, command = lambda: fc.Calcular(8,etiqueta))
boton9 = tk.Button(ventana, text = "9", width = 2, heigh = 2, command = lambda: fc.Calcular(9,etiqueta))
boton0 = tk.Button(ventana, text = "0", width = 2, heigh = 2, command = lambda: fc.Calcular(0,etiqueta))
boton_punto = tk.Button(ventana, text = ".", width = 2, heigh = 2, command = lambda: fc.Calcular(".",etiqueta))
boton_menos = tk.Button(ventana, text = "C", width = 2, heigh = 2, command = lambda: fc.Calcular(-1,etiqueta))

boton1.grid(row = 4, column = 0) #primera fila
boton2.grid(row = 4, column = 1) #segunda fila
boton3.grid(row = 4, column = 2) #tercera fila
boton4.grid(row = 3, column = 0) #primera fila
boton5.grid(row = 3, column = 1) #segunda fila
boton6.grid(row = 3, column = 2) #tercera fila
boton7.grid(row = 2, column = 0) #primera fila
boton8.grid(row = 2, column = 1) #segunda fila
boton9.grid(row = 2, column = 2) #tercera fila
boton0.grid(row = 5, column = 1)
boton_punto.grid(row = 5, column = 2)
boton_menos.grid(row = 5, column = 0)


#operadores
dividir = tk.Button(ventana, text = "+", width = 2, heigh = 2, command=lambda: fc.Calcular("/",etiqueta))
multiplicar = tk.Button(ventana, text="*", width= 2, heigh = 2, command=lambda: fc.Calcular("*",etiqueta))
restar = tk.Button(ventana, text="-", width = 2, heigh = 2, command=lambda: fc.Calcular("-",etiqueta))
sumar = tk.Button(ventana, text = "+", width = 2, heigh = 2, command=lambda: fc.Calcular("+",etiqueta))
boton_igual = tk.Button(ventana, text = "=", width = 16, heigh = 1, command=lambda: fc.Calcular(-2,etiqueta))


dividir.grid(row = 2, column = 3)
multiplicar.grid(row = 3, column = 3)
restar.grid(row = 4, column = 3)
sumar.grid(row = 5, column = 3)
boton_igual.grid(row = 6, column = 0, columnspan = 4, pady = 4)


ventana.mainloop() #lleva el registro de la ventana