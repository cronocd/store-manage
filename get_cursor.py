from psycopg2.extensions import cursor
from connection import Connection
from my_loggers import log
class Cursor():

    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = Connection.get_connection() 

        if self.connection:
            self.cursor = self.connection.cursor()
            log.debug(self.cursor)
            return self.cursor

    def __exit__(self, exc_type, exc, tb):
        if self.connection:
            if exc:
                self.connection.rollback()
                log.error(f'{exc_type}-{exc}-{tb}')
            else:
                self.connection.commit()
                
                if self.cursor:
                    self.cursor.close()
                Connection.left_connection(self.connection) 

if __name__ == '__main__':

    with Cursor() as cursor:
        if cursor:
            cursor.execute('SELECT * FROM products')
            log.debug(cursor.fetchall())