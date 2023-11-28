# calculator_practice
PyQt5 based calculator - Used for practice (based on https://studyingrabbit.tistory.com/23)

## Goals/UI 수정 요청 사항
* 기존 UI에서 수정해야 할 항목들 수정하기
1. Equation, Solution 삭제 및 하나의 LineEdit로 바꾸기
2. 4칙연산 버튼 위치 변경하기
  
* 기존 계산기에 없는 항목(버튼)들 추가하기 <br>
%, CE, C, 1/x, x^2, √(2)x

## Goals/기능 관련 요청 사항
* 버튼들의 동작은 clicked.connect() 메서드를 이용하여 연결

* Python의 exec 함수를 사용한 계산은 하지 말 것<br>
math나 numpy 라이브러리를 활용하여 구현할 것

* 기존 계산기에 없는 항목(버튼)에 기능 구현하기<br>
나머지, 값을 0으로 설정, 역수, 제곱, 제곱근


## Getting started
* pyqt5 모듈 설치 (python -m pip install pyqt5)
* 파이썬 파일 실행 (python calculator.main.py)
