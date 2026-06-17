from .Get_cursor import CursorM
import datetime
import calendar



class CRUDSALESM:
    
    _SELECT = 'SELECT * FROM monthdb'
    _INSERT = 'INSERT INTO monthdb(name,quantity,date) VALUES(%s,%s,%s)'
    _UPDATE = 'UPDATE monthdb SET quantity = quantity + %s WHERE id = %s'
    
    @classmethod
    def check_products(cls, products):
        crud = CRUDSALESM()
        records = crud.select_current_month()
        product = None
        found_product = False
        
        for record in records:
                if products[0] in record[1]:
                    id_product = record[0]
                    product = (int(products[1]), id_product)
                    found_product = True
                    
        if found_product:
            print("Here")
            crud.update(product)
            return True
        else:
            print("Here-")
            crud.insert(products)
            return True
            
    
    @classmethod
    def select(cls):
        with CursorM() as cursor:
            cursor.execute(cls._SELECT)
            records = cursor.fetchall()
            products = []
            for record in records:
                products.append(record)
            return products

    @classmethod
    def select_current_month(cls):
        """Return all monthdb rows for the current month automatically."""
        today = datetime.date.today()
        first_day = datetime.date(today.year, today.month, 1)
        last_day = datetime.date(today.year, today.month, calendar.monthrange(today.year, today.month)[1])
        query = cls._SELECT + ' WHERE date BETWEEN %s AND %s ORDER BY date'
        with CursorM() as cursor:
            cursor.execute(query, (first_day, last_day))
            return cursor.fetchall()

    @classmethod
    def select_month_sales(cls, year, month):
        """Return aggregated sales (name, total_quantity) for the given month.

        Uses a single SQL query with GROUP BY for efficiency.
        """
        first_day = datetime.date(year, month, 1)
        last_day = datetime.date(year, month, calendar.monthrange(year, month)[1])
        query = (
            "SELECT name, SUM(quantity) as total "
            "FROM monthdb "
            "WHERE date BETWEEN %s AND %s "
            "GROUP BY name "
            "ORDER BY total DESC"
        )
        with CursorM() as cursor:
            cursor.execute(query, (first_day, last_day))
            return cursor.fetchall()

    @classmethod
    def select_current_month_sales(cls):
        today = datetime.date.today()
        return cls.select_month_sales(today.year, today.month)

    @classmethod
    def select_previous_month_sales(cls):
        today = datetime.date.today()
        first_day_this_month = datetime.date(today.year, today.month, 1)
        prev_month_last = first_day_this_month - datetime.timedelta(days=1)
        return cls.select_month_sales(prev_month_last.year, prev_month_last.month)
        
    def insert(cls, product):
        with CursorM() as cursor:
            try: 
                values = (product[0], product[1], product[2])
                cursor.execute(cls._INSERT, values)
            except Exception as e:
                print(f'An error occurred while we were trying add the sales.: {e}')
                
    def update(cls, product):
        with CursorM() as cursor:
            try:
                values = (product[0], product[1])
                cursor.execute(cls._UPDATE, values)
            except Exception as e:
                print(f'An error occurred while we were trying to do a update: {e}')
                
                
if __name__ == '__main__':
    
    #product = CRUDSALESM().update((3,1))
    
    #product = CRUDSALESM().insert(('Rice', '2', '12/2/2026'))
    
    product = CRUDSALESM().check_products(('Water', '1', '2026/6/15'))
    
    product = CRUDSALESM().select()
    print(product)