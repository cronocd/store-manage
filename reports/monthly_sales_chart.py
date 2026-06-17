import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from CRUD.CRUD_MonthSales import CRUDSALESM

OUTPUT_DIR = os.path.join(os.path.dirname(__file__))
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'monthly_sales.png')


def generate_month_chart(output_path=None):
    data = CRUDSALESM.select_current_month_sales()
    if not data:
        print('No sales for current month to plot.')
        return None

    names = [row[0] for row in data]
    totals = [int(row[1]) for row in data]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(names, totals, color='tab:blue')
    plt.xlabel('Product')
    plt.ylabel('Quantity sold')
    plt.title('Sales by product - Current Month')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    for bar, val in zip(bars, totals):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(val),
                 ha='center', va='bottom')

    out = output_path or OUTPUT_FILE
    plt.savefig(out)
    plt.close()
    print(f'Chart saved to: {out}')
    return out


if __name__ == '__main__':
    generate_month_chart()
