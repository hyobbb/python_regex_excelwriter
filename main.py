import sys
from src.parser import *

if __name__ == '__main__':
    inputPath = sys.argv[1]
    filename = '.'.join(inputPath.split('.')[:-1])

    df = openFile(inputPath)
    df['상품명'] = [replace(line) for line in df['상품명']]
    df['변경 후 판매가격(원)'] = df['판매자 판매가격(원)']
    df.to_excel(filename + '_replaced.xlsx', engine='openpyxl', index=False)
