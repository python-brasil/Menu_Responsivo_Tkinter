from tkinter import *
from Functions import *


class NavBarDinamica():
    def __init__(self):
        self.root = Tk()
        self.root.geometry(center(self.root, 1366,768))
        self.root.title('Barra de navegação responsiva com Tkinter')
        self.root.config(bg='#444654')
        
        self.img_home = PhotoImage(file=r'img\icons8-home-24.png')
        self.img_user = PhotoImage(file=r'img\icons8-user-60.png')
        self.img_cofig = PhotoImage(file=r'img\icons8-settings-60.png')
        
        
        self.containers()
        self.itens_container01()
        
        self.root.mainloop()
        
    def containers(self):
        self.fr_container01 = Frame(
            self.root,
            bg='#202123',
            width= 200,
            height=768
        )   
        
        self.fr_container02 = Frame(
            self.root,
            bg='#202123',
            width= 60,
            height=768
        )  
        
        self.fr_container01.propagate(0)
        self.fr_container01.pack(side=LEFT)
        self.fr_container02.propagate(0)
 
          
    def itens_container01(self):
        self.btn_hide_bar = Button(
            self.fr_container01,
            text='<',
            font='Poppins 20',
            fg='#d1d5d3',
            bd=0,
            bg=self.fr_container01.cget('bg'),
            activeforeground='#bcbbbb',
            activebackground=self.fr_container01.cget('bg'),
            cursor='hand2',
            command=self.hide_menu
        )
        
        self.btn_home = Button(
            self.fr_container01,
            text='Home',
            font='Poppins 15',
            fg='#d1d5d3',
            bd=0,
            bg=self.fr_container01.cget('bg'),
            activebackground=self.fr_container01.cget('bg'),
            activeforeground='#bcbbbb',
            cursor='hand2',
            command=None
        )
        
        self.btn_users = Button(
            self.fr_container01,
            text='Users',
            font='Poppins 15',
            fg='#d1d5d3',
            bd=0,
            bg=self.fr_container01.cget('bg'),
            activebackground=self.fr_container01.cget('bg'),
            activeforeground='#bcbbbb',
            cursor='hand2',
            command=None
        )
        
        self.btn_config = Button(
            self.fr_container01,
            text='Tools',
            font='Poppins 15',
            fg='#d1d5d3',
            bd=0,
            bg=self.fr_container01.cget('bg'),
            activebackground=self.fr_container01.cget('bg'),
            activeforeground='#bcbbbb',
            cursor='hand2',
            command=None
        )
        self.btn_hide_bar.pack(anchor=E,padx=20)
        self.btn_home.pack()   
        self.btn_users.pack()   
        self.btn_config.pack()   
        
    def itens_container02(self):
        self.btn_show_bar = Button(
            self.fr_container02,
            text='>',
            font='Poppins 20',
            fg='#d1d5d3',
            bd=0,
            bg=self.fr_container01.cget('bg'),
            cursor='hand2',
            activebackground=self.fr_container01.cget('bg'),
            command=self.show_menu
        )
        
        self.btn_home_ico = Button(
            self.fr_container02,
            image=self.img_home,
            font='Poppins 15',
            fg='#d1d5d3',
            bd=0,
            bg=self.fr_container01.cget('bg'),
            cursor='hand2',
            activebackground=self.fr_container01.cget('bg'),
            command=None
        )
        self.btn_users_ico = Button(
            self.fr_container02,
            image=self.img_user,
            
            font='Poppins 15',
            fg='#d1d5d3',
            bd=0,
            bg=self.fr_container01.cget('bg'),
            cursor='hand2',
            activebackground=self.fr_container01.cget('bg'),
            command=None
        )
        
        self.btn_config_ico = Button(
            self.fr_container02,
            image=self.img_cofig,
            font='Poppins 15',
            fg='#d1d5d3',
            bd=0,
            bg=self.fr_container01.cget('bg'),
            cursor='hand2',
            activebackground=self.fr_container01.cget('bg'),
            command=None
        )
        
        self.btn_show_bar.pack(anchor=E,padx=20)
        self.btn_home_ico.pack()   
        self.btn_users_ico.pack()   
        self.btn_config_ico.pack()
        
    def show_menu(self):
        
        # Mostra ou esconde o menu lateral
        if self.fr_container02.winfo_viewable():
            for widget in self.fr_container02.winfo_children():
                widget.destroy()     

            self.fr_container02.pack_forget()
            self.fr_container01.pack(side=LEFT)
            
            self.itens_container01()
        else:
            self.fr_container02.pack(side="left", fill="y")
            
    def hide_menu(self):
        
        # Mostra ou esconde o menu lateral
        if self.fr_container01.winfo_viewable():
            for widget in self.fr_container01.winfo_children():
                widget.destroy()
            self.fr_container01.pack_forget()
            self.fr_container02.pack(side=LEFT)
            self.itens_container02()
        else:
            self.fr_container01.pack(side="left", fill="y")
            
        
NavBarDinamica()