from tkinter import *
class FileMenu:
    """Класс, который инкапсулирует в себе
        работу menu  наверху программы"""
    def __init__(self, __root,__newFile,__openFile, __saveFile):
        self.__root = __root
        __thisMenuBar = Menu(self.__root)
        __thisFileMenu = Menu(__thisMenuBar)
        __thisEditMenu = Menu(__thisMenuBar,tearoff=0)
        __thisFileMenu.add_command(label="Новый",command=__newFile)
        __thisFileMenu.add_command(label="Открыть",command=__openFile)
        __thisFileMenu.add_command(label="Сохранить",command=__saveFile)
        __thisFileMenu.add_separator()
        __thisMenuBar.add_cascade(label="MainFile",menu=__thisFileMenu)
        __thisMenuBar.add_cascade(label="Edit",menu=__thisEditMenu)
