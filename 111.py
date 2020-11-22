import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint
from PyQt5 import uic
from ui_GUI import Ui_MainWindow

class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUI.ui', self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.paint()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        self.draw_flag(qp)
        # Завершаем рисование
        qp.end()

    def draw_flag(self, qp):
        for i in range(10):
            qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            x = randint(10, 400)
            y = randint(10, 400)
            r = randint(10, 200)
            qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
