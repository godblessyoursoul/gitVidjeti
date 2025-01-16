import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.label = QLabel('0', self)
        self.button = QPushButton('Нажми меня', self)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.button.clicked.connect(self.increment_counter)
        self.setWindowTitle('Счетчик нажатий')
        self.show()
    def increment_counter(self):
        self.counter += 1
        self.label.setText(str(self.counter))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())