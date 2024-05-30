import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QSpinBox,
    QDoubleSpinBox,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tip Calculator")

        main_layout = QHBoxLayout()
        self.create_widgets(main_layout)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        self.calculate_button.clicked.connect(self.calculate_tip)
         
    # Layouts
    def create_widgets(self, main_layout):
        title = QVBoxLayout()
        price = QHBoxLayout()
        percent = QHBoxLayout()
        results = QVBoxLayout()

        # Title widgets
        title_lable = QLabel("Tip Calculator")
        title_lable.setContentsMargins(0, 0, 0, 100)
        title_lable.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        title_lable.setFont(QFont("Libre Baskerville Bold 700", 30))
        title.addWidget(title_lable)

        # Price widgets
        price_label = QLabel("Price of Meal")
        price_label.setFont(QFont("Libre Baskerville", 15))
        self.price_spinbox = QDoubleSpinBox()
        price.addWidget(price_label)
        price.addWidget(self.price_spinbox)
        self.price_spinbox.setMaximum(10000)
        self.price_spinbox.setMinimum(0)

        # Percent widgets
        percent_label = QLabel("Tip Percent")
        percent_label.setFont(QFont("Libre Baskerville", 15))
        self.percent_spinbox = QSpinBox()
        percent.addWidget(percent_label)
        percent.addWidget(self.percent_spinbox)
        self.percent_spinbox.setMaximum(100)
        self.percent_spinbox.setMinimum(0)

        # Results widgets
        results_label = QLabel("Results")
        results_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        results_label.setFont(QFont("Libre Baskerville Bold 700", 20))
        self.results_display = QLineEdit()
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.setFont(QFont("Libre Baskerville Bold 700", 20))
        results.addWidget(results_label)
        results.addWidget(self.results_display)
        results.addWidget(self.calculate_button)

        # Adding to layouts
        main_layout.addLayout(title)
        main_layout.addLayout(percent)
        main_layout.addLayout(price)
        main_layout.addLayout(results)
    
    # Functionality
    def calculate_tip(self):
        try:
            price = self.price_spinbox.value()
            percent = self.percent_spinbox.value()
            tip = price * (percent / 100)
            self.results_display.setText(f"${tip:.2f}")
        except ValueError:
            self.results_display.setText("Invalid input")

app = QApplication(sys.argv)
app.setStyle("Breeze")
window = MainWindow()
window.show()
app.exec()