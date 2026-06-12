from psycopg2 import pool
from my_loggers import log

class Connection():
    _DATABASE = 'Inventory_test'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _HOST = 'localhost'
    _PORT = '5432'
    _MIN_POOL = 1
    _MAX_POOL = 10
    _pool = None

    @classmethod
    def get_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_POOL,
                    cls._MAX_POOL,
                    database = cls._DATABASE,
                    user = cls._USERNAME,
                    password = cls._PASSWORD,
                    host = cls._HOST,
                    port = cls._PORT
                )
                return cls._pool
            except Exception as e:
                log.error(f'An error occurred while we were trying take the pool: {e}')
        else:
            return cls._pool

    @classmethod
    def get_connection(cls):
        pool = cls.get_pool()
        if pool is None:
            raise RuntimeError("Database pool is not initialized.")
        
        connection = pool.getconn()
        log.debug(connection)
        return connection

    @classmethod
    def left_connection(cls,connection):
        pool = cls.get_pool()
        if pool:
            pool.putconn(connection)

    @classmethod
    def close_connections(cls):
        pool = cls.get_pool()
        if pool:
            pool.closeall()


if __name__ == '__main__':
    connection1 = Connection().get_connection()
    Connection().left_connection(connection1)

    connection2 = Connection().get_connection()
    Connection().left_connection(connection2)

    connection3 = Connection().get_connection()
    Connection().left_connection(connection3)