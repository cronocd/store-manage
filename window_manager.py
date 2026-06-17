import tkinter as tk

class Manager:
    def __init__(self, root):
        self.root = root
        self.root.title('Storage')
        self.root.geometry('1080x600')


        #Nav Bar
        self.nav_bar = tk.Frame(self.root, bg='#2c3e50', width=180)
        self.nav_bar.pack(side = 'left', fill='y')
        self.nav_bar.pack_propagate(False)

        #Pages Container
        self.content_container = tk.Frame(self.root)
        self.content_container.pack(side='right', fill='both', expand=True)

        self.current_content = None
        
        self.show_buttons()

    #Buttons
    def show_buttons(self):
        from Pages.home import Home
        from Pages.Sell_W import Sell_Window
        from Pages.edit_db import Edit

        self.lb = tk.Label(self.nav_bar, text='Menu', font=('Arial', 12, 'bold'), bg = '#2c3e50', fg='white')
        self.lb.pack(pady=15)
        
        self.buttons_home = tk.Button(self.nav_bar, text='Home', relief='flat', command=lambda : self.show_pages(Home))
        self.buttons_home.pack(fill=tk.X, padx=10, pady=5)

        self.buttons_sell = tk.Button(self.nav_bar, text='Sell', relief='flat', command= lambda: self.show_pages(Sell_Window))
        self.buttons_sell.pack(fill=tk.X, padx=10, pady=20)
        
        self.button_edit = tk.Button(self.nav_bar, text='Edit Products', relief='flat', command= lambda: self.show_pages(Edit))
        self.button_edit.pack(fill=tk.X, padx=10, pady=50)
        


    def show_pages(self, pages_content):

        if self.current_content is not None:
            self.current_content.destroy()

        self.current_content = pages_content(self.content_container, self)
        self.current_content.pack(fill = 'both',  expand=True)
        