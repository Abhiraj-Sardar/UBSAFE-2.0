import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFrame
from PyQt5.QtGui import QPixmap

class SignInApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set window size and background color
        self.setGeometry(50, 50, 1200, 680)
        self.setWindowTitle('UBSAFE')
        self.setStyleSheet("background-color: white;")

        # Create and set the image on the left half
        # Replace 'image_path' with the actual image path
        image_frame = QFrame(self)
        image_frame.setGeometry(0, 0, 600, 680)
        image_frame.setStyleSheet("background-image: url('pics/signup.jpg'); background-size: cover;")

        # Create Sign In form on the right half
        form_label = QLabel('Sign In', self)
        form_label.setGeometry(650, 30, 200, 40)
        form_label.setStyleSheet("font-size: 30px;")

        sub_label = QLabel('Your Security, Your Way - Start Now with UBSAFE!', self)
        sub_label.setGeometry(650, 70, 500, 50)
        sub_label.setStyleSheet("font-size: 15px;")

        placeholders = ["Username", "Password", "Employee ID", "Phone", "Email", "Admin Email"]
        input_fields = []

        # Create input fields without borders and placeholders
        for i, placeholder in enumerate(placeholders):
            input_field = QLineEdit(self)
            input_field.setGeometry(650, 150 + i * 40, 250, 30)
            input_field.setPlaceholderText(placeholder)
            input_field.setStyleSheet("border: none; padding: 5px; font-size: 16px;")
            input_fields.append(input_field)

        submit_button = QPushButton('Get OTP', self)
        submit_button.setGeometry(860, 400, 100, 40)
        submit_button.setStyleSheet("background-color: #007BFF; color: white; border: none; border-radius: 5px; padding: 10px; font-size: 16px;")

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SignInApp()
    sys.exit(app.exec_())
