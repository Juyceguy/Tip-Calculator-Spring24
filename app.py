import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QSpinBox,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        # Create the layouts
        main_layout = QHBoxLayout()

        # 3 sections
        price = QHBoxLayout()
        percent = QHBoxLayout()
        title = QHBoxLayout()
        results = QVBoxLayout()

        def calculate_tip(self):
            """Calculate Tip"""
            # Get tip percent
            percent = self.percent_spinbox

            # Get price

            # Get tip

            # Display results

        # Title widgets
        title_lable = QLabel("Tip Calculator")
        title_lable.setContentsMargins(0, 0, 0, 100)

        # Price widgets
        # Input
        price_label = QLabel("Price of Meal")
        self.price_spinbox = QSpinBox()

        # Percent widgets
        # Input
        percent_label = QLabel("Tip Percent")
        self.percent_spinbox = QSpinBox()
        
        # results widgets
        results_label = QLabel("Results")
        self.results_display = QLineEdit()
        self.calculate_button = QPushButton("Calculate")
        

        # Align the Title
        title_lable.setAlignment(Qt.AlignmentFlag.AlignHCenter|
                                 Qt.AlignmentFlag.AlignTop)
        title_lable.setFont(QFont("Libre Baskerville Bold 700", 30))
        
        # Align the Results and the Caluclate label
        results_label.setAlignment(Qt.AlignmentFlag.AlignCenter|
                                 Qt.AlignmentFlag.AlignBottom)
        results_label.setFont(QFont("Libre Baskerville Bold 700", 20))
        self.calculate_button.setFont(QFont("Libre Baskerville Bold 700", 20))

        # Price Font 
        price_label.setFont(QFont("Libre Baskerville", 15))

        # Percent Font 
        percent_label.setFont(QFont("Libre Baskerville", 15))

        # Add our top title widgets
        price.addWidget(title_lable)

        # Add our price widgets
        price.addWidget(price_label)
        price.addWidget(self.price_spinbox)

        # Add our percent widgets
        percent.addWidget(percent_label)
        percent.addWidget(self.percent_spinbox)
        
        # Add our bottom title widgets
        results.addWidget(results_label)
        results.addWidget(self.results_display)
        results.addWidget(self.calculate_button)
        
        


        # Add the widgets to the layout
        main_layout.addLayout(title)
        main_layout.addLayout(percent)
        main_layout.addLayout(price)
        main_layout.addLayout(results)


        widget = QWidget()
        widget.setLayout(main_layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)



app = QApplication(sys.argv)
app.setStyle("Breeze")
window = MainWindow()
window.show()

app.exec()
