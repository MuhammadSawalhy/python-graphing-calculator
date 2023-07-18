import sys
from PySide2.QtWidgets import QApplication
from ui.app import App


if __name__ == "__main__":
    # Create the application and main window
    app = QApplication(sys.argv)
    main_window = App()
    main_window.show()

    # Start the event loop
    sys.exit(app.exec_())
