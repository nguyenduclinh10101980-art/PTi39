import json
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("main.ui", self)

        with open("new_data.json", "r", encoding="utf-8") as file:
            self.data = json.load(file)

        self.show_data()

        self.btnComplete.clicked.connect(self.complete)

    def show_data(self):
        self.listHomework.clear()

        for item in self.data:

            if item["completed"]:
                text = " ✅" + item["name"]
            else:
                text = "⬜ " + item["name"]
            self.listHomework.addItem(text)
        with open("new_data.json", "w", encoding="utf-8") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)
        self.show_data()
app = QApplication([])
window = MainWindow()
window.show()
app.exec()