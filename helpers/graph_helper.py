import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
import pyqtgraph as pg
from math import cos
from models.EquationFunctions import EquationEvaluator
from numpy import linspace

class PyQtGraphWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.plot_widget = pg.PlotWidget()
        self.layout.addWidget(self.plot_widget)
        
        self.plot_widget.setBackground('#2c313c')
        axis_pen = pg.mkPen(color='#b5b5b5', width=2)
        self.plot_widget.getAxis('bottom').setPen(axis_pen)
        self.plot_widget.getAxis('left').setPen(axis_pen) 
        
        self.plot_widget.getAxis('bottom').setTextPen(pg.mkPen(color='#FFFFFF'))  
        self.plot_widget.getAxis('left').setTextPen(pg.mkPen(color='#FFFFFF')) 
        self.stop = 100
        self.num_points = 1000
        
    def paint_equation(self, equation):
        self.plot_widget.clear()
        
        if EquationEvaluator(equation, 1) is None:
            return None

        start = -100 if EquationEvaluator(equation, -1) is not None else 0
        x = linspace(start, self.stop, self.num_points)
        y = [EquationEvaluator(equation, number) for number in x]

        self.plot_widget.plot(x, y, pen=pg.mkPen(color='#fff', width=5), symbol='o', symbolBrush='#4864b4')

        roots_x = []
        roots_y = []
        for i in range(len(x) - 1):
            if y[i] * y[i + 1] <= 0:
                root_x = (x[i] + x[i + 1]) / 2 
                root_y = EquationEvaluator(equation, root_x)
                roots_x.append(root_x)
                roots_y.append(root_y)
        if roots_x:
            self.plot_widget.plot(
                roots_x,
                roots_y,
                pen=None,
                symbol='o',
                symbolSize=10,
                symbolBrush='#b94946',
                symbolPen=pg.mkPen(color='#000', width=1) 
            )
        self.plot_widget.setRange(xRange=[3, 20])

