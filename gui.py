from PyQt5 import QtWidgets
from cryptography.fernet import Fernet

class CryptoApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CryptoSuit")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: orange;")

        self.text_edit_input = QtWidgets.QTextEdit(self)
        self.text_edit_input.setGeometry(50, 50, 300, 400)
        self.text_edit_input.setStyleSheet("background-color: white; font-size: 16px;")

        self.text_edit_output = QtWidgets.QTextEdit(self)
        self.text_edit_output.setGeometry(450, 50, 300, 400)
        self.text_edit_output.setStyleSheet("background-color: white; font-size: 16px;")

        self.button_encrypt = QtWidgets.QPushButton("Encrypt", self)
        self.button_encrypt.setGeometry(50, 480, 100, 50)
        self.button_encrypt.setStyleSheet("background-color: green; font-size: 16px;")
        self.button_encrypt.clicked.connect(self.encrypt)

        self.button_decrypt = QtWidgets.QPushButton("Decrypt", self)
        self.button_decrypt.setGeometry(200, 480, 100, 50)
        self.button_decrypt.setStyleSheet("background-color: green; font-size: 16px;")
        self.button_decrypt.clicked.connect(self.decrypt)

    def encrypt(self):
        plain_text = self.text_edit_input.toPlainText().encode()
        key = Fernet.generate_key()
        fernet = Fernet(key)
        encrypted_text = fernet.encrypt(plain_text)
        self.text_edit_output.setPlainText(str(encrypted_text, 'utf-8'))

    def decrypt(self):
        encrypted_text = self.text_edit_input.toPlainText().encode()
        key = Fernet.generate_key()
        fernet = Fernet(key)
        decrypted_text = fernet.decrypt(encrypted_text)
        self.text_edit_output.setPlainText(str(decrypted_text, 'utf-8'))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    crypto_app = CryptoApp()
    crypto_app.show()
    sys.exit(app.exec_())
