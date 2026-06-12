import tkinter as tk
import matplotlib
from CRUD.CRUD_DailySales import CRUDSALES
from CRUD.CRUD_MonthSales import CRUDSALESM
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Home(tk.Frame):
    def __init__(self, parent, master):
        super().__init__(parent, bg="#ffffff")
        lbl = tk.Label(self, text="Welcome To Store", font=("Arial", 18), bg="#ffffff")
        lbl.pack(pady=50)

        self.month_container_chartbar()
        self.daily_container_chartbar()


    def month_container_chartbar(self):
        self.Chartbar_Container_M = tk.Frame(self, bg='#ffffff')
        self.Chartbar_Container_M.pack(fill= 'y', side='right',expand=True)

        products = []
        stock = []
        
        record = CRUDSALESM().select() 
        for product in record:
            products.append(product[1])
            stock.append(product[2])

        fig = Figure(figsize=(4,4), dpi=100)

        colors =['#3498db', '#2ecc71', '#e74c3c', '#f1c40f']

        ax= fig.add_subplot(111)
        ax.bar(products, stock, color=colors, edgecolor='#2c3e50', width=0.4)

        ax.set_title('Sales Month', fontsize=12, fontweight='bold', pad= 5)
        ax.set_ylabel('Quantity Products Selled', fontsize= 10, fontweight='bold', labelpad= 1)
        ax.set_xlabel('Products Selled', fontsize= 10, fontweight='bold', labelpad= 2)
        ax.grid(axis='y', linestyle='dashdot', alpha= 0.7)

        self.canvas = FigureCanvasTkAgg(fig, master=self.Chartbar_Container_M)
        self.canvas_widget = self.canvas.get_tk_widget()

        self.canvas_widget.pack(side='right', fill='y', expand=True, padx=5, pady=6)
        self.canvas.draw()

        
    def daily_container_chartbar(self):
        self.Chartbar_Container_D = tk.Frame(self, bg='#ffffff')
        self.Chartbar_Container_D.pack(fill='y', side='left', expand=True)

        products = []
        stock = []
        
        record = CRUDSALES().select() 
        for product in record:
            products.append(product[1])
            stock.append(product[2])

        fig = Figure(figsize=(4,4), dpi=100)

        ax = fig.add_subplot(111)

        colors = ['#3498db', '#2ecc71', '#e74c3c', '#f1c40f']

        ax.bar(products, stock, color=colors, edgecolor='#2c3e50', width=0.4)

        ax.set_title('Sales To Day', fontsize=12, fontweight='bold', pad=5)
        ax.set_ylabel('Quantity Products Selled', fontsize= 10, fontweight= 'bold', labelpad=1)
        ax.set_xlabel('Product Selled', fontsize= 10, fontweight='bold', labelpad=2)
        ax.grid(axis='y', linestyle='dashdot', alpha=0.7)

        self.canvas = FigureCanvasTkAgg(fig, master=self.Chartbar_Container_D)
        self.canvas_widget = self.canvas.get_tk_widget()

        self.canvas_widget.pack(side= 'left', fill='y', expand=True, padx=5, pady=6)

        self.canvas.draw()