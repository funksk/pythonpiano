from PyQt5.QtWidgets import QApplication, QLabel
import sys
import os

app = QApplication([])
label = QLabel('hello world!')
label.show()
sys.exit(app.exec_())