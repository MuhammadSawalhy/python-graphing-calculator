import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import matplotlib.pyplot as plt
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

        # Create the input field for the function
        self.function_input = QLineEdit()
        self.function_input.setPlaceholderText("Enter a mathematical expression")
        main_layout.addWidget(self.function_input)

        # Create the button to plot the function
        plot_button = QPushButton("Plot")
        plot_button.clicked.connect(self.plot_function)
        main_layout.addWidget(plot_button)

        # Create the matplotlib figure and canvas
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        main_layout.addWidget(self.canvas)

        # Set the main widget as the central widget
        self.setCentralWidget(main_widget)

    def plot_function(self):
        # Clear the current plot
        self.figure.clear()

        # Get the mathematical expression from the input field
        expression = self.function_input.text()

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
