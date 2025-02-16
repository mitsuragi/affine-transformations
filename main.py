import sys
import math
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QGraphicsScene, QGraphicsView,
    QGraphicsPolygonItem, QVBoxLayout, QWidget, QFormLayout,
    QLineEdit, QPushButton
)
from PyQt6.QtGui import QPolygonF
from PyQt6.QtCore import QPointF


class TriangleApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Афинные преобразования треугольника")
        self.resize(600, 400)

        # Создаём основное окно и графическую сцену
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.triangle = self.create_triangle()
        self.scene.addItem(self.triangle)

        # Поля ввода для параметров
        self.tx_input = QLineEdit("0")
        self.ty_input = QLineEdit("0")
        self.angle_input = QLineEdit("0")
        self.scale_x_input = QLineEdit("1")
        self.scale_y_input = QLineEdit("1")

        # Кнопка для применения преобразований
        apply_button = QPushButton("Применить")
        apply_button.clicked.connect(self.apply_transformations)

        # Создание формы ввода
        form_layout = QFormLayout()
        form_layout.addRow("Смещение X:", self.tx_input)
        form_layout.addRow("Смещение Y:", self.ty_input)
        form_layout.addRow("Угол поворота (°):", self.angle_input)
        form_layout.addRow("Масштаб X:", self.scale_x_input)
        form_layout.addRow("Масштаб Y:", self.scale_y_input)
        form_layout.addWidget(apply_button)

        # Компоновка виджетов
        control_panel = QWidget()
        control_panel.setLayout(form_layout)
        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addWidget(control_panel)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def create_triangle(self):
        """Создаёт равносторонний треугольник"""
        side = 100
        height = (math.sqrt(3) / 2) * side  # Высота треугольника

        points = [
            QPointF(-side / 2, height / 2),  # Левая вершина
            QPointF(side / 2, height / 2),   # Правая вершина
            QPointF(0, -height / 2)          # Верхняя вершина
        ]

        polygon = QPolygonF(points)
        triangle_item = QGraphicsPolygonItem(polygon)
        triangle_item.setTransformOriginPoint(0, 0)  # Центр трансформаций
        return triangle_item

    def apply_transformations(self):
        """Применяет афинные преобразования"""
        try:
            # Получаем значения из полей ввода
            tx = float(self.tx_input.text())
            ty = float(self.ty_input.text())
            angle = float(self.angle_input.text())
            scale_x = float(self.scale_x_input.text())
            scale_y = float(self.scale_y_input.text())

            # Применяем преобразования
            self.triangle.setScale(scale_x)  # Масштабирование (по X и Y)
            self.triangle.setRotation(angle)  # Вращение
            self.triangle.setPos(tx, ty)  # Смещение

        except ValueError:
            print("Ошибка: Введите корректные числа!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TriangleApp()
    window.show()
    sys.exit(app.exec())
