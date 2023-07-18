from PySide2.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


class InputForm(QWidget):
    def __init__(self, plot):
        super().__init__()

        main_layout = QVBoxLayout(self)
        input_hbox = QHBoxLayout()

        # Create the label for the input field
        label = QLabel("Function: ")
        input_hbox.addWidget(label)

        # Create the input field for the function
        self.function_input = QLineEdit()
        self.function_input.setPlaceholderText(
            "Enter a mathematical expression")
        self.function_input.returnPressed.connect(plot)
        input_hbox.addWidget(self.function_input)

        main_layout.addLayout(input_hbox)

        # Create the button to plot the function
        plot_button = QPushButton("Plot")
        plot_button.clicked.connect(plot)
        main_layout.addWidget(plot_button)

        self.setLayout(main_layout)

    def get_expression(self):
        return self.function_input.text()
