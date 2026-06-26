from get_cursor import Cursor

class User:
    
    _SELECT = 'SELECT * FROM user_employees'
    _INSERT = 'INSERT INTO user_employees(name, lastname, age, ci, role, phone, pwd) VALUES(%s, %s, %s, %s, %s, %s, %s)'
    _UPDATE = 'UPDATE user_employees SET age = %s, role = %s, phone = %s, pwd = %s WHERE id == %s'
    _DELETE = 'DELETE FROM user_employees WHERE id == %s'
    
    
    
    
    @classmethod
    def select (cls):
        with Cursor() as cursor:
            cursor.execute(cls._SELECT)
            records = cursor.fetchall()
            users = []
            for record in records:
                users.append(record)
            return users

if __name__ == '__main__':
    
    app = User()
    
    record = app.select()
    
    for user in record:
        print(user)
    