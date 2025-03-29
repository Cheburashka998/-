import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt

class HarmonicOscillationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("График гармонического колебания")
        self.setGeometry(400, 300, 1000, 750)
        self.setStyleSheet("background-color: #e0f7fa;")
        self.setup_interface()

    def setup_interface(self):
        layout = QVBoxLayout()

        header = QLabel("Гармоническое колебание: График зависимости", self)
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 24px; font-weight: bold; padding: 15px;")
        layout.addWidget(header)

        self.amplitude_input = QLineEdit(self)
        self.amplitude_input.setPlaceholderText("Введите амплитуду (м)")
        self.amplitude_input.setStyleSheet("padding: 12px; font-size: 16px;")
        layout.addWidget(self.amplitude_input)

        self.frequency_input = QLineEdit(self)
        self.frequency_input.setPlaceholderText("Введите частоту (Гц)")
        self.frequency_input.setStyleSheet("padding: 12px; font-size: 16px;")
        layout.addWidget(self.frequency_input)

        self.phase_input = QLineEdit(self)
        self.phase_input.setPlaceholderText("Введите фазу (градусы)")
        self.phase_input.setStyleSheet("padding: 12px; font-size: 16px;")
        layout.addWidget(self.phase_input)

        self.plot_button = QPushButton("Построить график", self)
        self.plot_button.setStyleSheet("background-color: #00838f; color: white; font-size: 16px; padding: 12px;")
        self.plot_button.clicked.connect(self.plot_harmonic_graph)
        layout.addWidget(self.plot_button)

        self.setLayout(layout)

    def plot_harmonic_graph(self):
        try:
            amplitude = float(self.amplitude_input.text())
            frequency = float(self.frequency_input.text())
            phase = float(self.phase_input.text())

            if amplitude <= 0 or frequency <= 0:
                raise ValueError("Амплитуда и частота должны быть положительными значениями!")

            time = np.linspace(0, 10, 1000)
            displacement = amplitude * np.cos(2 * np.pi * frequency * time + np.radians(phase))

            plt.plot(time, displacement, color="orange", linewidth=2)
            plt.xlabel("Время (с)")
            plt.ylabel("Смещение (м)")
            plt.title("Гармоническое колебание")
            plt.grid(True)
            plt.show()

        except ValueError as e:
            self.show_error_popup(str(e))

    def show_error_popup(self, message):
        error_popup = QWidget()
        error_popup.setWindowTitle("Ошибка")
        error_message = QLabel(message, error_popup)
        error_message.setStyleSheet("font-size: 14px; color: red; padding: 15px;")
        error_message.move(20, 20)
        error_popup.resize(320, 120)
        error_popup.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HarmonicOscillationApp()
    window.show()
    sys.exit(app.exec())
