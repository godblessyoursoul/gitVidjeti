import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QCheckBox, QRadioButton, QVBoxLayout, QHBoxLayout, QGroupBox

class textchanger(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Текст для отображения", self)
        # Цвет текста
        self.color_combo = QComboBox(self)
        self.color_combo.addItems(["Красный", "Зеленый", "Синий"])
        self.color_combo.currentIndexChanged.connect(self.update_text)
        # Стиль текста
        self.bold_checkbox = QCheckBox("Жирный", self)
        self.bold_checkbox.stateChanged.connect(self.update_text)
        self.italic_checkbox = QCheckBox("Курсив", self)
        self.italic_checkbox.stateChanged.connect(self.update_text)
        # Размер текста
        self.size_group = QGroupBox("Размер текста", self)
        self.size_layout = QVBoxLayout()
        self.radio_small = QRadioButton("Маленький", self)
        self.radio_medium = QRadioButton("Средний")
        self.radio_large = QRadioButton("Большой")
        self.radio_small.setChecked(True)
        self.size_layout.addWidget(self.radio_small)
        self.size_layout.addWidget(self.radio_medium)
        self.size_layout.addWidget(self.radio_large)
        self.size_group.setLayout(self.size_layout)
        self.radio_small.toggled.connect(self.update_text)
        self.radio_medium.toggled.connect(self.update_text)
        self.radio_large.toggled.connect(self.update_text)
        # Компоновка
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.color_combo)
        layout.addWidget(self.bold_checkbox)
        layout.addWidget(self.italic_checkbox)
        layout.addWidget(self.size_group)
        self.setLayout(layout)
        self.update_text()  # Инициализация текста
    def update_text(self):
        # Получаем текущие настройки
        color = self.color_combo.currentText().lower()
        is_bold = self.bold_checkbox.isChecked()
        is_italic = self.italic_checkbox.isChecked()
        font_size = 10  # По умолчанию
        if self.radio_medium.isChecked():
            font_size = 14
        elif self.radio_large.isChecked():
            font_size = 18
        # Устанавливаем шрифт
        font = self.label.font()
        font.setPointSize(font_size)
        font.setBold(is_bold)
        font.setItalic(is_italic)
        self.label.setFont(font)
        # Устанавливаем цвет текста
        color_dict = {
            "красный": "red",
            "зеленый": "green",
            "синий": "blue"
        }
        self.label.setStyleSheet(f"color: {color_dict[color]};")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = textchanger()
    window.setWindowTitle("Настройка отображения текста")
    window.show()
    sys.exit(app.exec_())