class User:
    def __init__(self, name = '', lastname = '', age = 0, ci = 0, role = '', email = '', phone = '', pwd = ''):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.ci = ci
        self.role = role
        self.email = email
        self.phone = phone
        self.pwd = pwd
        
        
    @property
    def name(self):
        return self.name
    @name.setter
    def name(self, name):
        self.name = name
        
    @property
    def lastname(self):
        return self.lastname
    @lastname.setter
    def lastname(self, lastname):
        self.lastname = lastname
    
    @property
    def age(self):
        return self.age
    @age.setter
    def age(self, age):
        self.age = age
        
    @property
    def ci(self):
        return self.ci
    @ci.setter
    def ci(self, ci):
        self.ci = ci
        
    @property
    def role(self):
        return self.role
    @role.setter
    def role(self, role):
        self.role = role
        
    @property
    def email(self):
        return self.email
    @email.setter
    def email(self, email):
        self.email = email
        
    @property
    def phone(self):
        return self.phone
    @phone.setter
    def phone(self, phone):
        self.phone = phone
        
    @property
    def pwd(self):
        return self.pwd
    @pwd.setter
    def pwd(self, pwd):
        self.pwd = pwd