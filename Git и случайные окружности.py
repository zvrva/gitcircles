import sys

from random import choice

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.n = 0
        self.color = []
        for i in range(0, 256):
            self.color.append(i)

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Git и случайные окружности')
        self.b = QPushButton(self)
        self.b.move(135, 135)
        self.b.resize(30, 30)
        self.b.setText('go')
        self.b.clicked.connect(self.run)

    def run(self):
        self.n = True

    def paintEvent(self, event):
        if self.n:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        c = []
        for i in range(0, 200):
            c.append(i)
        f = choice([1, 2, 3, 4])
        for i in range(f):
            qp.setBrush(QColor(choice(self.color), choice(self.color), choice(self.color)))
            qp.drawEllipse(choice(c), choice(c), choice(c), choice(c))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
