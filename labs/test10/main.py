import sys

from PyQt6.QtWidgets import QApplication

from gui import GUI

def main():
    application = QApplication(sys.argv)
    window = GUI()
    window.show()
    application.exec()

if __name__ == "__main__":
    main()
