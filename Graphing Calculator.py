import re
import numpy as np
import tkinter as tk
import ttkbootstrap as ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk, FigureCanvasTkAgg


def app_start():
    window = ttk.Window(themename = 'darkly')
    window.title("Graphing Calculator")
    window.geometry("1300x900")

    title_display = ttk.Label(master = window, text = "APCSP Graphing Calculator", font = "Consolas 25 bold")
    title_display.pack(pady = 25)
    
    inputbox = ttk.Frame(master = window)
    inputbox_str = tk.StringVar()
    entry = ttk.Entry(master = inputbox, textvariable = inputbox_str)

    def populate_graph():
        x, y = root(inputbox_str.get())
        graph(window, x, y)

    populate_button = ttk.Button(master = inputbox, text = "Graph", command = populate_graph)
    ƒofx = ttk.Label(master = inputbox, text = "ƒ = ", font = "Consolas 18")
    ƒofx.pack(side = "left")
    entry.pack(side = "left")
    populate_button.pack(side = "left", padx = 10)
    
    inputbox.pack(pady = 10)

    window.mainloop()

def graph(window, x, y):
    if hasattr(window, 'canvas'):
        window.canvas.get_tk_widget().destroy()
    if hasattr(window, 'toolbar'):
        window.toolbar.destroy()

    window.fig, window.ax = plt.subplots()
    window.ax.plot(x, y)
    window.canvas = FigureCanvasTkAgg(window.fig, master = window)
    window.canvas.draw()
    window.canvas.get_tk_widget().pack(pady = 40)
    
    window.toolbar = NavigationToolbar2Tk(window.canvas, window, pack_toolbar = False)
    window.toolbar.update()
    window.toolbar.pack()

def root(user_input):
    x_list = np.linspace(-50, 50, 1001)
    y_list = []

    sterile_function = corrector(user_input)
    
    border()

    for i in x_list:
        try:
            result = eval(sterile_function.replace("x", "(" + str(i) + ")"))
            y_list.append(result)
            print(f"ƒ({i}) = {result}")
        except ZeroDivisionError:
            y_list.append(float('inf'))
            print(f"ƒ({i}) = N/A")
        except Exception as a: 
            print(f"Error: {a}")

    border()
    
    return x_list, y_list

def corrector(tb_modified):
    tb_modified = tb_modified.lower()
    update_dictionary = {
        r"\barcsinh\b": "np.arcsinh",
        r"\barccosh\b": "np.arccosh",
        r"\barctanh\b": "np.arctanh",
        
        r"\barcsin\b": "np.arcsin",
        r"\barccos\b": "np.arccos",
        r"\barctan\b": "np.arctan",
        r"\barctan2\b": "np.arctan2",
        
        r"\bsinh\b": "np.sinh",
        r"\bcosh\b": "np.cosh",
        r"\btanh\b": "np.tanh",
        
        r"\bsin\b": "np.sin",
        r"\bcos\b": "np.cos",
        r"\btan\b": "np.tan",
        
        r"\blog\b": "np.log",
        r"\blog10\b": "np.log10",
        r"\blog1p\b": "np.log1p",
        r"\blog2\b": "np.log2",
        r"\blogaddexp\b": "np.logaddexp",
        r"\blogaddexp2\b": "np.logaddexp2",
        
        r"\bsqrt\b": "np.sqrt",
        r"\babs\b": "np.abs",
        
        r"\bpi\b": "np.pi",
    }

    for old, new in update_dictionary.items():
        tb_modified = re.sub(old, new, tb_modified)

    return tb_modified

# Just for beutifying the debugging process
def border():
   return print("\n" + 10 * "-" + "\n")

app_start()