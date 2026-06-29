from get_cursor import Cursor
from datetime import date
class ManageEarnD:
    
    _SELECT = 'SELECT * FROM daily_earn'
    _INSERT = 'INSERT INTO daily_earn (ci, earn, date) VALUES(%s, %s, %s)'
    _UPDATE = 'UPDATE daily_earn SET earn = earn + %s WHERE date = %s AND ci = %s'
    _DELETE = 'DELETE FROM daily_earn WHERE ci = %s'
    
    @classmethod
    def check(cls, user):
        records = cls.select(user[0])
        found = False
        
        for record in records:
            if record[0] == user[0]:
                user_update = (user[1], user[2], user[0])
                found = True
                break
            
        if found:
            cls.update(user_update)
        else:
            cls.insert(user)
    
    @classmethod
    def select (cls, id_user):
        query = cls._SELECT + ' WHERE date = %s AND ci = %s'
        today = date.today()
        values = (today, id_user)
        
        with Cursor() as cursor:
            cursor.execute(query,values)
            records = cursor.fetchall()
            users = []
            for record in records:
                users.append(record)
            return users
        
    @classmethod
    def insert(cls, user):
        with Cursor() as cursor:
            try:
                value = (user[0], user[1], user[2])
                cursor.execute(cls._INSERT, value)
            except Exception as e:
                print(f'An error occurred while we were adding a user: {e}')
    
    @classmethod            
    def update(cls, user):
        with Cursor() as cursor:
            try:        #earn     date     ci
                value = (user[0], user[1], user[2])
                cursor.execute(cls._UPDATE, value)
            except Exception as e:
                print(f'An error occurred while we were trying to update a user: {e}')

    @classmethod                
    def delete(cls, user):
        with Cursor() as cursor:
            try:
                value = (user,)
                cursor.execute(cls._DELETE, value)
            except Exception as e:
                print(f'An error occurred while we were trying to delete a user: {e}')
                
if __name__ == '__main__':
    
    earn = ManageEarnD().select('32.495.770')
    
    print(earn)