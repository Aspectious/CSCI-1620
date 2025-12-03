from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import *
from logic import calculate


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test 10")
        self.setFixedSize(400,400)
        self.setup();

    def setup(self):
        self.layout = QVBoxLayout()
        
        self.title = QLabel("BILL CALCULATOR")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.title)

        self.food_input = QLineEdit();
        self.food_input.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.drink_input = QLineEdit();
        self.drink_input.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.dessert_input = QLineEdit();
        self.dessert_input.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.grid = QGridLayout()
        self.grid.addWidget(QLabel("Food"), 0, 0)
        self.grid.addWidget(self.food_input, 0, 1)
        self.grid.addWidget(QLabel("Drink"), 1, 0)
        self.grid.addWidget(self.drink_input, 1, 1)
        self.grid.addWidget(QLabel("Dessert"), 2, 0)
        self.grid.addWidget(self.dessert_input, 2, 1)
        self.layout.addLayout(self.grid)

    
        self.tip_group = QGroupBox("Tip")
        self.tip_layout = QHBoxLayout()
        self.tip_10 = QRadioButton("10%")
        self.tip_15 = QRadioButton("15%");
        self.tip_20 = QRadioButton("20%")
        self.tip_10.setChecked(True)

        self.tip_buttons = QButtonGroup()
        self.tip_buttons.addButton(self.tip_10, 10)
        self.tip_buttons.addButton(self.tip_15, 15)
        self.tip_buttons.addButton(self.tip_20, 20)

        self.tip_layout.addWidget(self.tip_10)
        self.tip_layout.addWidget(self.tip_15)
        self.tip_layout.addWidget(self.tip_20)
        self.tip_group.setLayout(self.tip_layout)
        self.layout.addWidget(self.tip_group)


        self.RESULTS_TARGET = QLabel("\n\n\n\n\n\n")
        self.RESULTS_TARGET.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.RESULTS_TARGET.setFont(QFont("Courier New"));
        self.layout.addWidget(self.RESULTS_TARGET);

        self.button_row = QHBoxLayout()
        self.submit_button = QPushButton("SUBMIT")
        self.clear_button = QPushButton("CLEAR")
        self.submit_button.clicked.connect(self.submit)
        self.clear_button.clicked.connect(self.clear)
        self.button_row.addWidget(self.submit_button)
        self.button_row.addWidget(self.clear_button)
        self.layout.addLayout(self.button_row)

        self.setLayout(self.layout)

    def replaceResultsWidget(self, replacementText):
        self.RESULTS_TARGET.setText(replacementText);

    def createResults(self, kvobj):
        text = "SUMMARY\n";

        for key,value in kvobj.items():
            key = (key + ":").ljust(20);
            value = f"{value:.2f}".rjust(20);
            text += f"{key}{value}\n";


        self.replaceResultsWidget(text)

    def submit(self):
        try:
            food = float(self.food_input.text())
            drink = float(self.drink_input.text())
            dessert = float(self.dessert_input.text())
            tip_percent = self.tip_buttons.checkedId()
            result = calculate(food, drink, dessert, tip_percent)

            self.createResults(result)
        except ValueError:
            errortext = "Food, Drink, and Dessert\n" + "need to be numeric\n" + "e.g. 10.25 not $10.25"

            self.replaceResultsWidget(errortext)


    def clear(self):
        self.food_input.clear()
        self.drink_input.clear()
        self.dessert_input.clear()
        self.tip_10.setChecked(True)
        self.tip_15.setChecked(False)
        self.tip_20.setChecked(False)
        self.replaceResultsWidget("")