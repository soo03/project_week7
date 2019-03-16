from calc.first  import First
from calc.second import Second

if __name__ == '__main__':   # main이라고 치면 자동으로 뜸
    first = First()
    #first.execute()     # 실행해보면 연산 결과 나옴 (한번 실행해보고 난 이후 주석으로 막아둠)
    second = Second()
    second.execute()     # 실행해보면 새로 입력한 13, 17을 더해서 first파일에 만들어놓은 연산대로 2를 곱한 값이 나옴

