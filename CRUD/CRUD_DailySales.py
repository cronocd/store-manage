from get_cursor import Cursor
from time import strftime



class CRUDSALES:
    
    _SELECT = 'SELECT * FROM dailysales WHERE date = %s AND id_user = %s'
    _INSERT = 'INSERT INTO dailysales(name, quantity, date, id_user) VALUES(%s, %s, %s, %s)'
    _UPDATE = 'UPDATE dailysales SET quantity = quantity + %s WHERE name = %s AND id_user = %s AND date = %s'
    
    @classmethod
    def check_products(cls, products):
        crud = CRUDSALES()
        records = crud.select(products[3])
        found_product = False
        
        for record in records:
            if products[0] == record[0]:
                product = (int(products[1]), products[0], products[3], products[2])
                found_product = True
                break
                
        if found_product:
            return crud.update(product)
        else:
            return crud.insert(products)
            
    
    def select(cls, id_user):
        with Cursor() as cursor:
            now = strftime("%Y-%m-%d")
            values = (now, id_user)
            cursor.execute(cls._SELECT, values)
            records = cursor.fetchall()
            products = []
            for record in records:
                products.append(record)
            return products
        
    def insert(cls, product):
        with Cursor() as cursor:
            try: 
                values = (product[0],product[1], product[2], product[3])
                cursor.execute(cls._INSERT, values)
                return True
            except Exception as e:
                print(f'An error occurred while we were trying add the sales.: {e}')
                return False
    def update(cls, product):
        with Cursor() as cursor:
            try:
                values = (product[0], product[1], product[2], product[3])
                cursor.execute(cls._UPDATE, values)
                return True
            except Exception as e:
                print(f'An error occurred while we were trying to do a update: {e}')
                return False
                
                
if __name__ == '__main__':
    
    #product = CRUDSALES().update((3,1))
    
    #product = CRUDSALES().insert(('Rice', '2', '12/2/2026'))
    
    #product = CRUDSALES().check_products(('Water', '1', '12/2/2026'))
    
    product = CRUDSALES().select()
    print(product)