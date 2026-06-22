import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showwarning,showinfo
from product import  Product
from CRUD.CRUD_Products import CRUD
class Edit(tk.Frame):
    def __init__(self, parent, master):
        super().__init__(parent, bg="#ffffff")
        
        self.label = tk.Label(self, text='Edit Products', font=('Arial', 15, 'bold'), fg= 'black', bg='white')
        self.label.pack(pady=15)
        self.id_product = None
        self.edit_container()
        self.entries()
        self.buttons()
        self.table_container()
        self.table_product()
        
    def edit_container(self):
        
        self.container = tk.Frame(self, bg='white')
        self.container.pack(fill='x', pady=10)
    
    def table_container(self):
        
        self.container_t = tk.Frame(self, bg='white')
        self.container_t.pack(fill='both')
    
    def table_product(self):
        product = ('id', 'name', 'stock', 'price')
        
        self.table = ttk.Treeview(self.container_t, columns=product, show='headings')
        self. table.pack(fill='both', expand=True)
        
        self.table.heading('id', text = 'ID')
        self.table.heading('name', text = 'Name')
        self.table.heading('stock', text = 'Stock')
        self.table.heading('price', text = 'Price')
        
        self.load_table()
        
        self.table.bind('<<TreeviewSelect>>', self.get_info_tb)

    def entries(self):
        
        #--Name------
        self.name_entry = tk.Entry(self.container, width=20)
        self.name_entry.pack(padx=5, side='left')
        #------------
        
        #--Stock------
        self.quantity_entry = tk.Entry(self.container, width=20)
        self.quantity_entry.pack(padx=5, side='left')
        #-------------
        
        #--Cost--------
        self.price_entry = tk.Entry(self.container, width=20)
        self.price_entry.pack(padx=5, side='left')
        #--------------
        
    def buttons(self):
        
        self.delete_button = tk.Button(self.container, text='Delete', font=('Arial', 10, 'bold'), width=14, command= self.delete_product)
        self.delete_button.pack(side='right', padx=5)
        
        self.add_button = tk.Button(self.container, text='ADD', font=('Arial', 10, 'bold'), width=14, command=self.add_product)
        self.add_button.pack(side='right', padx=5)
        
    def get_entries(self):
        
        name = self.name_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()
        
        if name and quantity and price:
            info = (name, quantity, price)
            return info
        else:
            return False
    
    def cleaner_entries(self):
        
        self.name_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        
    def load_table(self):
        for product in self.table.get_children():
            self.table.delete(product)
            
        records = CRUD.select()
        for record in records:
            self.table.insert(parent='', index='end', values=record)
    
    def get_info_tb(self, event):
        info = self.table.selection()
        if info:
            product = self.table.item(info)['values']
            
            self.cleaner_entries()
            self.id_product = product[0]
            self.name_entry.insert(tk.END, product[1])
            self.quantity_entry.insert(tk.END, product[2])
            self.price_entry.insert(tk.END, product[3])
            
    def add_product(self):
        
        inf = self.get_entries()
        id = self.id_product

        if self.id_product is not None:
            normal_product = Product(id, inf[0], inf[1], inf[2])
            CRUD.update(normal_product)
            showinfo(title='...', message='The product was updated.')
            self.load_table()
            self.cleaner_entries()
            self.id_product = None
        elif inf is not False:
            normal_product = Product(name=inf[0],stock=inf[1],cost=inf[2])
            CRUD.insert(normal_product)
            showinfo(title='...', message='The product was added')
            self.load_table()
            self.cleaner_entries()            
        else:
            showwarning(title='....', message='Complete the field')
            
    def delete_product(self):
        
        id = Product(self.id_product)
        
        if id is not None:
            CRUD.delete(id,)
            showinfo(title='...', message='The product was deleted')
            self.id_product = None
            self.cleaner_entries()
            self.load_table()
        else:
            showwarning(title='...', message='First select the product that you want delete!')