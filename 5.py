import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QComboBox
from PyQt5.QtCore import Qt

class GasPressureApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Зависимость давления от объёма")
        self.setGeometry(450, 350, 950, 650)
        self.setStyleSheet("background-color: #d1c4e9;")
        self.createUI()

    def createUI(self):
        layout = QVBoxLayout()

        header_label = QLabel("График зависимости давления газа от объёма", self)
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet("font-size: 24px; font-weight: bold; padding: 20px;")
        layout.addWidget(header_label)

        self.temperature_input = QLineEdit(self)
        self.temperature_input.setPlaceholderText("Введите температуру (К)")
        self.temperature_input.setStyleSheet("padding: 10px; font-size: 16px; margin: 12px 0;")
        layout.addWidget(self.temperature_input)

        self.moles_input = QLineEdit(self)
        self.moles_input.setPlaceholderText("Введите количество вещества (моль)")
        self.moles_input.setStyleSheet("padding: 10px; font-size: 16px; margin: 12px 0;")
        layout.addWidget(self.moles_input)

        self.unit_combobox = QComboBox(self)
        self.unit_combobox.addItem("Па")
        self.unit_combobox.addItem("Атм")
        self.unit_combobox.setStyleSheet("padding: 10px; font-size: 16px; margin: 12px 0;")
        layout.addWidget(self.unit_combobox)

        self.plot_button = QPushButton("Построить график", self)
        self.plot_button.setStyleSheet("background-color: #0288d1; color: white; font-size: 16px; padding: 12px;")
        self.plot_button.clicked.connect(self.plot_pressure_graph)
        layout.addWidget(self.plot_button)

        self.setLayout(layout)

    def plot_pressure_graph(self):
        try:
            temperature = float(self.temperature_input.text())
            moles = float(self.moles_input.text())
            unit = self.unit_combobox.currentText()

            if temperature <= 0 or moles <= 0:
                raise ValueError("Температура и количество вещества должны быть положительными значениями!")

            R = 8.314  # Универсальная газовая постоянная
            volume = np.linspace(0.01, 10, 100)
            pressure = (moles * R * temperature) / volume

            if unit == "Атм":
                pressure = pressure / 101325  # Перевод из Па в Атм

            plt.plot(volume, pressure, color="teal", linewidth=2)
            plt.xlabel("Объём (м³)")
            plt.ylabel(f"Давление ({unit})")
            plt.title("Закон Бойля-Мариотта")
            plt.grid(True)
            plt.show()

        except ValueError as e:
            self.display_error_message(str(e))

    def display_error_message(self, message):
        error_dialog = QWidget()
        error_dialog.setWindowTitle("Ошибка")
        error_label = QLabel(message, error_dialog)
        error_label.setStyleSheet("font-size: 14px; color: red; padding: 20px;")
        error_label.move(20, 20)
        error_dialog.resize(320, 120)
        error_dialog.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GasPressureApp()
    window.show()
    sys.exit(app.exec())
