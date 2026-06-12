from get_cursor import Cursor
from my_loggers import log
from product import Product


class CRUD():
    _SELECT='SELECT * FROM products'
    _INSERT='INSERT INTO products (name, stock, cost) VALUES(%s, %s, %s)'
    _UPDATE='UPDATE products SET name=%s, stock=%s, cost=%s WHERE id = %s'
    _DELETE='DELETE FROM products WHERE id=%s'
    _UPDATESTOCK = 'UPDATE products SET stock = stock - %s WHERE name = %s'

    @classmethod
    def select(cls):
        with Cursor() as cursor:
            if cursor:
                cursor.execute(cls._SELECT)
                records = cursor.fetchall()
                products = []
                for record in records:
                    products.append(record)
                    log.debug('everything is working')
                return products

    @classmethod
    def insert(cls,product):
        with Cursor() as cursor:
            if cursor:
                try:
                    values = (product.name, product.stock, product.cost)
                    cursor.execute(cls._INSERT,values)
                    return cursor.rowcount
                except Exception as e:
                    log.error(f'An error ocurrer: {e}')

    @classmethod
    def update(cls, product):
        with Cursor() as cursor:
            if cursor:
                try:
                    values=(product.name, product.stock, product.cost, product.id)
                    cursor.execute(cls._UPDATE, values)
                    log.debug(cursor.rowcount)
                except Exception as e:
                    log.error(f'An error ocurrer while we were trying to update a product: {e}')

    @classmethod
    def delete(cls, product):
        with Cursor() as cursor:
            if cursor:
                try:
                    value = (product.id,)
                    cursor.execute(cls._DELETE, value)
                    log.debug(cursor.rowcount)
                except Exception as e:
                    log.error(f'An error ocurrer while we were trying to delete a product: {e}')
                    
    @classmethod
    def subtract(cls, products):
        try:
            with Cursor() as cursor:
                values = (products[0], products[1])
                cursor.execute(cls._UPDATESTOCK, values)
                return True
        except Exception as e:
            print(f'An error occurred while we were trying to do this :{e}')
            return False   
            
if __name__ == '__main__':

    #product_1 = Product(name='Flour', stock=45, cost=1.5)
    #insert_p = CRUD().insert(product=product_1)

    product_1 = Product(id=3,name='Spaghetti', stock=60, cost=2)
    update_p = CRUD().update(product=product_1)

    #product_1 = Product(id = 5)
    #delete_p = CRUD().delete(product=product_1)

    products = CRUD().select()
    if products:
        for product in products:
            print(product)
