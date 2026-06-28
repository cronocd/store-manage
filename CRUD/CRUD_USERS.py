from get_cursor import Cursor

class CrudUser:
    
    _SELECT = 'SELECT * FROM user_employees'
    _INSERT = 'INSERT INTO user_employees(name, lastname, age, ci, role, email, phone, password) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
    _UPDATE = 'UPDATE user_employees SET age = %s, role = %s, phone = %s, password = %s WHERE id = %s'
    _DELETE = 'DELETE FROM user_employees WHERE id = %s'
    
    
    
    
    @classmethod
    def select (cls):
        with Cursor() as cursor:
            cursor.execute(cls._SELECT)
            records = cursor.fetchall()
            users = []
            for record in records:
                users.append(record)
            return users
        
    @classmethod
    def insert(cls, user):
        with Cursor() as cursor:
            try:
                value = (user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7])
                cursor.execute(cls._INSERT, value)
            except Exception as e:
                print(f'An error occurred while we were adding a user: {e}')
                
    def update(cls, user):
        with Cursor() as cursor:
            try:
                value = (user[0], user[1], user[2], user[3], user[4])
                cursor.execute(cls._UPDATE, value)
            except Exception as e:
                print(f'An error occurred while we were trying to update a user: {e}')
                
    def delete(cls, user):
        with Cursor as cursor:
            try:
                value = (user,)
                cursor.execute(cls._DELETE, value)
            except Exception as e:
                print(f'An error occurred while we were trying to delete a user: {e}')

if __name__ == '__main__':
    
    app = User()
    
    record = app.select()
    
    for user in record:
        print(user)
    