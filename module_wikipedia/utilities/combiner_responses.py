import sys

if __name__ == '__main__':

    current_date = None
    current_text = 0
    date = None

    for line in sys.stdin:
        date, text = line.strip().split('\t')
        

        if current_date == date:
            current_text = current_text + ' ' + text  
        else:
            if current_date:
                print(f"{current_date}\t{current_text}")
            
            current_date = date
            current_text = text 
       
        

    if current_date == date:
        print(f"{current_date}\t{current_text}")
        