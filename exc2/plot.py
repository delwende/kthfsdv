import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import math
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
class Plot:
    def __init__(self, xmin, xmax, ymin, ymax, grid_color, root):

        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax

       
        frame = tk.Frame(root)
	
        fig = Figure()
        self.ax = fig.add_subplot(111)
        self.ax.grid(color=grid_color)
        self.ax.set_xlim(self.xmin, self.xmax)
        self.ax.set_ylim(self.ymin, self.ymax)

        self.canvas = FigureCanvasTkAgg(fig,master=root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

        frame.pack()

    def funct_h(self, t_values):
        lamda = [5*math.sin(2*math.pi*1*i) for i in t_values]
        h = [3*math.pi*math.exp(i) for i in lamda]

        return h

    def plot_result(self, t_values):
        self.ax.plot(t_values, self.funct_h(t_values), "b")

    
    


if __name__ == '__main__':
    t_values = np.linspace(-390, 400, 200)
    root = tk.Tk()
    plot = Plot(-600, 500, -600, 800, "r", root)
    plot.plot_result(t_values)

    root.mainloop()


