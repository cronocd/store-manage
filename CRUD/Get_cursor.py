from .Get_connection import ConnectionS
from .Get_connection import ConnectionM
class CursorS:
    
    def __init__(self):
        self.cursor = None
        self.connection = None
        
    def __enter__(self):
        self.connection = ConnectionS().get_connection()
        
        self.cursor = self.connection.cursor()
        print('Cursor:%s',self.cursor)
        return self.cursor
    
    def __exit__(self, exc_type, exc, tb):
        
        if exc:
            self.connection.rollback()
            print('[%s]-:-{%s}-:-{%s}', exc, exc_type, tb)
        else:
            self.connection.commit()
            self.cursor.close()
            ConnectionS().left_pool(self.connection)
            
class CursorM:
    
    def __init__(self):
        self.connection = None
        self.cursor = None
        
    def __enter__(self):
        self.connection = ConnectionM().get_connection()
        self.cursor = self.connection.cursor()
        print(self.cursor)
        return self.cursor
    
    def __exit__(self, exc_type, exc, tb):
        if exc:
            self.connection.rollback()
            print(f'{exc}-:-{exc_type}-:-{tb}')
        else:
            self.connection.commit
            self.cursor.close
            ConnectionM().left_pool(self.connection)
            
if __name__ == '__main__':

    with CursorM() as cursor:
        if cursor:
            cursor.execute('SELECT * FROM monthdb')
            print(cursor.fetchall())