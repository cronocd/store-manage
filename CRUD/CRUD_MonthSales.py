from get_cursor import Cursor
import datetime
import calendar


class CRUDSALESM:
    _SELECT = 'SELECT * FROM monthsales'
    _INSERT = 'INSERT INTO monthsales(name, quantity, date, id_user) VALUES(%s, %s, %s, %s)'

    @classmethod
    def check_products(cls, products):
        crud = CRUDSALESM()
        return crud.insert(products)

    @classmethod
    def select(cls):
        with Cursor() as cursor:
            cursor.execute(cls._SELECT)
            records = cursor.fetchall()
            products = []
            for record in records:
                products.append(record)
            return products

    @classmethod
    def select_current_month(cls, id_user):
        today = datetime.date.today()
        first_day = datetime.date(today.year, today.month, 1)
        last_day = datetime.date(today.year, today.month, calendar.monthrange(today.year, today.month)[1])
        query = (
            'SELECT name, SUM(quantity) AS total '
            'FROM monthsales '
            'WHERE date BETWEEN %s AND %s AND id_user = %s '
            'GROUP BY name '
            'ORDER BY total DESC'
        )
        with Cursor() as cursor:
            cursor.execute(query, (first_day, last_day, id_user))
            return cursor.fetchall()

    def insert(cls, product):
        with Cursor() as cursor:
            try:
                values = (product[0], product[1], product[2], product[3])
                cursor.execute(cls._INSERT, values)
                return True
            except Exception as e:
                print(f'An error occurred while we were trying add the sales.: {e}')
                return False


if __name__ == '__main__':
    # product = CRUDSALESM().check_products(('Water', '1', '2026-06-15', '32.495.769'))
    product = CRUDSALESM().select()
    print(product)
