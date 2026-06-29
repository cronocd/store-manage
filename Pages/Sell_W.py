import tkinter as tk
from tkinter.ttk import Treeview
from tkinter.messagebox import showwarning, showinfo, showerror
from datetime import date
from CRUD.CRUD_DailySales import CRUDSALES
from CRUD.CRUD_MonthSales import CRUDSALESM
from CRUD.CRUD_Products import CRUD
from CRUD.CRUD_EarnDaily import ManageEarnD
from CRUD.CRUD_EarnMonthly import ManageEarnM
from Check.history import History
from datetime import date


class Sell_Window(tk.Frame):
    def __init__(self, parent, role):
        super().__init__(parent, bg='#ffffff')
        self.role = role
        self.products_list = []
        self.product_name = None
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
        
        self.lb_total = tk.Label(self. container_sh, text='0.00', font=('Arial', 20, 'bold'), bg = 'White')
        self.lb_total.pack(side='right') 
        
    def container_tb_content(self):
        self.container_tb = tk.Frame(self)
        self.container_tb.pack(side='left', fill='both', expand=True)

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

        self.container_s.pack(side='left', fill='both', expand=True)

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
            
        self.add_btn = tk.Button(self.fields, text='ADD', font=('Arial', 10, 'bold'), command=self.add_list)
        self.add_btn.pack(side='left', padx=5)
        
        self.cancel_btn = tk.Button(self.container_sh, text='Cancel', font=('Arial', 10, 'bold'), width=12, command=self.cancel_process)
        self.cancel_btn.pack(side='right', padx=45)
        
        self.delete_product_btn = tk.Button(self.container_sh, text='Delete Product', font=('Arial', 10, 'bold'), width=12, command=self.delete_product)
        self.delete_product_btn.pack(side='right', padx=30)
        
        self.button_sell = tk.Button(self.fields, text='Sell', font=('Arial', 10, 'bold'), width=20, command=self.sell_button)
        self.button_sell.pack(side='right', padx=45)

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
        
        if product and cost and quantity:
            for product in self.products_list:
                if inf_product[0] in product[0]:
                    add = False
                    
            if add is not True:
                showwarning(title='Product in cart', message='The product is already')
                self.clean_entries()
            else:            
                self.products_list.append(inf_product)
                self.load_cart_table()
                self.sum_total(inf_product)
                
        else:
            showwarning(title='...', message='Complete the field')
            self.clean_entries()
    
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
                if info.lower() in product[1].lower():
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
        records = CRUD.select()
        IDs = []

        if len(self.products_list) is not 0:
            
            for record in records:
                for product in self.products_list:
                    if not int(record[2]) > int(product[2]) and record[1] == product[0]:
                        showerror(title='NO STOCK', message=f'Stock not enough of {product[0]}')
                        IDs.append(product[0])
                        

            if len(self.products_list) != 0:
                
                for record in self.products_list:
                    if record[0] in IDs:
                        pass
                    else:
                        now = date.today()
                        product = (record[0], record[2], date_sale, self.role[2])
                        productm = (record[0], record[2], now, self.role[2])
                        daily = CRUDSALES.check_products(product)
                        month = CRUDSALESM.check_products(productm)
                        store = CRUD.subtract((record[2], record[0]))
                if daily and month and store:
                    showinfo(title = 'Sales', message= 'To sale is already')

                    for product in self.sell_tb.get_children():
                        self.sell_tb.delete(product)

                    History().log_sales(self.products_list, self.role[1])
                    ManageEarnD().check((self.role[2], float(self.lb_total['text']), now))
                    ManageEarnM().check_user((self.role[2], float(self.lb_total['text']), now))
                    self.clean_entries()
                    self.products_list = []
                    self.lb_total['text'] = '0.00'
                else:
                    showerror(title='Sales', message='An error occurred please, check it') 

                    for product in self.sell_tb.get_children():
                        self.sell_tb.delete(product)

                    self.products_list = []
        else:
            showwarning(title='...', message='Add something to the list first.')
            self.products_list = []
            
    def sum_total(self, product):
        
        if float(self.lb_total['text']) <= 0.00:
            total = float(product[1]) * int(product[2])
            self.lb_total['text'] = total
        else:
            lb_total = float(self.lb_total['text'])
            total = float(product[1]) * int(product[2]) + lb_total
            self.lb_total['text'] = total
            
    def cancel_process(self):
        
        if len(self.products_list) != 0:
            showinfo(title='Cancel', message='The sales was canceled')

            for product in self.sell_tb.get_children():
                self.sell_tb.delete(product)

            self.products_list = []
            self.lb_total['text'] = '0.00'
        else:
            showwarning(title='Cancel', message='Select something first')
    
    def delete_product(self):
        
        select = self.sell_tb.selection()
        
        if select:
            product = self.sell_tb.item(select)['values']
            
            
            lb_total = float(self.lb_total['text'])
            total = lb_total - float(product[1]) * int(product[2])
            self.lb_total['text'] = total
            
            id = 0
            found = False
            
            for record in self.products_list:
                
                if record[0] == product[0]:
                    found = True
                    break
                else:
                    id += 1 
            
            if found:
                self.products_list.pop(id)
            
            self.load_cart_table()
            self.clean_entries()
        else:
            showerror(title='Remove Product', message='Select something first')
            self.clean_entries()
            