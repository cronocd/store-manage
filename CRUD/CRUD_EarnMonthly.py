from get_cursor import Cursor
import datetime
import calendar


class ManageEarnM:
    _INSERT = 'INSERT INTO month_earn (ci, earn, date) VALUES(%s, %s, %s)'
    _UPDATE = 'UPDATE month_earn SET earn = earn + %s WHERE date = %s AND ci = %s'

    @classmethod
    def check_user(cls, user):
        
        records = cls.select(user[0])
        found = False
        
        for record in records:
            if record[0] == user[0]:
                #              earn     date     ci
                user_update = (user[1], user[2], user[0])
                found = True
                break
            
        if found:
            cls.update(user_update)
        else:
            cls.insert(user)
    
    @classmethod
    def select(cls, ci):
        query = 'SELECT * FROM month_earn WHERE date = %s AND ci = %s'
        today = datetime.date.today()
        value = (today, ci)
        with Cursor() as cursor:
            cursor.execute(query, value)
            records = cursor.fetchall()
            user = []
            for record in records:
                user.append(record)
            return user
    
    @classmethod
    def select_current_month(cls, id_user):
        today = datetime.date.today()
        first_day = datetime.date(today.year, today.month, 1)
        last_day = datetime.date(today.year, today.month, calendar.monthrange(today.year, today.month)[1])
        query = (
            'SELECT SUM(earn) AS total '
            'FROM month_earn '
            'WHERE date BETWEEN %s AND %s AND ci = %s '
            'ORDER BY total DESC'
        )
        with Cursor() as cursor:
            cursor.execute(query, (first_day, last_day, id_user))
            return cursor.fetchall()

    @classmethod
    def insert(cls, user):
        with Cursor() as cursor:
            try:
                values = (user[0], user[1], user[2])
                cursor.execute(cls._INSERT, values)
                return True
            except Exception as e:
                print(f'An error occurred while we were trying add the sales.: {e}')
                return False

    @classmethod 
    def update(cls, user):
        with Cursor() as cursor:
            try:
                values = (user[0], user[1], user[2])
                cursor.execute(cls._UPDATE, values)
            except Exception as e:
                print(f'An error occurred while we were trying update the earn: {e}')