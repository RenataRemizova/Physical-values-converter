import sys

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QLineEdit, QLabel, QToolBar, QListWidgetItem

# table for convert
table_convert_width = [[1, 0.1, 0.01, 0.001, 0.000001],
                       [10, 1, 0.1, 0.01, 0.00001],
                       [100, 10, 1, 0.1, 0.0001],
                       [1000, 100, 10, 1, 0.001],
                       [1000000, 100000, 10000, 1000, 1]]

table_convert_weight = [[1, 0.001, 0.000001, 0.0000001, 0.000000001],
                        [1000, 1, 0.001, 0.00001, 0.000001],
                        [1000000, 1000, 1, 0.01, 0.001],
                        [10000000, 100000, 100, 1, 0.01],
                        [1000000000, 1000000, 1000, 10, 1]]

table_convert_time = [[1, 0.0166667, 0.000277778],
                      [60, 1, 0.0166667],
                      [3600, 60, 1]]


# link new windows
def func_weight():
    widget.addWidget(Weight())
    widget.setCurrentIndex(widget.currentIndex() + 1)


def func_time():
    widget.addWidget(Time())
    widget.setCurrentIndex(widget.currentIndex() + 1)


def func_temperature():
    widget.addWidget(Temperature())
    widget.setCurrentIndex(widget.currentIndex() + 1)


def func_speed():
    widget.addWidget(Speed())
    widget.setCurrentIndex(widget.currentIndex() + 1)


def func_width():
    widget.addWidget(Width())
    widget.setCurrentIndex(widget.currentIndex() + 1)


# windows
class Width(QDialog):
    def __init__(self):
        super(Width, self).__init__()
        loadUi("UI/converter_width.ui", self)
        self.units = ["мм", "см", "дм", "м", "км"]

        self.input_units.addItems(self.units)
        self.output_units.addItems(self.units)

        self.weight.clicked.connect(func_weight)
        self.time.clicked.connect(func_time)
        self.temperature.clicked.connect(func_temperature)
        self.speed.clicked.connect(func_speed)
        self.show_result.clicked.connect(self.output)

    def get_value(self):
        try:
            in_unit = self.input_units.currentText()
            on_unit = self.output_units.currentText()
            in_index = self.units.index(in_unit)
            on_index = self.units.index(on_unit)
            in_value = float(self.value_input.text())
            return in_value, in_index, on_index
        except ValueError:
            print("Error")

    def output(self):
        in_value, in_index, on_index = self.get_value()
        result = table_convert_width[in_index][on_index] * in_value
        self.result.setText(str(result))


class Weight(QDialog):
    def __init__(self):
        super(Weight, self).__init__()
        loadUi("UI/converter_weight.ui", self)
        self.units = ["мг", "г", "кг", "ц", "т"]
        self.input_units.addItems(self.units)
        self.output_units.addItems(self.units)

        self.time.clicked.connect(func_time)
        self.temperature.clicked.connect(func_temperature)
        self.speed.clicked.connect(func_speed)
        self.width.clicked.connect(func_width)
        self.show_result.clicked.connect(self.output)

    def get_value(self):
        try:
            in_unit = self.input_units.currentText()
            on_unit = self.output_units.currentText()
            in_index = self.units.index(in_unit)
            on_index = self.units.index(on_unit)
            in_value = float(self.value_input.text())
            return in_value, in_index, on_index
        except ValueError:
            print("Error")

    def output(self):
        in_value, in_index, on_index = self.get_value()
        result = table_convert_weight[in_index][on_index] * in_value
        self.result.setText(str(result))


class Time(QDialog):
    def __init__(self):
        super(Time, self).__init__()
        loadUi("UI/converter_time.ui", self)
        self.units = ["с", "мин", "ч"]
        self.input_units.addItems(self.units)
        self.output_units.addItems(self.units)

        self.weight.clicked.connect(func_weight)
        self.temperature.clicked.connect(func_temperature)
        self.speed.clicked.connect(func_speed)
        self.width.clicked.connect(func_width)
        self.show_result.clicked.connect(self.output)

    def get_value(self):
        try:
            in_unit = self.input_units.currentText()
            on_unit = self.output_units.currentText()
            in_index = self.units.index(in_unit)
            on_index = self.units.index(on_unit)
            in_value = float(self.value_input.text())
            return in_value, in_index, on_index
        except ValueError:
            print("Error")

    def output(self):
        in_value, in_index, on_index = self.get_value()
        result = table_convert_time[in_index][on_index] * in_value
        self.result.setText(str(result))


class Temperature(QDialog):
    def __init__(self):
        super(Temperature, self).__init__()
        loadUi("UI/converter_temperature.ui", self)
        self.units = ["°C", "°F"]
        self.input_units.addItems(self.units)
        self.output_units.addItems(self.units)

        self.weight.clicked.connect(func_weight)
        self.time.clicked.connect(func_time)
        self.speed.clicked.connect(func_speed)
        self.width.clicked.connect(func_width)
        self.show_result.clicked.connect(self.get_value)
        # (32 °F − 32) × 5/9
        # (72 °C × 9/5) + 32

    def co(self, in_value):
        result = (in_value * (9 / 5) + 32)
        return result

    def fo(self, in_value):
        result = (in_value - 32) * (5 / 9)
        return result

    def conditional(self, in_unit, on_unit, in_value):
        if in_unit == "°C" and on_unit == "°F":
            result = self.co(in_value)
        elif in_unit == "°F" and on_unit == "°C":
            result = self.fo(in_value)
        elif in_unit == on_unit:
            result = in_value
        self.result.setText(str(result))

    def get_value(self):
        try:
            in_unit = self.input_units.currentText()
            on_unit = self.output_units.currentText()
            in_value = float(self.value_input.text())
            self.conditional(in_unit, on_unit, in_value)
        except ValueError:
            print("Error")


class Speed(QDialog):
    def __init__(self):
        super(Speed, self).__init__()
        loadUi("UI/converter_speed.ui", self)
        self.units = ["м/c", "км/ч"]
        self.input_units.addItems(self.units)
        self.output_units.addItems(self.units)

        self.weight.clicked.connect(func_weight)
        self.time.clicked.connect(func_time)
        self.temperature.clicked.connect(func_temperature)
        self.width.clicked.connect(func_width)
        self.show_result.clicked.connect(self.get_value)
        # from m/s: m/s * 3.6
        # from km/h: k/h // 3.6

    def m_s(self, in_value):
        result = in_value * 3.6
        return result

    def km_h(self, in_value):
        result = in_value / 3.6
        return result

    def conditional(self, in_unit, on_unit, in_value):
        if in_unit == "м/c" and on_unit == "км/ч":
            result = self.m_s(in_value)
        elif in_unit == "км/ч" and on_unit == "м/c":
            result = self.km_h(in_value)
        elif in_unit == on_unit:
            result = in_value
        self.result.setText(str(result))

    def get_value(self):
        try:
            in_unit = self.input_units.currentText()
            on_unit = self.output_units.currentText()
            in_value = float(self.value_input.text())
            self.conditional(in_unit, on_unit, in_value)
        except ValueError:
            print("Error")


app = QApplication(sys.argv)
first_screen = Width()
widget = QStackedWidget()
widget.addWidget(first_screen)
widget.setWindowIcon(QtGui.QIcon('icon.png'))
widget.setWindowTitle("Конвертер")
widget.setMaximumSize(700, 700)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Error")

# Renata, 4 November 2022
