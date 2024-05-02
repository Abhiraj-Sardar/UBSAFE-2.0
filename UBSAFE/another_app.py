import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class AnotherPage(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Another Page")
        self.setGeometry(50, 50, 800, 600)
        
        label = QLabel("This is another page.", self)
        label.setGeometry(100, 100, 400, 100)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnotherPage()
    window.show()
    sys.exit(app.exec_())
