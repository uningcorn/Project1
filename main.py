## 함수 선언부
def add_num(n1, n2):
    return n1 + n2

def sub_num(n1, n2):
    return n1 - n2

## 전역 변수부
num1, num2, res = 100, 200, 0

## 메인 코드부
res = add_num(num1, num2)
print(num1, '+', num2, '=', res)

res = sub_num(num1, num2)
print(num1, '-', num2, '=', res)
