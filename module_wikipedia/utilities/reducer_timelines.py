import sys
from datetime import datetime

if __name__ == '__main__':
    start_date = sys.argv[1]
    end_date = sys.argv[2]

    start_date = datetime.strptime(start_date, "%d-%m-%Y")
    end_date = datetime.strptime(end_date, "%d-%m-%Y")

    for line in sys.stdin:
        data = line.strip().split('\t')


        current_date = data[0]
        text = data[1]

        current_date = datetime.strptime(current_date, "%d-%m-%Y")

        if start_date <= current_date <= end_date:
            print(f'{current_date}\n{text}')
            print()
    