import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QProgressBar, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer, QObject, pyqtSignal




class LogoPage(QMainWindow):
    showAnotherPageSignal = pyqtSignal()
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Logo Page")
        self.setGeometry(50, 50, 1200, 680)
        self.setStyleSheet("background-color: #f4f4f4;")
        
        # Load your logo image
        logo = QLabel(self)
        pixmap = QPixmap("pics/logo.png")  # Replace with your logo file path
        logo.setPixmap(pixmap)
        logo.setAlignment(Qt.AlignCenter)
        
        # Center the logo in the window
        logo.setGeometry((self.width() - pixmap.width()) // 2, (self.height() - pixmap.height()) // 2, pixmap.width(), pixmap.height())
        
        # Create a progress bar
        progress_bar = QProgressBar(self)
        progress_bar.setGeometry(340, pixmap.height() + 50, pixmap.width(), 20)
        progress_bar.setStyleSheet("QProgressBar {"
                                   "    border: 1px solid grey;"
                                   "    border-radius: 3px;"
                                   "    background-color: white;"
                                   "}"
                                   "QProgressBar::chunk {"
                                   "    background-color: blue;"
                                   "    border-radius: 2px;"
                                   "}")
        progress_bar.setTextVisible(False)
        
        # Create a timer to update the progress bar
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.progress_value = 0
        self.timer.start(100)  # Update every 100 milliseconds


    def update_progress(self):
        # Update the progress bar value
        self.progress_value += 4
        if self.progress_value > 100:
            self.progress_value = 0
            self.showAnotherPageSignal.emit()
        self.findChild(QProgressBar).setValue(self.progress_value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LogoPage()
    def open_another_page():
        from another_app import AnotherPage  # Import the class only when needed
        app2 = QApplication(sys.argv)
        window2 = AnotherPage()
        window2.show()
        sys.exit(app2.exec_())
    window.showAnotherPageSignal.connect(open_another_page)
    window.show()
    sys.exit(app.exec_()) 

