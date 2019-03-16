from cabbagePrice.trainer import CabbageTrainer
from pandas.io.parsers import read_csv

if __name__ == '__main__':
    data = read_csv('price_data.csv', sep=',')  # 현재 작업폴더에 미리 다운받아놓은 데이터 # 쉼표로 구분
    t = CabbageTrainer()
    t.test(data)




    