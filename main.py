from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import Qt
from random import randint
import sys


class DrawingWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.should_paint = False

    def paintEvent(self, event):
        if self.should_paint:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)

            color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            brush = QBrush(color)
            painter.setBrush(brush)

            diameter = randint(5, 30)
            x = self.width() // 2 - diameter // 2
            y = self.height() // 2 - diameter // 2
            painter.drawEllipse(x, y, diameter, diameter)

    def draw_circle(self):
        self.should_paint = True
        self.update()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        drawing_widget = DrawingWidget()

        button = QPushButton('Draw')
        button.clicked.connect(drawing_widget.draw_circle)

        layout = QVBoxLayout()
        layout.addWidget(drawing_widget)
        layout.addWidget(button)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())