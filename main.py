import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QListWidget, QMessageBox, \
    QLabel, QLineEdit


class ToDoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tasks = []

        self.setWindowTitle("To-Do List Application")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.desc_label = QLabel("Description:", self)
        self.layout.addWidget(self.desc_label)
        self.desc_entry = QLineEdit(self)
        self.layout.addWidget(self.desc_entry)

        self.due_label = QLabel("Due Date:", self)
        self.layout.addWidget(self.due_label)
        self.due_entry = QLineEdit(self)
        self.layout.addWidget(self.due_entry)

        self.priority_label = QLabel("Priority:", self)
        self.layout.addWidget(self.priority_label)
        self.pri_entry = QLineEdit(self)
        self.layout.addWidget(self.pri_entry)

        self.task_entry = QPushButton("Add Task", self)
        self.task_entry.clicked.connect(self.add_task)
        self.layout.addWidget(self.task_entry)

        self.task_list = QListWidget(self)
        self.layout.addWidget(self.task_list)

        self.done_button = QPushButton("Mark as Done", self)
        self.done_button.clicked.connect(self.mark_task_as_done)
        self.layout.addWidget(self.done_button)

        self.central_widget.setLayout(self.layout)

    def add_task(self):
        description = self.desc_entry.text()
        due_date = self.due_entry.text()
        priority = self.pri_entry.text()
        task = f"{description}           Due: {due_date}           Priority: {priority}"

        self.tasks.append(task)
        self.task_list.addItem(task)

        self.desc_entry.clear()
        self.due_entry.clear()

    def mark_task_as_done(self):
        selected_item = self.task_list.currentItem()
        if selected_item:
            selected_item.setBackground(QColor("green"))
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Warning")
            msg_box.setText("No task selected.")
            msg_box.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())
