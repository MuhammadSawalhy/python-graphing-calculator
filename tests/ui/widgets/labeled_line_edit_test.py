from PySide2.QtWidgets import QApplication

from ui.widgets.labeled_line_edit import LabeledLineEdit


def test_ui(qtbot):
    # Create your app object and show it
    labeled_input = LabeledLineEdit("Label: ")
    qtbot.addWidget(labeled_input)

    # Check that the app behaves as expected
    assert labeled_input.label.text() == "Label: "

