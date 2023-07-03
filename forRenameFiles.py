from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import font
from tkinter.messagebox import showerror, showwarning, showinfo
import os
import pygame


forbidden_dir = ("C:/", "D:/")


class Errors:
    def __init__(self, name, addinfo):
        self.name = name
        self.addinfo = addinfo

    def show(self):
        return (f'Error {self.name}. {self.addinfo}. Try again!')

    def show1(self):
        return ("{}{}".format(self.name, self.addinfo))


Error100 = Errors('100', 'You forgot indicate the directory of needed files')
Error101 = Errors('101', 'You forgot insert name of files')
Error102 = Errors('102', 'You select forbidden folder')
ErrorElvin = Errors('Aboba', 'Hello from shlyuxa Elvin <3')
Success = Errors('Brilliant! ', 'Program completed successfully')


def OpenWindow():
    window = Tk()
    window.title('Rename Files by the order of the Eyyub, fucking, Yaqubov')

    def browse_dir():
        dir_for_rename = filedialog.askdirectory()
        field_fordir.insert(0, dir_for_rename)

    # Searching of Errors and show they types in messegebox

    def finderror():
        if field_fordir.get() == "":
            return (Error100.show(), False)
        if field_forname.get() == "":
            return (Error101.show(), False)
        if field_fordir.get() in forbidden_dir:
            return (Error102.show(), False)
        if field_forname.get().lower() == "elvin" or field_forname.get().lower() == "emin gey":
            return (ErrorElvin.show(), False)
        else:
            return (Success.show1(), True)

    def start():
        if finderror()[1] == False:
            showerror(message=finderror()[0], title='Error')
            return 0
        else:
            if renamefiles(str(field_forname.get()), field_foraddext.get(), field_fordir.get()) != 0:
                showinfo(message=finderror()[0], title='Success')
    
    # dictionary of songs
    masterpiece = {
        'Kim bilir': "Eyyub Yaqubov  - Kim Bilir.mp3",
        "Sovetski": "Eyyub Yaqubov - Sovetski.mp3",
        "Bakılı Balası": "Eyyub Yaqubov - Bakılı Balası.mp3",
        "Emin qey": "Eyyub Yaqubov - Доля Воровская.mp3",
        "Bayıl": "Eyyub Yaqubov- Bayıl.mp3",
        "Серый Попугай": "Eyyub Yaqubov - Серый Попугай.mp3",
        "Kişidi Bu Remix": "Eyyub Yaqubov -   Kişidi Bu Remix.mp3",
        "Самолёт Баку-Москва": "Brandon Stone  Eyyub Yaqubov -  Самолет БакуМосква.mp3"
    }

    masterpiece_keys = list()

    #keys of dictionary
    for key in masterpiece:
        masterpiece_keys.append(key)

    # Main settings for window
    window.geometry('500x500')
    window.resizable(width=False, height=False)

    # First row, For Browse files
    field_fordir = Entry(width=60)
    field_fordir.place(x=10, y=12, height=22)
    btn_browse = ttk.Button(text='Browse', command=browse_dir)
    btn_browse.place(x=400, y=10)

    # Second row, for file name
    label_for_name = Label(text='Name for files:', font=('Arial', 14))
    label_for_name.place(x=10, y=45)
    field_forname = Entry(width=30)
    field_forname.place(x=140, y=50, height=22)

    # Third row, for enter additional extensions
    label_for_addext = Label(
        text='Additional extensions:', font=('Arial', 14))
    label_for_addext.place(x=10, y=80)
    field_foraddext = Entry(width=45)
    addext = list(field_foraddext.get().split())
    field_foraddext.place(x=200, y=85, height=22)

    # First note for addext
    font_for_note = font.Font(family='Arial', size=10, slant='italic')
    label_for_note = Label(
        text='Note: Enter extensions separated by a space', font=font_for_note, fg='red')
    label_for_note.place(x=90, y=105)

    # Second note for whole app
    font_for_note2 = font.Font(family='Arial', size=15, weight='bold')
    label_for_note2 = Label(
        text='CHECK IF THE SELECTED FOLDER IS CORRECT!', fg='#DB1523', font=font_for_note2)
    label_for_note2.place(x=15, y=140)

    #it's not just music, it's a Baku chansons!
    masterpiece_var = StringVar(value= masterpiece_keys[0])
    combobox = ttk.Combobox(window, textvariable=masterpiece_var)
    combobox['state'] = 'readonly'
    combobox["values"] = masterpiece_keys

    #initial music
    pygame.init()
    pygame.mixer.music.load("Eyyub Yaqubov  - Kim Bilir.mp3")
    pygame.mixer.music.play()

    def playSound(event):
        value = combobox.get()
        pygame.mixer.music.load(masterpiece.get(value))
        pygame.mixer.music.play() 

    combobox.bind("<<ComboboxSelected>>", playSound)

    label_music = Label(
        text="Choose your Eyyub's favourite!", fg='#000000', font=font_for_note2)
    
    combobox.place(x = 180, y = 210, width=150, height = 20)
    label_music.place(x = 90, y = 170)

    # Button for strart and check errors of program
    btn_for_start = ttk.Button(text='Yebash!', command=start)
    btn_for_start.place(x=100, y=250, width=140, height=30)

    # Exit Button
    btn_exit = ttk.Button(text="Naxuy", command=exit)
    btn_exit.place(x = 260, y = 250, width = 140, height = 30)

    window.mainloop()


def renamefiles(name, addext, path):
    try:
        file_list = os.listdir(path)
    except FileNotFoundError and OSError:
        showerror(message=Error102.show(), title='Error')
        return 0

    # append additional extensions in main list of extensions
    addext = list(addext.split())
    extensions = ['jpeg', 'jpg', 'png', 'svg',
                  'tiff', "JPG", "PNG", "JPEG", "SVG", "TIFF"]
    extensions.extend(addext)
    # Opening current directory for rename
    os.chdir(path)

    def rename(old_name, num, name, extension):
        new_name = f'{name} {num}.{extension}'
        os.rename(old_name, new_name)

    a = 1
    # Rename every file in dir
    for file in file_list:
        path_of_file = file
        check_extensioin = path_of_file.split('.')
        definitely_ext = check_extensioin[1]
        if definitely_ext in extensions:
            rename(path_of_file, a, name, definitely_ext)
            a += 1


def main():
    OpenWindow()


if __name__ == "__main__":
    main()
else:
    print("You try to use this code as lib, but do this without respect. Don't do this please")
