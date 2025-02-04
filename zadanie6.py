import sys
import json
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QComboBox, QSpinBox, QRadioButton, QHBoxLayout, QButtonGroup

class WeatherApp(QWidget):
    def __init__(self, weather_data):
        super().__init__()
        self.setWindowTitle("инфа о погоде")
        self.setGeometry(100, 100, 600, 400)
        # сохранение исходных данных
        self.weather_data = weather_data
        # создание таблицы
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["город", "темпа", "градусная мера"])
        # создание QComboBox
        self.combo_box = QComboBox()
        self.combo_box.addItems(["всё", "минималка", "максималка", "средняя"])
        self.combo_box.currentIndexChanged.connect(self.filter_data)
        # создание QSpinBox для ввода порога температуры
        self.spin_box = QSpinBox()
        self.spin_box.setRange(-100, 100)  # устанавливаем диапазон температур
        self.spin_box.setValue(0)  # устанавливаем начальное значение
        self.spin_box.valueChanged.connect(self.filter_by_temperature)
        # создание QRadioButton для выбора фильтрации
        self.radio_above = QRadioButton("Выше")
        self.radio_below = QRadioButton("Ниже")
        # группировка QRadioButton
        self.radio_group = QButtonGroup()
        self.radio_group.addButton(self.radio_above)
        self.radio_group.addButton(self.radio_below)
        self.radio_above.toggled.connect(self.filter_by_temperature)
        self.radio_below.toggled.connect(self.filter_by_temperature)
        # расположение виджетов
        layout = QVBoxLayout()
        # создаем горизонтальный layout для QSpinBox и QRadioButton
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(self.spin_box)
        filter_layout.addWidget(self.radio_above)
        filter_layout.addWidget(self.radio_below)
        layout.addWidget(self.combo_box)
        layout.addLayout(filter_layout)
        layout.addWidget(self.table)
        self.setLayout(layout)
        # отображение всех данных по умолчанию
        self.display_data(self.weather_data)

    def display_data(self, data):
        # проверка на пустые данные
        if not data:
            self.table.setRowCount(0)
            return
        # отображаем данные в таблице
        self.table.setRowCount(len(data))
        for row, weather in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(weather["city"]))
            self.table.setItem(row, 1, QTableWidgetItem(str(weather["temperature"])))
            self.table.setItem(row, 2, QTableWidgetItem(weather["unit"]))

    def filter_data(self):
        # фильтрация данных на основе combobox
        selected_option = self.combo_box.currentText()
        if selected_option == "всё":
            self.display_data(self.weather_data)
        elif selected_option == "минималка":
            min_temp = min(self.weather_data, key=lambda x: x["temperature"])
            self.display_data([min_temp])
        elif selected_option == "максималка":
            max_temp = max(self.weather_data, key=lambda x: x["temperature"])
            self.display_data([max_temp])
        elif selected_option == "средняя":
            avg_temp = sum([x["temperature"] for x in self.weather_data]) / len(self.weather_data)
            avg_data = [{"city": "Общая", "temperature": round(avg_temp, 2), "unit": "C"}]
            self.display_data(avg_data)
    def filter_by_temperature(self):
        # получаем значение порога из QSpinBox
        threshold = self.spin_box.value()
        # фильтрация данных на основе выбранного QRadioButton
        if self.radio_above.isChecked():
            filtered_data = [weather for weather in self.weather_data if weather["temperature"] > threshold]
        elif self.radio_below.isChecked():
            filtered_data = [weather for weather in self.weather_data if weather["temperature"] < threshold]
        else:
            filtered_data = self.weather_data
        # отображение отфильтрованных данных
        self.display_data(filtered_data)
def load_weather_data(file_path):
    with open(file_path, encoding="ISO-8859-1") as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    weather_data = load_weather_data("data.json")
    app = QApplication(sys.argv)
    window = WeatherApp(weather_data)
    window.show()
    sys.exit(app.exec_())
