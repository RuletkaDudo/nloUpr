from PyQt5.QtCore import Qt, QPoint
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPainter, QColor, QPixmap
from random import randint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.flag = 0
        self.setGeometry(300, 300, 300, 300)
        self.NLO = QLabel(self)
        self.NLO.setPixmap(QPixmap('myNlo.png'))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.NLO.move(self.NLO.x(),
                          self.NLO.y() - 5 if self.NLO.y() - 5 >= 0 else self.height() - self.NLO.height())
        elif event.key() == Qt.Key_Down:
            self.NLO.move(self.NLO.x(), (self.NLO.y() + 5) % (self.height() - self.NLO.height()))
        elif event.key() == Qt.Key_Right:
            self.NLO.move((self.NLO.x() + 5) % (self.width() - self.NLO.width()), self.NLO.y())
        elif event.key() == Qt.Key_Left:
            self.NLO.move(self.NLO.x() - 5 if self.NLO.x() - 5 >= 0 else self.width() - self.NLO.width(),
                          self.NLO.y())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
