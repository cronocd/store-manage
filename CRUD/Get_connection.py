from psycopg2 import pool


class ConnectionS:
    _DATABASE = 'daily_sales'
    _NAME = 'postgres'
    _PASSWORD = 'admin'
    _HOST = 'localhost'
    _PORT = '5432'
    _MIN_CONN = 1
    _MAX_CONN = 6
    pool = None
    
    
    @classmethod
    def get_pool(cls):
        if cls.pool is None:
            try:
                cls.pool = pool.SimpleConnectionPool(
                    cls._MIN_CONN,
                    cls._MAX_CONN,
                    database = cls._DATABASE,
                    user = cls._NAME,
                    password = cls._PASSWORD,
                    host = cls._HOST,
                    port = cls._PORT
                )
                print('Connection stablish: %s', cls.pool)
                return cls.pool
            except Exception as e:
                print('An error occurred while we were trying to create the pool: %s', e)
        else:
            return cls.pool
        
        
    @classmethod
    def get_connection(cls):
        pool = cls.get_pool()
        if pool is not None:
            connection = pool.getconn()
            print('Get the connection: %s', connection)
            return connection
        
        
    @classmethod
    def left_pool(cls, connection):
        pool = cls.get_pool()
        pool.putconn(connection)
        
        
    @classmethod
    def close_pool(cls):
        pool = cls.get_pool()
        pool.closeall()


class ConnectionM:
    
    _DB_NAME = 'month_sales'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _HOST = 'localhost'
    _PORT = '5432'
    _MIN_POOL = 1
    _MAX_POOL = 5
    pool = None
    
    @classmethod
    def get_pool(cls):
        if cls.pool is None:
            try:
                cls.pool = pool.SimpleConnectionPool(
                    cls._MIN_POOL,
                    cls._MAX_POOL,
                    database = cls._DB_NAME,
                    user = cls._USERNAME,
                    password = cls._PASSWORD,
                    host = cls._HOST,
                    port = cls._PORT,
                )
                print(cls.pool)
                return cls.pool
            except Exception as e:
                print(f'An error occurred while we trying to connect: {e}')       
        else:
            return cls.pool
        
    @classmethod
    def get_connection(cls):
        pool = cls.get_pool()
        connection = pool.getconn()
        print(connection)
        return connection
    
    @classmethod
    def left_pool(cls, connection):
        pool = cls.get_pool()
        pool.putconn(connection)
    
    @classmethod
    def close_pool(cls):
        pool = cls.get_pool()
        pool.closeall()

if __name__ == '__main__':
    connection1 = ConnectionM().get_connection()
    ConnectionM().left_pool(connection1)
    
    connection2 = ConnectionM().get_connection()
    ConnectionM().left_pool(connection2)
    
    connection3 = ConnectionM().get_connection()
    ConnectionM().left_pool(connection3)
