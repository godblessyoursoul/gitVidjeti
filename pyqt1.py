# zadanie 4
import json
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QSpinBox, QLabel, QHBoxLayout
class Weather:
    def __init__(self, city, temperature, unit):
        self.city = city
        self.temperature = temperature
        self.unit = unit
def load_weather_data(file_path):
    with open(file_path, encoding="ISO-8859-1") as file:
        data = json.load(file)
    return [Weather(item["city"], item["temperature"], item["unit"]) for item in data]
class WeatherApp(QWidget):
    def __init__(self, weather_data):
        super().__init__()
        self.setWindowTitle("инфа о погоде")
        self.setGeometry(100, 100, 600, 400)
        self.weather_data = weather_data
        self.filtered_data = weather_data
        # таблица
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["город", "температура", "градусная мера"])
        # виджеты для фильтрации
        self.min_temp_spinbox = QSpinBox()
        self.min_temp_spinbox.setRange(-100, 100)
        self.min_temp_spinbox.setValue(-100)
        self.min_temp_spinbox.valueChanged.connect(self.filter_data)
        self.max_temp_spinbox = QSpinBox()
        self.max_temp_spinbox.setRange(-100, 100)
        self.max_temp_spinbox.setValue(100)
        self.max_temp_spinbox.valueChanged.connect(self.filter_data)
        # меточки
        min_label = QLabel("Мин. температура:")
        max_label = QLabel("Макс. температура:")
        # макетик для фильтров
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(min_label)
        filter_layout.addWidget(self.min_temp_spinbox)
        filter_layout.addWidget(max_label)
        filter_layout.addWidget(self.max_temp_spinbox)
        # основной макет
        layout = QVBoxLayout()
        layout.addLayout(filter_layout)
        layout.addWidget(self.table)
        self.setLayout(layout)
        self.update_table()
    def update_table(self):
        # обновление таблицы с текущими данными
        self.table.setRowCount(len(self.filtered_data))
        for row, weather in enumerate(self.filtered_data):
            self.table.setItem(row, 0, QTableWidgetItem(weather.city))
            self.table.setItem(row, 1, QTableWidgetItem(str(weather.temperature)))
            self.table.setItem(row, 2, QTableWidgetItem(weather.unit))
    def filter_data(self):
        # фильтр данных на основе qbox
        min_temp = self.min_temp_spinbox.value()
        max_temp = self.max_temp_spinbox.value()
        if min_temp == -100 and max_temp == 100:
            # если значения по умолчанию, показываем все данные
            self.filtered_data = self.weather_data
        else:
            self.filtered_data = [
                weather for weather in self.weather_data
                if min_temp <= weather.temperature <= max_temp
            ]
        self.update_table()
if __name__ == "__main__":
    import sys
    weather_data = load_weather_data("data.json")
    app = QApplication(sys.argv)
    window = WeatherApp(weather_data)
    window.show()
    sys.exit(app.exec_())
