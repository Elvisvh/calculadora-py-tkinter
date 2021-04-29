def Calcular(num, etiqueta):
    if num==-1:
        etiqueta.delete(0,'end')
    elif num == -2:
        calculo = eval(etiqueta.get())
        etiqueta.delete(0, 'end')
        etiqueta.insert(0, calculo)
    else:
        etiqueta.insert('end', num)

