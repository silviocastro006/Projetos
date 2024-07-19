from tkinter import *

def verificar(janela,entrada,resultado):
    number = entrada.get()
    entrada.delete(0, END)
    if number == '':
        pass
    else:
        if isinstance(number,str):
            number = number.upper()
        try:
            int_number = int(number)
            resultado.config(text=f'{int_number} é do tipo inteiro')
        except:
            try:
                float_number =float(number)
                resultado.config(text=f'{float_number} é do tipo real')
            except:
                try:
                    if number == 'FALSE':
                        bool_number = False
                    elif number == 'TRUE':
                        bool_number = True
                    resultado.config(text=f'{bool_number} é do tipo booleano')
                except:
                    resultado.config(text=f'Não foi possível converter pois {number} é do tipo {type(number)}')
        janela.geometry('400x250')
        resultado.pack(side='bottom')

# o isinstance não funciona para inputs de tipo string, ele sempre vai ser string

def verifica_2(janela, entrada, resultado):
    numero = entrada.get()
    entrada.delete(0,END)
    if isinstance(numero, int):
        resultado.config(text=f'{numero} é do tipo inteiro')
    elif isinstance(numero, float):
        resultado.config(text=f'{numero} é do tipo real')
    elif isinstance(numero, bool):
        resultado.config(text=f'{numero} é do tipo booleano')
    else:
        resultado.config(text=f'Não foi possível converter pois {numero} é do tipo {type(numero)}')
    janela.geometry('400x250')
    resultado.pack(side='bottom')

