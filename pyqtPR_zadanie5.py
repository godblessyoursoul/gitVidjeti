import json
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QComboBox
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
        self.table.setHorizontalHeaderLabels(["Город", "Температура", "Градусная мера"])
        # создание QComboBox
        self.combo_box = QComboBox()
        self.combo_box.addItems(["всё", "минималка", "максималка", "средняя"])
        self.combo_box.currentIndexChanged.connect(self.filter_data)
        # расположение виджетов
        layout = QVBoxLayout()
        layout.addWidget(self.combo_box)
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
            avg_data = [{"city": "общая", "temperature": round(avg_temp, 2), "unit": "C"}]
            self.display_data(avg_data)
if __name__ == "__main__":
    import sys
    # пример данных
    weather_data = [
        {"city": "Moscow", "temperature": -5, "unit": "C"},
        {"city": "Tokyo", "temperature": 8, "unit": "C"},
        {"city": "Berlin", "temperature": 12, "unit": "C"},
        {"city": "Saint Petersburg", "temperature": 4, "unit": "C"},
        {"city": "Boston", "temperature": 15, "unit": "C"},
    ]
    app = QApplication(sys.argv)
    window = WeatherApp(weather_data)
    window.show()
    sys.exit(app.exec_())