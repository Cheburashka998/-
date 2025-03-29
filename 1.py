import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class ProjectileMotionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Моделирование траектории")
        self.setGeometry(450, 300, 950, 650)
        self.setStyleSheet("background-color: #f0f0f0;")
        self.initializeUI()

    def initializeUI(self):
        main_layout = QVBoxLayout()

        header_label = QLabel("График траектории полета тела", self)
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet("font-size: 22px; font-weight: bold; margin-top: 20px;")
        main_layout.addWidget(header_label)

        input_layout = QVBoxLayout()

        self.speed_input_field = QLineEdit(self)
        self.speed_input_field.setPlaceholderText("Введите скорость (м/с)")
        self.speed_input_field.setStyleSheet("padding: 10px; font-size: 16px; margin: 10px 0;")
        input_layout.addWidget(self.speed_input_field)

        self.angle_input_field = QLineEdit(self)
        self.angle_input_field.setPlaceholderText("Введите угол (градусы)")
        self.angle_input_field.setStyleSheet("padding: 10px; font-size: 16px; margin: 10px 0;")
        input_layout.addWidget(self.angle_input_field)

        self.plot_button = QPushButton("Построить траекторию", self)
        self.plot_button.setStyleSheet("background-color: #28a745; color: white; font-size: 16px; padding: 12px;")
        self.plot_button.clicked.connect(self.plot_trajectory)
        input_layout.addWidget(self.plot_button)

        main_layout.addLayout(input_layout)

        self.canvas = FigureCanvas(plt.figure())
        self.canvas.setFixedSize(650, 450)
        main_layout.addWidget(self.canvas)

        self.setLayout(main_layout)

    def plot_trajectory(self):
        try:
            velocity = float(self.speed_input_field.text())
            angle = float(self.angle_input_field.text())

            if velocity <= 0 or not (0 <= angle <= 90):
                raise ValueError("Введите положительную скорость и угол от 0 до 90 градусов.")

            gravity = 9.81
            angle_radians = np.radians(angle)
            flight_time = 2 * velocity * np.sin(angle_radians) / gravity
            time = np.linspace(0, flight_time, 500)
            horizontal_distance = velocity * np.cos(angle_radians) * time
            vertical_distance = velocity * np.sin(angle_radians) * time - 0.5 * gravity * time ** 2

            self.canvas.figure.clear()
            axis = self.canvas.figure.add_subplot(111)
            axis.plot(horizontal_distance, vertical_distance, color='blue', linewidth=2)
            axis.set_xlabel("Расстояние (м)")
            axis.set_ylabel("Высота (м)")
            axis.set_title("Траектория полета тела")
            axis.grid(True)

            self.canvas.draw()

        except ValueError as e:
            self.display_error_message(str(e))

    def display_error_message(self, message):
        error_dialog = QWidget()
        error_dialog.setWindowTitle("Ошибка")
        error_label = QLabel(message, error_dialog)
        error_label.setStyleSheet("font-size: 14px; color: red; padding: 15px;")
        error_label.move(20, 20)
        error_dialog.resize(300, 100)
        error_dialog.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProjectileMotionApp()
    window.show()
    sys.exit(app.exec())
