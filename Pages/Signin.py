import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo, showwarning
from CRUD.CRUD_USERS import CrudUser
from user import User

class SignIn(tk.Toplevel):
    
    def __init__(self, master):
        super().__init__(master)
        self.geometry('500x500')
        self.title('Sign In')
        self.config(bg='White')
        self.lb = tk.Label(self, text='Sign In', bg='White', fg='Black', font=('Arial', 15, 'bold'))
        self.lb.pack()
        
        self.container_l()
        self.container_r()
        self.entries()
        self.admin_fields()
        
    
    def container_l(self):
        
        self.fields_container_l = tk.Frame(self, bg='White')
        self.fields_container_l.pack(side='left', fill='y',expand=True)
        
    def container_r(self):
        
        self.fields_container_r = tk.Frame(self, bg='White')
        self.fields_container_r.pack(side='right', fill='y', expand=True)
    
    def entries(self):
        
        self.name_lb = tk.Label(self.fields_container_l, text='Name', bg='white', fg='Black', font=('Arial', 12, 'bold'))
        self.name_lb.pack(pady=10)
        self.name = tk.Entry(self.fields_container_l)
        self.name.pack()

        self.lastname_lb = tk.Label(self.fields_container_r, text='Lastname', bg='white', fg='Black', font=('Arial', 12, 'bold'))
        self.lastname_lb.pack(pady=10)
        self.lastname = tk.Entry(self.fields_container_r)
        self.lastname.pack()
        
        self.age_lb = tk.Label(self.fields_container_l, text='Age', bg='white', fg='Black', font=('Arial', 12, 'bold'))
        self.age_lb.pack(pady=10)
        self.age = tk.Entry(self.fields_container_l)
        self.age.pack()

        self.ci_lb = tk.Label(self.fields_container_r, text='C.I', bg='white', fg='Black', font=('Arial', 12, 'bold'))
        self.ci_lb.pack(pady=10)
        self.ci = tk.Entry(self.fields_container_r)
        self.ci.pack()
        
        
        #Combobox
        value = tk.StringVar
        self.role_lb = tk.Label(self.fields_container_l, text='Role', bg='white', fg='Black', font=('Arial', 12, 'bold'))
        self.role_lb.pack(pady=10)
        self.role = ttk.Combobox(self.fields_container_l, textvariable=value, values=['Employee', 'Admin', 'Manage'])
        self.role.pack()
        self.role.set('Employee')
        
        self.email_lb = tk.Label(self.fields_container_r, text='Email', bg='white', fg='Black', font=('Arial', 12, 'bold'))
        self.email_lb.pack(pady=10)
        self.email = tk.Entry(self.fields_container_r)
        self.email.pack()
        
        self.phone_lb = tk.Label(self.fields_container_l, text='Phone', bg='white', fg='Black', font=('Arial', 12, 'bold'))
        self.phone_lb.pack(pady=10)
        self.phone = tk.Entry(self.fields_container_l)
        self.phone.pack()
        
        self.pwd_lb = tk.Label(self.fields_container_r, text='Password', bg='white', fg='Black', font=('Arial', 12, 'bold'))
        self.pwd_lb.pack(pady=10)
        self.pwd = tk.Entry(self.fields_container_r)
        self.pwd.pack()
        
        
    def admin_fields(self):
        
        self.name_admin_lb = tk.Label(self.fields_container_l, text='Name Admin', bg='White', font=('Arial', 12))
        self.name_admin_lb.pack(pady=20)
        self.name_admin = tk.Entry(self.fields_container_l)
        self.name_admin.pack()
        
        
        self.pwd_admin_lb = tk.Label(self.fields_container_r, text='Password Admin', bg='White', font=('Arial', 12))
        self.pwd_admin_lb.pack(pady=20)
        self.pwd_admin = tk.Entry(self.fields_container_r)
        self.pwd_admin.pack()
        
        self.button = tk.Button(self.fields_container_l, text='Enter', font=('Arial', 12, 'bold'), command=self.add_employee)
        self.button.pack(pady=20)
        
        self.button_c = tk.Button(self.fields_container_r, text='Close', font=('Arial', 12, 'bold'), command=self.close_btn)
        self.button_c.pack(pady=20)

    def valid_user(self):
        
        records = CrudUser().select()
        name = self.name_admin.get()
        pwd = self.pwd_admin.get()
        found = False
        
        for record in records:
            if name == record[1] and pwd == record[8] and record == 'admin' or record[5] == 'manage':
                found = True
                break
            
        if found:
            return True
        else:
            return False
    
    def get_entries(self):
        
        name = self.name.get()
        lastname = self.lastname.get()
        age = self.age.get()
        ci = self.ci.get()
        role = self.role.get().lower()
        email = self.email.get()
        phone = self.phone.get()
        pwd = self.pwd.get()
        
        
        if len(phone) == 11 and '@' in email:
            if name and lastname and age and ci and role and email and phone and pwd:
                user = (name, lastname, age, ci , role, email, phone, pwd)
                return user
            else:
                return False
        else:
            showwarning(title='Fields', message='Check the number phone or the email')
            return False
    
    def add_employee(self):
        authorized = self.valid_user()
        user = self.get_entries()
        
        if authorized and user:
            
            #user_inf = User(name = user[0], lastname = user[1], age = user[2], ci = user[3], role = user[4], email = user[5], phone = user[6], pwd = user[7])
            CrudUser().insert(user)
            
            showinfo(title= 'Sign In', message= 'The user was added')
            self.destroy()
            self.master.deiconify()
        else:
            showerror(title= 'Sign In', message= 'The user wasn`t added')

    def close_btn(self):
        self.destroy()
        self.master.deiconify()
        
if __name__ == '__main__':
    
    SignIn().mainloop()