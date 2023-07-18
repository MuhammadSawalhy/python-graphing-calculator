import sys
from input_form import InputForm
from PySide2.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np


class MainWindow(QMainWindow):
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

        # Clear the current plot
        self.figure.clear()

        # Evaluate the expression over a range of x values
        x = np.linspace(-10, 10, 1000)
        y = eval(expression)

        # Create a subplot and plot the expression
        ax = self.figure.add_subplot(111)
        ax.plot(x, y)

        # Set the title and axis labels
        ax.set_title(expression)
        ax.set_xlabel("x")
        ax.set_ylabel("y")

        # Redraw the canvas
        self.canvas.draw()


if __name__ == "__main__":
    # Create the application and main window
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()

    # Start the event loop
    sys.exit(app.exec_())
