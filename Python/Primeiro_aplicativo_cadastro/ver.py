from tkinter import*
from cadastro import *

def ver():
    jan_ver = Tk()
    jan_ver.geometry('500x500')
    jan_ver.config(background='#00BFFF', padx=10, pady=10)
    jan_ver.title('Lista de Alunos')
    jan_ver.iconbitmap(bitmap=r'Python\Primeiro_aplicativo_cadastro\tech.ico')

    info = Label(master=jan_ver, text='Abaixo os alunos cadastrados',background='#00BFFF', foreground='black', pady=10).grid(row=0, column=0)

    espac1 = Label(master=jan_ver, background='#00BFFF').grid(row=1, column=0)

    def obter_caminho(): #obtenho o caminho genérico
        diretorio = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(diretorio,'cadastro.txt')
    
    caminho = obter_caminho()

    with open(caminho) as arquivo:
        conteudo = arquivo.read()

    def fechar():
        jan_ver.destroy()

    leitura = Text(master=jan_ver, width=60, height=20, wrap='word')
    leitura.grid(row=2, column=0)
    leitura.insert(END, conteudo)
    leitura.config(state='disabled')

    espac2 = Label(master=jan_ver, background='#00BFFF').grid(row=3, column=0)


    sair = Button(master=jan_ver, text='Sair', padx=35, pady=20, command=fechar).grid(row=4, column=0)

    jan_ver.mainloop()