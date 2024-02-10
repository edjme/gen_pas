import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
import random
import string


class PasswordGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Генератор паролей')

        # Добавляем виджеты
        self.label_length = QLabel('Длина пароля:')
        self.edit_length = QLineEdit()

        self.checkbox_uppercase = QCheckBox('Использовать буквы верхнего регистра')
        self.checkbox_lowercase = QCheckBox('Использовать буквы нижнего регистра')
        self.checkbox_digits = QCheckBox('Использовать цифры')
        self.checkbox_special_chars = QCheckBox('Использовать специальные символы')

        self.generate_button = QPushButton('Сгенерировать пароль')
        self.generate_button.clicked.connect(self.generate_password)

        # Создаем компоновщик интерфейса
        layout = QVBoxLayout()
        layout.addWidget(self.label_length)
        layout.addWidget(self.edit_length)
        layout.addWidget(self.checkbox_uppercase)
        layout.addWidget(self.checkbox_lowercase)
        layout.addWidget(self.checkbox_digits)
        layout.addWidget(self.checkbox_special_chars)
        layout.addWidget(self.generate_button)

        self.setLayout(layout)

    def generate_password(self):
        length = int(self.edit_length.text()) if self.edit_length.text().isdigit() else 0
        use_uppercase = self.checkbox_uppercase.isChecked()
        use_lowercase = self.checkbox_lowercase.isChecked()
        use_digits = self.checkbox_digits.isChecked()
        use_special_chars = self.checkbox_special_chars.isChecked()

        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)

        if password:
            QMessageBox.information(self, 'Сгенерированный пароль', f'Ваш сгенерированный пароль: {password}')


def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        QMessageBox.warning(None, 'Ошибка', 'Выберите хотя бы один тип символов для пароля.')
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec_())
