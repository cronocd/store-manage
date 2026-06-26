from get_cursor import Cursor



class CRUDSALES:
    
    _SELECT = 'SELECT * FROM dailysales WHERE date = CURRENT_DATE ORDER BY date DESC'
    _INSERT = 'INSERT INTO dailysales(name,quantity,date) VALUES(%s,%s,%s)'
    _UPDATE = 'UPDATE dailysales SET quantity = quantity + %s WHERE id = %s'
    
    @classmethod
    def check_products(cls, products):
        crud = CRUDSALES()
        records = crud.select()
        product = None
        found_product = False
        
        for record in records:
                if products[0] in record[1]:
                    id_product = record[0]
                    product = (int(products[1]), id_product)
                    found_product = True
                    
        if found_product:
            crud.update(product)
            return True
        else:
            crud.insert(products)
            return True
            
    
    def select(cls):
        with Cursor() as cursor:
            cursor.execute(cls._SELECT)
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
            except Exception as e:
                print(f'An error occurred while we were trying add the sales.: {e}')
                
    def update(cls, product):
        with Cursor() as cursor:
            try:
                values = (product[1], product[2])
                cursor.execute(cls._UPDATE, values)
            except Exception as e:
                print(f'An error occurred while we were trying to do a update: {e}')
                
                
if __name__ == '__main__':
    
    #product = CRUDSALES().update((3,1))
    
    #product = CRUDSALES().insert(('Rice', '2', '12/2/2026'))
    
    #product = CRUDSALES().check_products(('Water', '1', '12/2/2026'))
    
    product = CRUDSALES().select()
    print(product)