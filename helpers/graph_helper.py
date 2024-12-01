import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
import pyqtgraph as pg
from math import cos
from models.EquationFunctions import EquationEvaluator

class PyQtGraphWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.plot_widget = pg.PlotWidget()
        self.layout = QVBoxLayout(self)
        self.plot_widget = pg.PlotWidget()
        self.layout.addWidget(self.plot_widget)
        self.plot_widget.setBackground('#2c313c')

    def paint_equation(self,equation):
        self.plot_widget.clear()
        if EquationEvaluator(equation,1) is None:
            print('ERROR')
            return None
        x = [number for number in range(-100 if EquationEvaluator(equation, -1) is not None else 0, 100)] 
        y = [EquationEvaluator(equation,number) for number in x]
        self.plot_widget.plot(x,y,pen=pg.mkPen(color='#ec134e',width=5),symbol='o',symbolBrush='b')
