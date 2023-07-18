from ui.widgets.input_form import InputForm
from PySide2.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

from utils.input import convert_expression, validate_expression, validate_x_limits


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
        x_start = self.input_form.get_x_start()
        x_end = self.input_form.get_x_end()

        if not self.validate(expression, x_start, x_end):
            return

        # Clear the current plot
        self.figure.clear()

        # Evaluate the expression over a range of x values
        x = np.linspace(float(x_start), float(x_end), 1000)
        y = eval(convert_expression(expression))

        # Create a subplot and plot the expression
        ax = self.figure.add_subplot(111)
        ax.plot(x, y)

        # Set the title and axis labels
        ax.set_title(expression)
        ax.set_xlabel("x")
        ax.set_ylabel("y")

        # Redraw the canvas
        self.canvas.draw()

    def validate(self, expression: str, x_start: str, x_end: str) -> bool:
        error_msg = validate_expression(expression)
        if error_msg:
            self.display_error_dialog("Invalid expression", error_msg)
            return False

        error_msg = validate_x_limits(x_start, x_end)
        if error_msg:
            self.display_error_dialog("Invalid x limits", error_msg)
            return False

        return True

    def display_error_dialog(self, title: str, msg: str):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Information)
        error_dialog.setWindowTitle(title)
        error_dialog.setText(title)
        error_dialog.setInformativeText(msg)
        error_dialog.setStandardButtons(QMessageBox.Ok)
        error_dialog.exec()
