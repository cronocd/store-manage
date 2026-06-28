class User:
    def __init__(self, name='', lastname='', age=0, ci=0, role='', email='', phone='', pwd=''):
        self._name = name
        self._lastname = lastname
        self._age = age
        self._ci = ci
        self._role = role
        self._email = email
        self._phone = phone
        self._pwd = pwd

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        self._lastname = lastname

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def ci(self):
        return self._ci

    @ci.setter
    def ci(self, ci):
        self._ci = ci

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        self._role = role

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    @property
    def pwd(self):
        return self._pwd

    @pwd.setter
    def pwd(self, pwd):
        self._pwd = pwd