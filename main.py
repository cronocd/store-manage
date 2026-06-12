import tkinter as tk
from window_manager import Manager
from Pages.home import Home

if __name__ == '__main__':
    root = tk.Tk()
    app = Manager(root)
    app.show_pages(Home)
    root.mainloop()
    