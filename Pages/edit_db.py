import tkinter as tk

class Edit(tk.Frame):
    def __init__(self, parent, master):
        super().__init__(parent, bg="#ffffff")
        
        self.label = tk.Label(self, text='Edit Products', font=('Arial', 15, 'bold'), fg= 'black', bg='white')
        self.label.pack(pady=15)
        self.edit_container()
        self.entries()
        self.buttons()
        self.table_container()
        
    def edit_container(self):
        
        self.container = tk.Frame(self, bg='white')
        self.container.pack(fill='x', pady=10)
    
    def table_container(self):
        
        self.container_t = tk.Frame(self, bg='white')
        self.container_t.pack(fill='x', side='bottom')
        
    def entries(self):
        
        self.price_entry = tk.Entry(self.container, width=20)
        self.price_entry.pack(padx=5, side='left')

        self.quantity_entry = tk.Entry(self.container, width=20)
        self.quantity_entry.pack(padx=5, side='left')
        
        self.name_entry = tk.Entry(self.container, width=20)
        self.name_entry.pack(padx=5, side='left')
        
    def buttons(self):
        
        self.delete_button = tk.Button(self.container, text='Delete', font=('Arial', 10, 'bold'), width=14)
        self.delete_button.pack(side='right', padx=5)
        
        self.add_button = tk.Button(self.container, text='ADD', font=('Arial', 10, 'bold'), width=14)
        self.add_button.pack(side='right', padx=5)
        
    def get_entries(self):
        
        name = self.name_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()
        
        info = (name, quantity, price)
        return info
    
    def cleaner_entries(self):
        
        self.name_entry.delete(0, 'END')
        self.quantity_entry.delete(0, 'END')
        self.price_entry.delete(0, 'END')