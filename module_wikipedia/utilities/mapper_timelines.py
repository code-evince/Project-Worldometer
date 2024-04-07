import sys

def get_month(month_name):
    month_dict = {
        'January': '01', 'February': '02', 'March': '03', 'April': '04',
        'May': '05', 'June': '06', 'July': '07', 'August': '08',
        'September': '09', 'October': '10', 'November': '11', 'December': '12'
    }

    
    month = month_dict[month_name]

    return month


def convert_to_date(date, year):
    #date - can be like 1 January or Januray

    if len(date.split()) == 2: #Eg. Date: 1 January -> ['1', 'January']
        dd = date.split()[0]

        if len(dd) == 1: #Convert 1 to 01
            dd = '0' + dd 
        elif len(dd) == 5:
            dd = dd[3:]

        mm = get_month(date.split()[1])

        return f'{dd}-{mm}-{year}'
    
    # Eg. Date: January
    else:
        dd = '15'
        mm = get_month(date)
       
        return f'{dd}-{mm}-{year}'

if __name__ == '__main__':
    year = sys.argv[1]

    for line in sys.stdin:
        data = line.strip().split('::')
        if len(data) == 1 or data[0] == 'Background' or len(data[0]) > 13:
            continue
        else:
            date = convert_to_date(data[0], year)
            text = data[1]
            print(f'{date}\t{text}')
