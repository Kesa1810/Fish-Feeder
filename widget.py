import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fish Feeder")

        central_widget = QWidget(self)
        central_widget.setStyleSheet("background-color: lightblue;")
        central_widget.setFixedSize(QSize(400, 300))
        self.setCentralWidget(central_widget)

        # Main vertical layout to push content to the bottom
        main_layout = QVBoxLayout(central_widget)

        # Horizontal layout to hold buttons side-by-side
        button_layout = QHBoxLayout()

        # Feed Button
        feed = QPushButton()
        feed.setObjectName("feedButton")
        feed.setFixedSize(QSize(180, 65))  # Adjusted size to fit 400px window width
        feed.setCheckable(True)
        feed.pressed.connect(self.feed_pressed)

        # Clean Button
        clean = QPushButton()
        clean.setObjectName("cleanButton")
        clean.setFixedSize(QSize(180, 65))
        clean.setCheckable(True)
        clean.pressed.connect(self.clean_pressed)

        # Add buttons to the horizontal layout
        button_layout.addWidget(feed)
        button_layout.addWidget(clean)

        # Push buttons to the bottom of the window
        main_layout.addStretch()
        main_layout.addLayout(button_layout)

    def feed_pressed(self):
        print("Fish has been fed!")

    def clean_pressed(self):
        print("Tank has been cleaned!")


app = QApplication(sys.argv)

with open("style.css", "r") as f:
    app.setStyleSheet(f.read())

window = MainWindow()
window.show()

app.exec()