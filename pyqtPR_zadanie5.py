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
