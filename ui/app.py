from ui.widgets.input_form import InputForm
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

from utils.input import convert_expression


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide2 Matplotlib Example")

        # Create the main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        self.input_form = InputForm(self.plot)
        main_layout.addWidget(self.input_form)

        # Create the matplotlib figure and canvas
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        main_layout.addWidget(self.canvas)

        # Set the main widget as the central widget
        self.setCentralWidget(main_widget)

    def plot(self):
        expression = self.input_form.get_expression()
        converted = convert_expression(expression)

        # Clear the current plot
        self.figure.clear()

        # Evaluate the expression over a range of x values
        x = np.linspace(self.input_form.get_x_start(),
                        self.input_form.get_x_end(), 1000)
        y = eval(converted)

        # Create a subplot and plot the expression
        ax = self.figure.add_subplot(111)
        ax.plot(x, y)

        # Set the title and axis labels
        ax.set_title(expression)
        ax.set_xlabel("x")
        ax.set_ylabel("y")

        # Redraw the canvas
        self.canvas.draw()

