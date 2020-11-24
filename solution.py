import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('solution.ui', self)
        self.connection = sqlite3.connect('solution.db')
        self.cursor = self.connection.cursor()
        self.pushButton.clicked.connect(self.check)

    def check(self):
        glagol = self.lineEdit.text()
        try:
            glagol = self.cursor.execute(f"""SELECT * FROM trans WHERE name_trans == '{glagol}'""").fetchall()[0][0]
        except:
            pass
        glagol1 = self.cursor.execute(f"""SELECT name_1f FROM '1f' WHERE id_1f == {glagol}""").fetchone()[0]
        glagol2 = self.cursor.execute(f"""SELECT name_2f FROM '2f' WHERE id_2f == {glagol}""").fetchone()[0]
        glagol3 = self.cursor.execute(f"""SELECT name_3f FROM '3f' WHERE id_3f == {glagol}""").fetchone()[0]
        self.lineEdit_2.setText(glagol1)
        self.lineEdit_3.setText(glagol2)
        self.lineEdit_4.setText(glagol3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
