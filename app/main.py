import tkinter 
from tkinter import * 
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter.messagebox import showerror
from tkinter import messagebox
from tkinter import colorchooser
from tkinter.messagebox import showinfo


# const
APP_NAME = 'Andrew`s Pad' 
WIDTH = 900
HEIGHT = 650



class Text_editor:
    def __init__(self):
        self.file_name = tkinter.NONE
    
    def new_file(self):
        self.file_name = 'Без названия'
        text.delete('1.0', tkinter.END)
    
    def open_file(self):
        inp = askopenfile(mode = 'r')
        if inp is None:
            return
        data = inp.read()
        text.delete('1.0', tkinter.END)
        text.insert('1.0', data)
    
    def save_file(self):
        data = text.get('1.0', tkinter.END)
        output =  open(self.file_name, 'w', encoding = 'utf-8')
        output.write(data)
        output.close()
    
    def save_as_file(self):
        output = asksaveasfile(mode = 'w', defaultextension = '.txt')
        data = text.get('1.0', tkinter.END)
        try:
            output.write(data.rstrip())
        except Exception:
            showerror(title = 'Ошибка!', message = 'Ошибка при сохранении файла')
    

    def get_info(self):
        messagebox.showinfo('Справка', 'Информация о нашем преложение! Спасибо, что его используете!')

    def abc_exit(self):
        app.quit()
    
    def ch_pro1(self):
        app.wm_attributes('-alpha', 1)
    
    def ch_pro2(self):
        app.wm_attributes('-alpha', 0.9)
    
    def ch_pro3(self):
        app.wm_attributes('-alpha', 0.75)
    
    def ch_pro4(self):
        app.wm_attributes('-alpha', 0.5)
    
    def dark_1(self):
        app.configure(bg = '#1c242e')
        text.config(bg = '#1c242e')
   
    def white_1(self):
        app.config(bg = 'white')
        text.config(bg = 'white')

    def ch_clr(self):
        color_bk = colorchooser.askcolor()
        app['bg'] = color_bk[1]
        text['bg'] = color_bk[1]
  
    def about_pr(self):
        hello = showinfo('Andrew`s Pad', 'Текстовый редактор\n\nВерсия: 1.00.1\nДанная программа написана исключительно на Python3\nДата написания: 3.12.2020\nАвтор: Недильской Андрей')


app = tkinter.Tk() 
app.title(APP_NAME)
app.minsize(width = WIDTH, height = HEIGHT) 
app.maxsize(width = WIDTH, height = HEIGHT) 

text = tkinter.Text(app, width = WIDTH - 50, height = HEIGHT, wrap = 'word') 
scroll = Scrollbar(app, orient = VERTICAL, command = text.yview) 
scroll.pack(side = 'right', fill = 'y') 
text.configure(yscrollcommand = scroll.set) 
text.pack()  
menubar =  tkinter.Menu(app) 
editor = Text_editor() 


app_menu = tkinter.Menu(menubar) 
app_menu.add_command(label= 'Новый файл', command = editor.new_file)
app_menu.add_command(label= 'Открыть', command = editor.open_file)
app_menu.add_command(label= 'Сохранить', command = editor.save_file)
app_menu.add_command(label= 'Сохранить как', command = editor.save_as_file)
app_menu.add_command(label= 'Выход', command = editor.abc_exit)

app_spravka = tkinter.Menu(menubar) 
app_spravka.add_command(label = 'О программе', command = editor.about_pr)

app_bk = tkinter.Menu(menubar)
app_bk.add_command(label = '1', command = editor.ch_pro1)
app_bk.add_command(label = '0.9', command = editor.ch_pro2)
app_bk.add_command(label = '0.75', command = editor.ch_pro3)
app_bk.add_command(label = '0.5', command = editor.ch_pro4)

app_changecolor = tkinter.Menu(menubar)
app_changecolor.add_command(label = 'Темная тема', command = editor.dark_1) 
app_changecolor.add_command(label = 'Светлая тема', command = editor.white_1) 
app_changecolor.add_command(label = 'Свой вариант', command = editor.ch_clr) 

menubar.add_cascade(label = 'Файл', menu = app_menu) 
menubar.add_cascade(label = 'Изменить цветовую тему', menu = app_changecolor) 
menubar.add_cascade(label = 'Изменить прозрачность редактора', menu = app_bk) 
menubar.add_cascade(label = 'Справка', menu = app_spravka, command = editor.get_info) 
app.config(menu = menubar) 


app.mainloop() 