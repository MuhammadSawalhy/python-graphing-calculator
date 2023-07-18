from PySide2.QtGui import QDoubleValidator
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
        self.x_start.input.returnPressed.connect(plot)
        self.x_end.input.returnPressed.connect(plot)
        x_limits_hbox = QHBoxLayout()
        x_limits_hbox.addWidget(self.x_start)
        x_limits_hbox.addWidget(self.x_end)
        main_layout.addLayout(x_limits_hbox)

        # Create the button to plot the function
        self.plot_button = QPushButton("Plot")
        self.plot_button.clicked.connect(plot)
        main_layout.addWidget(self.plot_button)

        # Set intial values and and constraints of the inputs
        self.expression.input.setText("x ^ 2")
        self.x_start.input.setText("-10")
        self.x_end.input.setText("10")
        self.x_start.input.setValidator(QDoubleValidator())
        self.x_end.input.setValidator(QDoubleValidator())

        self.setFixedHeight(170)
        self.setLayout(main_layout)

    def get_expression(self):
        return self.expression.input.text()

    def get_x_start(self):
        return self.x_start.input.text()

    def get_x_end(self):
        return self.x_end.input.text()

