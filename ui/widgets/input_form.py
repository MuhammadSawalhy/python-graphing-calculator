from PySide2.QtCore import QRegExp
from PySide2.QtGui import QDoubleValidator, QValidator
from PySide2.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout, QWidget
from ui.widgets.labeled_line_edit import LabeledLineEdit


class InputForm(QWidget):
    def __init__(self, plot):
        QWidget.__init__(self)

        main_layout = QVBoxLayout()

        self.expression = LabeledLineEdit("Function: ")
        self.expression.input.setPlaceholderText(
            "Enter a mathematical expression")
        self.expression.input.returnPressed.connect(plot)
        main_layout.addWidget(self.expression)

        # Create the limits of x inputs
        self.x_start = LabeledLineEdit("Min x: ")
        self.x_end = LabeledLineEdit("Max x: ")
        x_limits_hbox = QHBoxLayout()
        x_limits_hbox.addWidget(self.x_start)
        x_limits_hbox.addWidget(self.x_end)
        main_layout.addLayout(x_limits_hbox)

        # Create the button to plot the function
        plot_button = QPushButton("Plot")
        plot_button.clicked.connect(plot)
        main_layout.addWidget(plot_button)

        # Set intial values and and constraints of the inputs
        self.expression.input("x ^ 2")
        self.x_start.input.setText("-10")
        self.x_end.input.setText("10")
        self.x_start.input.setValidator(QDoubleValidator())
        self.x_end.input.setValidator(QDoubleValidator())

        # Set a fixed width for the labels
        self.expression.label.setFixedWidth(60)
        self.x_start.label.setFixedWidth(60)
        self.x_end.label.setFixedWidth(60)

        self.setFixedHeight(140)
        self.setLayout(main_layout)

    def get_expression(self) -> str:
        return self.expression.input.text()

    def get_x_start(self):
        return float(self.x_start.input.text())

    def get_x_end(self):
        return float(self.x_end.input.text())

