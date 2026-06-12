import tkinter as tk
from tkinter.ttk import Treeview
from tkinter.messagebox import showwarning, showinfo, showerror
from datetime import date
from CRUD.CRUD_DailySales import CRUDSALES

from CRUD.CRUD_Products import CRUD


class Sell_Window(tk.Frame):
    def __init__(self, parent, master):
        super().__init__(parent, bg='#ffffff')
        self.products_list = []
        self.lb = tk.Label(self, text='Sell', font=('Arial',18, 'bold'), fg='black', bg='white')
        self.lb.pack(pady=20)
        self.container_search()
        self.fields_container()
        self.bar_search()
        self.container_tb_content()
        self.table_product()
        self.container_sell()
        self.table_sell()
        self.Entry_quantity()


    def container_search(self):
        self.container_sh = tk.Frame(self, bg='white')
        self.container_sh.pack(fill='x',pady=10)

    def fields_container(self):
        self.fields = tk.Frame(self,bg='white')
        self.fields.pack(fill='x',pady=10, side='bottom')

    def bar_search(self):
        self.search = tk.Entry(self.container_sh, width=25)
        self.search.pack(side='left', padx=10)
        
        self.button_search = tk.Button(self.container_sh, text='Search', font=('Arial', 10, 'bold'),width=10, command=self.search_option)
        self.button_search.pack(side= 'left')
        
    def container_tb_content(self):
        self.container_tb = tk.Frame(self)
        self.container_tb.pack(side='left', fill='both')

    def table_product(self):

        colum = ('ID', 'Product', 'Cost')
        self.table = Treeview(self.container_tb, columns=colum, show='headings')

        self.table.heading('ID', text='ID')
        self.table.heading('Product', text='Product')
        self.table.heading('Cost', text='Cost')

        self.table.column('ID',width=100)
        self.table.column('Product',width=150)
        self.table.column('Cost',width=150)

        self.table.bind('<<TreeviewSelect>>', self.get_product)
        
        self.load_products()

        self.table.pack(fill='both', expand=True)

    def container_sell(self):
        self.container_s = Treeview(self)

        self.container_s.pack(side='left', fill='both')

    def table_sell(self):

        colums = ('product', 'cost', 'quantity') 
        self.sell_tb = Treeview(self.container_s, columns=colums, show='headings')

        self.sell_tb.heading('product', text='Product')
        self.sell_tb.heading('cost', text='Cost')
        self.sell_tb.heading('quantity', text='Quantity')

        self.sell_tb.column('quantity', width=96)
        
        self.sell_tb.pack(fill='both', expand=True)

    def Entry_quantity(self):

        self.product_field = tk.Entry(self.fields, state='readonly')
        self.product_field.pack(side='left')
        
        self.cost_field = tk.Entry(self.fields, state='readonly')
        self.cost_field.pack(side='left')

        self.quantity_field = tk.Entry(self.fields)
        self.quantity_field.pack(side='left')
            
        self.button_q = tk.Button(self.fields, text='ADD', font=('Arial', 10, 'bold'), command=self.add_list)
        self.button_q.pack(side='left', padx=5)
        
        self.button_sell = tk.Button(self.fields, text='Sell', font=('Arial', 10, 'bold'), width=25, command=self.sell_button)
        self.button_sell.pack(side='left', padx=50)

    def load_products(self):

        for product in self.table.get_children():
            self.table.delete(product)

        products = CRUD.select()
        if products:
            for product in products:
                self.table.insert(parent='', index=tk.END, values=(product[0],product[1],product[3]))

    def clean_entries(self):
        self.product_field.configure(state='normal')
        self.cost_field.configure(state='normal')

        self.product_field.delete(0, tk.END)
        self.cost_field.delete(0, tk.END)
        self.quantity_field.delete(0, tk.END)

        self.product_field.configure(state='readonly')
        self.cost_field.configure(state='readonly')
        
    def get_product(self, event):
        product = self.table.selection()
        if product:
            list_product = self.table.item(product)['values']

            self.clean_entries()

            self.product_field.configure(state='normal')
            self.cost_field.configure(state='normal')

            self.product_field.insert(tk.END, list_product[1])
            self.cost_field.insert(tk.END, list_product[2])

            self.product_field.configure(state='readonly')
            self.cost_field.configure(state='readonly')
            
    def add_list(self):
        product = self.product_field.get()
        cost = self.cost_field.get()
        quantity = self.quantity_field.get()
        inf_product = (product, cost, quantity)
        add = True
        for product in self.products_list:
            if inf_product[0] in product[0]:
                add = False
                
        if add is not True:
            showwarning(title='Product in cart', message='The product is already')
        else:            
            self.products_list.append(inf_product)
            self.load_cart_table()
            print(self.products_list)

    def load_cart_table(self):

        for product in self.sell_tb.get_children():
            self.sell_tb.delete(product)

        for inf in self.products_list:
            self.sell_tb.insert(parent='', index='end', values=inf)
            
    def search_option(self):
        info = self.search.get()
        mach_product = []
        if info.isdigit():
            id_product = int(info)
            products = CRUD.select()
            for product in products:
                if id_product is product[0]:
                     mach_product.append((product[0],product[1],product[2],product[3]))
        else:
            products = CRUD.select()
            for product in products:
                if info in product[1]:
                    mach_product.append((product[0],product[1],product[2],product[3]))
                    
        if len(mach_product) == 0: 
            self.load_products()
            showwarning(title='No Found', message=f'The Product {info} was\'n found')
        else:
            for product in self.table.get_children():
                self.table.delete(product)

            for product in mach_product:
                self.table.insert(parent='', index='end', values=product)
                
    def sell_button(self):
        date_sale = date.today()
        for record in self.products_list:
            product = (record[0], record[2], date_sale)
            daily = CRUDSALES.check_products(product)
            store = CRUD.subtract((record[2], record[0]))
        if daily and store:
            showinfo(title = 'Sales', message= 'To sale is already')
            
            for product in self.sell_tb.get_children():
                self.sell_tb.delete(product)
            
            self.clean_entries()
        else:
            showerror(title='Sales', message='An error occurred please, check it')