from PySide2.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QWidget


class LabeledLineEdit(QWidget):
    def __init__(self, label: str, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        self.label = QLabel(label)
        self.input = QLineEdit()

        # Set size
        self.label.setFixedWidth(60)
        self.input.setFixedHeight(40)

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.input)
        self.setLayout(main_layout)

