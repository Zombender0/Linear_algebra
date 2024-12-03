import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
import pyqtgraph as pg
from math import cos
from models.EquationFunctions import EquationEvaluator
from numpy import linspace
class PyQtGraphWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.plot_widget = pg.PlotWidget()
        self.layout = QVBoxLayout(self)
        self.plot_widget = pg.PlotWidget()
        self.layout.addWidget(self.plot_widget)
        self.plot_widget.setBackground('#2c313c')
        self.stop = 100
        self.num_points = 1000
    def paint_equation(self,equation):
        self.plot_widget.clear()
        
        if EquationEvaluator(equation, 1) is None:
            print('ERROR')
            return None
        start = -100 if EquationEvaluator(equation, -1) is not None else 0
        
        x = linspace(start, self.stop, self.num_points)
        
        y = [EquationEvaluator(equation, number) for number in x]
        self.plot_widget.plot(x, y, pen=pg.mkPen(color='#ec134e', width=5), symbol='o', symbolBrush='b')
