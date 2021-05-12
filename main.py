from pytube import YouTube
from tkinter import *

# yt = YouTube('https://www.youtube.com/watch?v=9T6PXX7X2ro')
# print(yt.title)
# print(yt.thumbnail_url)

main = Tk()

class Funcionalidades():
    def baixar(self):
        yt = YouTube(self.entry.get())
        self.alert['text'] = (yt.title + ' - Baixado')
        yt.streams.first().download()


class Aplicacao(Funcionalidades):
    def __init__(self):
        self.main = main
        self.Telas()
        self.Frame()
        self.wigts()
        main.mainloop()

    def Telas(self):
        self.main.title('Download video MP3')
        self.main.configure(background='black')
        self.main.geometry('572x318')
        self.main.resizable(False, False)

    def Frame(self):
        self.principal = Frame(self.main, bg='white')
        self.principal.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

    def wigts(self):
        Label(self.principal, text='Link for video', bg='white',font="impact 15 bold").place(relx=0.01, rely=0.15)
        self.entry=Entry(self.principal)
        self.entry.place(relx=0.25,rely=0.15,relwidth=0.65,relheight=0.10)
        self.alert=Label(self.principal,text='',bg='white')
        self.alert.place(relx=0.25, rely=0.30)
        Button(self.principal, text='Baixar', bg='green',font="impact 15",command=self.baixar).place(relx=0.45, rely=0.60)
Aplicacao()
