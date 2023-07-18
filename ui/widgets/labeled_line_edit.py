from PySide2.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QWidget


class LabeledLineEdit(QWidget):
    def __init__(self, label: str, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        self.label = QLabel(label)
        self.input = QLineEdit()

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.input)
        self.setLayout(main_layout)

