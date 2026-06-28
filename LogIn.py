import tkinter as tk
from window_manager import Manager
from Pages.home import Home
from Check.history import History
from tkinter.messagebox import showwarning, showinfo, showerror
from CRUD.CRUD_USERS import CrudUser
from Pages.Signin import SignIn

class Login(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.geometry('400x400')
        self.title('Log In')
        self.config(bg = 'white')
        
        self.label = tk.Label(self, text='Log In', font=('Arial', 15, 'bold'), bg='white')
        self.label.pack(pady=10, side='top', ipady=20)
        
        self.user_label = tk.Label(self, text='Name', bg='white', font=('Arial', 12, 'bold'))
        self.user_label.pack()
        
        self.user = tk.Entry(self, width=20, fg='black', font=('Arial', 12, 'bold'))
        self.user.pack(pady=10)
        
        self.pwd_label = tk.Label(self, text='Password', bg='white', font=('Arial', 12, 'bold'))
        self.pwd_label.pack()
        
        self.pwd = tk.Entry(self, width=20, fg='black', font=('Arial', 12, 'bold'), show='*')
        self.pwd.pack(pady=10)
        
        self.button = tk.Button(self, text='Enter', command=self.check_user)
        self.button.pack(pady=30, side='left')
        
        self.buttonSing = tk.Button(self, text='Sing In', command=self.signin)
        self.buttonSing.pack(pady=30, side='right')
        
    def get_entries(self):
        
        user = self.user.get()
        pwd = self.pwd.get()
        if user and pwd:
            inf = (user, pwd)
            return inf
        else:
            False

    def check_user(self):
        
        info = self.get_entries()
        record = CrudUser().select()
        found_user = False
        role = ()
        
        if info:
            for user in record:
                if user[1] == info[0] and user[8] == info[1]:
                    found_user = True
                    role = (user[5], user[1], user[4])
                    break
                else:
                    found_user = False
                    role = ()
            
        else:
            showwarning(title='Field', message='Complete the field first')
        
        if found_user:
            self.destroy()
            self.log(role)
        else:
            showerror(title='Not found', message='Check the info and try again')
            

    def log(self, role):

        History().check_folder(role[1]) 
        root = tk.Tk()
        app = Manager(root, role)
        app.show_pages(Home)
        root.mainloop()
        
    def signin(self):
        self.withdraw()
        SignIn(self)
        


if __name__ == '__main__':
    app= Login()
    app.mainloop()