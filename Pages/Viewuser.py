import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
from CRUD.CRUD_USERS import CrudUser
from Pages.Signin import SignIn
from CRUD.CRUD_EarnDaily import ManageEarnD
from CRUD.CRUD_EarnMonthly import ManageEarnM

class ViewUser(tk.Frame):
    
    def __init__(self, parent, role):
        super().__init__(parent, bg="#ffffff")
        self.id_user = None
        self.user_role = role
        self.lb = tk.Label(self, text='View Employees', font=('Arial', 15, 'bold'), bg='white', fg='black')
        self.lb.pack(side= 'top', pady=5)
        self.container_top()
        self.container_btm()
        self.entries()
        self.buttons(parent)
        self.tb()
        
    def container_top(self):
        
        self.container_fd = tk.Frame(self, bg='white')
        self.container_fd.pack(pady=10, fill='x')    
    
    def container_btm(self):
        
        self.container_tb = tk.Frame(self)
        self.container_tb.pack(side='bottom', fill='both', expand= True)
    
    def on_focus_in(self, event):
        widget = event.widget
        
        if widget.get() in ('Age', 'Phone', 'Email'):
            widget.delete(0, 'end')
            
    def on_focus_out(self, event):
        
        widget = event.widget
        
        if widget.get() == "":
            if widget is self.age:
                widget.insert(0, 'Age')
            elif widget is self.phone:
                widget.insert(0, 'Phone')
            else:
                widget.insert(0, 'Email')
    
    def placeholder(self):
        
        self.age.insert(0, 'Age')        
        self.role_cb.set('Employee')        
        self.phone.insert(0, 'phone')        
        self.email.insert(0, 'email')        
        self.status_user.set('Active')        
        
    def entries(self):
        
        self.age = tk.Entry(self.container_fd, width=10)
        self.age.insert(0, 'Age')
        self.age.pack(side='left', padx=5)
        self.age.bind("<FocusIn>", self.on_focus_in)
        self.age.bind("<FocusOut>", self.on_focus_out)

        self.role_var = tk.StringVar()
        self.role_cb = ttk.Combobox(self.container_fd, textvariable=self.role_var, values=['Employee', 'Admin', 'Manage'], width=20)
        self.role_cb.pack(side='left', padx=5)
        self.role_cb.set('Employee')
        
        
        self.phone = tk.Entry(self.container_fd, width=15)
        self.phone.insert(0, 'Phone')
        self.phone.pack(side='left', padx=5)
        self.phone.bind("<FocusIn>", self.on_focus_in)
        self.phone.bind("<FocusOut>", self.on_focus_out)
        
        self.email = tk.Entry(self.container_fd, width=20)
        self.email.insert(0, 'Email')
        self.email.pack(side='left', padx=5)
        self.email.bind("<FocusIn>", self.on_focus_in)
        self.email.bind("<FocusOut>", self.on_focus_out)
        
        self.status_var = tk.StringVar()
        self.status_user = ttk.Combobox(self.container_fd, textvariable=self.status_var, values=['Activate', 'Deactivate'], width=20)
        self.status_user.pack(side='left', padx=5)
        self.status_user.set('Activate')
        
    def tb(self):
        
        headers = ('name', 'lastname', 'age', 'ci', 'role', 'phone', 'email', 'status', 'sales(d)', 'sales(m)')
        self.table_users = ttk.Treeview(self.container_tb, columns=headers, show='headings')
        
        self.table_users.heading('name', text='Name')
        self.table_users.heading('lastname', text='Lastname')
        self.table_users.heading('age', text='Age')
        self.table_users.heading('ci', text='C.I')
        self.table_users.heading('role', text='Role')
        self.table_users.heading('phone', text='Phone')
        self.table_users.heading('email', text='Email')
        self.table_users.heading('status', text='Status')
        self.table_users.heading('sales(d)', text='Sales(D)')
        self.table_users.heading('sales(m)', text='Sales(M)')
        
        self.table_users.column('name', width=45)
        self.table_users.column('lastname', width=45)
        self.table_users.column('age', width=5)
        self.table_users.column('ci', width=40)
        self.table_users.column('role', width=35)
        self.table_users.column('phone', width=40)
        self.table_users.column('email', width=65)
        self.table_users.column('status', width=5)
        self.table_users.column('sales(d)', width=5)
        self.table_users.column('sales(m)', width=5)
        
        self.loadinfo()
        
        self.table_users.bind("<<TreeviewSelect>>", self.insert_entries)
        self.table_users.pack(fill='both', expand=True)
        
    def loadinfo(self):
        
        for user in self.table_users.get_children():
            self.table_users.delete(user)
            
        records = CrudUser().select()
        
        for user in records:
            earn_day = ManageEarnD().select(user[4])
            try:
                earnd = earn_day[0][1]
            except Exception:
                earnd = 0.00
            
            earn_month = ManageEarnM().select(user[4])
            try:
                earnm = earn_month[0][1]
            except Exception:
                earnm = 0.00
                
            self.table_users.insert(parent='', index='end', values=(user[1], user[2], user[3], user[4], user[5].capitalize(), user[7], user[6], user[9].capitalize(), earnd, earnm))
            
    def insert_entries(self, event):
        select = self.table_users.selection()
        if select:
            inf = self.table_users.item(select)['values']
            
            self.clean_entries()
            self.id_user = inf[3]
            self.age.insert(0, inf[2])
            self.role_cb.set(inf[4])
            self.phone.insert(0, inf[5])
            self.email.insert(0, inf[6])
            self.status_user.set(inf[7])
            
    def clean_entries(self):
        
        self.age.delete(0, 'end')
        self.phone.delete(0, 'end')
        self.email.delete(0,'end')
    
    def buttons(self, parent):
        
        self.refresh_btn = tk.Button(self.container_fd, text='🗘', font=('Arial', 12, 'bold'), width=5, command= self.loadinfo)
        self.refresh_btn.pack(side='right')
        
        self.update_btn = tk.Button(self.container_fd, text='Update', font=('Arial', 12, 'bold'), width=15, command= self.update_user)
        self.update_btn.pack(side='right', padx=10)
        
        self.add_btn = tk.Button(self.container_fd, text='Add', font=('Arial', 12, 'bold'), width=15, command= lambda: self.add_user(parent))
        self.add_btn.pack(side='right', padx=10)
    
    def update_user(self):
        age = self.age.get()
        role = self.role_cb.get()
        phone = self.phone.get()
        email = self.email.get()
        status = self.status_user.get()
        
        if age and age != 'Age' and role and phone and email and status and self.id_user != None:
            
            info = (age, role.lower(), phone, email, status.lower(), self.id_user)
            CrudUser().update(info)
            showinfo(title='Fields', message='The user was updated')
            self.clean_entries()
            self.placeholder()
            self.id_user = None
            self.loadinfo()
        else:
            showerror(title= 'Fields', message= 'Select something first')
            
    def add_user(self, parent):
        SignIn(parent)