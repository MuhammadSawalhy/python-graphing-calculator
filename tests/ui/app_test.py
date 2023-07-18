import pytest
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMessageBox
from ui.app import App


@pytest.fixture
def app(qtbot):
    app = App()
    qtbot.addWidget(app)
    yield app


def test_message_box_is_displayed(app, qtbot):
    # TODO: test message boxes
    qtbot.keyClicks(app.input_form.expression, "x * 2")
    qtbot.mouseClick(app.input_form.plot_button, Qt.LeftButton)

