
# -*- coding: utf-8 -*-
import tkinter
import os
from tkinter import *
from tkinter.messagebox import * # нужен для беседы типа, хочешь закрыть? А не так быстро
from tkinter.filedialog import * # для возможностей сохранения файлов
from FileMenu import FileMenu

class Notepad:
    """ Главный класс, в котором у нас собираются остальные классы """
    __root = Tk() 

    #default window width and height
    __thisWidth = 300  # ширина окна
    __thisHeight = 300  # высота окна
    __thisTextArea = Text(__root, font=("Verdana", 24, 'bold')) 
    # __thisHelpMenu = Menu(__thisMenuBar) #tearoff allows you to detach menus for the main window creating floating menus.
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None 

    def __init__(self,**kwargs):
        #инициализация
        #set window size (the default is 300x300)
        self.__thisWidth = kwargs['width'] #принимаем аргумент размера, который выдается на запуске
        self.__thisHeight = kwargs['height']          # устанавливаем заголовок окна
        self.__root.title("Untitled - Notepad")
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, 0, 0))
        # чтобы наше окно могло растягиваться
        self.__root.grid_rowconfigure(0,weight=1)
        self.__root.grid_columnconfigure(0,weight=1)
        self.__thisTextArea.grid(sticky=N+E+S+W)
        self.__root.config(menu=FileMenu(self.__root, self.__newFile, self.__openFile, self.__saveFile))
        self.__thisScrollBar.pack(side=RIGHT,fill=Y)
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)


    def __openFile(self):
        
        self.__file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if self.__file == "":
            self.__file = None 
        else:
            self.__root.title(os.path.basename(self.__file) + " - Notepad")             # устанавливаем заголовок кона
            self.__thisTextArea.delete(1.0,END)
            file = open(self.__file,"r")
            self.__thisTextArea.insert(1.0,file.read())
            file.close()

    def __newFile(self):
        self.__root.title("Безымянный - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0,END)

    def __saveFile(self):

        if self.__file == None:
            #save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

            if self.__file == "":
                self.__file = None
            else:
                file = open(self.__file,"w") # пытаемся сохранить файл
                file.write(self.__thisTextArea.get(1.0,END))
                file.close()
                self.__root.title(os.path.basename(self.__file) + " - Notepad")# изменяем title
        else:
            file = open(self.__file,"w")
            file.write(self.__thisTextArea.get(1.0,END))
            file.close()

    def run(self):
        # запускаем наше приложение
        self.__root.mainloop()

# запуск приложения
notepad = Notepad(width=600,height=400)
notepad.run()


