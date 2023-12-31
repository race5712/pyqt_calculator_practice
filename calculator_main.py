import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        ### 레이아웃을 미리 만들어 둠
        layout_box = QGridLayout()

        ### 수식 입력을 위한 LineEdit 위젯 생성
        label_equation = QLabel("calculate: ")
        self.equation = QLineEdit("")
        self.equation.setAlignment(Qt.AlignRight)  # 오른쪽 정렬 설정

        ### 사칙연상 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")

        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))

        ### 사칙연산 버튼을 레이아웃에 추가
        layout_box.addWidget(button_plus, 4, 3)
        layout_box.addWidget(button_minus, 3, 3)
        layout_box.addWidget(button_product, 2, 3)
        layout_box.addWidget(button_division, 1, 3)

        ### =, C, backspace 버튼 생성
        button_equal = QPushButton("=")
        button_C = QPushButton("C")
        button_backspace = QPushButton("Backspace")

        ### =, C, backspace 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_C.clicked.connect(self.button_C_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        ### =, C, backspace 버튼을 레이아웃에 추가
        layout_box.addWidget(button_equal, 5, 3)
        layout_box.addWidget(button_C, 0, 2)
        layout_box.addWidget(button_backspace, 0, 3)

        ### 숫자 버튼 생성하고, 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number == 9:
                layout_box.addWidget(number_button_dict[number], 2, 2)
            elif number == 8:
                layout_box.addWidget(number_button_dict[number], 2, 1)
            elif number == 7:
                layout_box.addWidget(number_button_dict[number], 2, 0)   
            elif number == 6:
                layout_box.addWidget(number_button_dict[number], 3, 2)
            elif number == 5:
                layout_box.addWidget(number_button_dict[number], 3, 1)
            elif number == 4:
                layout_box.addWidget(number_button_dict[number], 3, 0)
            elif number == 3:
                layout_box.addWidget(number_button_dict[number], 4, 2)
            elif number == 2:
                layout_box.addWidget(number_button_dict[number], 4, 1)
            elif number == 1:
                layout_box.addWidget(number_button_dict[number], 4, 0)
            elif number == 0:
                layout_box.addWidget(number_button_dict[number], 5, 1)

        ### 소숫점 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        layout_box.addWidget(button_dot, 5, 2)

        ### +/- 버튼만 완성. 시그널은 구현 x
        button_plus_minus = QPushButton("+/-")
        layout_box.addWidget(button_plus_minus, 5, 0)

        ### 기존 계산기에 없는 항목(버튼) 생성 %, CE, 1/x, x^2, √x / C는 미리 구현된 것을 활용.
        button_rest = QPushButton("%")
        button_CE = QPushButton("CE")
        button_reciprocal = QPushButton("1/x")
        button_square = QPushButton("x^2")
        button_squareroot = QPushButton("√x")

        ### %, CE, 1/x, x^2, √x 버튼 클릭 시 시그널 설정/ CE는 C와 같은 동작으로 구현하기에 같은 함수 사용.
        button_rest.clicked.connect(self.button_rest_clicked)
        button_CE.clicked.connect(self.button_C_clicked)
        button_reciprocal.clicked.connect(self.button_reciprocal_clicked)
        button_square.clicked.connect(self.button_square_clicked)
        button_squareroot.clicked.connect(self.button_squareroot_clicked)
        

        ### %, CE, 1/x, x^2, √x 버튼을 레이아웃에 추가
        layout_box.addWidget(button_rest, 0, 0)
        layout_box.addWidget(button_CE, 0, 1)
        layout_box.addWidget(button_reciprocal, 1, 0)
        layout_box.addWidget(button_square, 1, 1)
        layout_box.addWidget(button_squareroot, 1, 2)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addWidget(label_equation)
        main_layout.addWidget(self.equation)
        main_layout.addLayout(layout_box)

        self.setLayout(main_layout)
        self.show()

        self.save_number = 0
        self.save_operation = ''
        self.save_old_number = 0
    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        if self.save_old_number == 0:
            equation = self.equation.text()
            equation += str(num)
            self.equation.setText(equation)
        else:
            equation = self.equation.text()
            equation += str(num)
            self.equation.setText(equation)
            self.save_number = int(equation)

    def button_operation_clicked(self, operation):
        equation = self.equation.text()
        self.save_old_number = int(equation)
        self.save_operation = operation
        self.equation.setText("")

    def button_equal_clicked(self):
        try:
            if self.save_operation == '+':
                solution = self.save_old_number + self.save_number
                self.equation.setText(str(solution))
                self.save_old_number = 0
                self.save_number = 0
            elif self.save_operation == '-':
                solution = self.save_old_number - self.save_number
                self.equation.setText(str(solution))
                self.save_old_number = 0
                self.save_number = 0
            elif self.save_operation == '*':
                solution = self.save_old_number * self.save_number
                self.equation.setText(str(solution))
                self.save_old_number = 0
                self.save_number = 0
            elif self.save_operation == '/':
                solution = self.save_old_number / self.save_number
                self.equation.setText(str(solution))
                self.save_old_number = 0
                self.save_number = 0
            elif self.save_operation == '%':
                solution = self.save_old_number % self.save_number
                self.equation.setText(str(solution))
                self.save_old_number = 0
                self.save_number = 0
        except Exception as e:
            self.equation.setText("")
    
    def button_C_clicked(self):
        self.equation.setText("")

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)

    def button_rest_clicked(self):
        equation = self.equation.text()
        self.save_old_number = int(equation)
        self.save_operation = "%"
        self.equation.setText("")

    def button_reciprocal_clicked(self):
        try:
            equation = self.equation.text()
            solution = 1 / int(equation)
            self.equation.setText(str(solution))
        except Exception as e:
            self.equation.setText("")
    
    def button_square_clicked(self):
        try:
            equation = self.equation.text()
            solution = int(equation) * int(equation)
            self.equation.setText(str(solution))
        except Exception as e:
            self.equation.setText("")

    def button_squareroot_clicked(self):
        try:
            equation = self.equation.text()
            solution = int(equation) ** 0.5
            self.equation.setText(str(solution))
        except Exception as e:
            self.equation.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
