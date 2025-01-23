import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QVBoxLayout, QHBoxLayout, QRadioButton, QPushButton

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('инфа о челике')
        self.surname_input = QLineEdit(self)
        self.name_input = QLineEdit(self)
        self.otchestvo_input = QLineEdit(self)
        self.city_combo = QComboBox(self)
        self.city_combo.addItems(['москоу', 'питер', 'абакан', 'красноярск'])
        self.male_radio = QRadioButton('мужик', self)
        self.female_radio = QRadioButton('женщина', self)
        self.submit_button = QPushButton('Отправить', self)
        self.result_label = QLabel('', self)
        layout = QVBoxLayout()
        layout.addWidget(QLabel('фамилия:'))
        layout.addWidget(self.surname_input)
        layout.addWidget(QLabel('имя:'))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel('отчество:'))
        layout.addWidget(self.otchestvo_input)
        layout.addWidget(QLabel('город:'))
        layout.addWidget(self.city_combo)
        layout.addWidget(QLabel('пол:'))
        layout.addWidget(self.male_radio)
        layout.addWidget(self.female_radio)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.result_label)
        self.setLayout(layout)
        self.submit_button.clicked.connect(self.show_info)
    def show_info(self):
        surname = self.surname_input.text()
        name = self.name_input.text()
        otchestvo = self.otchestvo_input.text()
        city = self.city_combo.currentText()
        gender = 'мужик' if self.male_radio.isChecked() else 'женщина' if self.female_radio.isChecked() else 'Не указан'
        self.result_label.setText(f'фио: {surname} {name} {otchestvo}, город: {city}, пол: {gender}')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
