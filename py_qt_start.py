from PyQt5.QtWidgets import (QLabel, QApplication, QTextEdit, QListWidget,
                            QPushButton, QLineEdit, QWidget, QHBoxLayout, QVBoxLayout)

app = QApplication([])

window = QWidget()
window.resize(600, 500)
window.setWindowTitle("Розумні замітки")

window.show()
main_line = QHBoxLayout()

line1 = QVBoxLayout()

text = QTextEdit()
list1 = QListWidget()
list2 = QListWidget()
list3 = QLineEdit()
add_btn = QPushButton("Створити замітку")
del_btn = QPushButton("Видалити замітку")
save_btn = QPushButton("Зберегти замітку")
line2 = QHBoxLayout()
line2.addWidget(add_btn)
line2.addWidget(del_btn)

add_tag_btn = QPushButton("Додати до нотатки")
del_tag_btn = QPushButton("Видалити з нотатки")
search_tag_btn = QPushButton("Шукати за тегом")
tag_line = QHBoxLayout()
tag_line.addWidget(add_tag_btn)
tag_line.addWidget(del_tag_btn)

line1.addWidget(QLabel("Список заміток"))
line1.addWidget(list1)
line1.addLayout(line2)
line1.addWidget(save_btn)
line1.addWidget(QLabel("Список тегів"))
line1.addWidget(list2)
line1.addWidget(list3)
line1.addLayout(tag_line)
line1.addWidget(search_tag_btn)
main_line.addWidget(text)
main_line.addLayout(line1)

window.setLayout(main_line)

app.exec()

notes = {
    "Назва замітки": {
        "текст": "Дуже важливий текст заміткі",
        "теги": ["чернетка", "думки"]
    }
}