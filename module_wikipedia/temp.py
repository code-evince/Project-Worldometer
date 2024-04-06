import os
import subprocess
def run_map_reduce2(start_date, end_date):
    #Extracting start date and end date in month year formate Eg.01-05-2020 -> 05_2020
    s_m_year_temp = start_date[3:]
    s_m_year =  s_m_year_temp.replace('-', '_')

    e_m_year_temp = end_date[3:]
    e_m_year = e_m_year_temp.replace('-', '_')

    print(s_m_year)
    print(e_m_year)

    valid_files = [] #Stores all files between start and end date

    for root, dirs, files in os.walk('CovidNewsTxt/responses'):
        for file_name in files:
            m_year = file_name[:-4]
            # print(m_year)
            if s_m_year <= m_year <= e_m_year:
                valid_files.append(file_name)

    valid_files = sorted(valid_files)
    
    print()
    print(valid_files)
    print()


    cmd = '('
    for file_name in valid_files:
        year = file_name[3:7]
        cat_cmd = f'cat CovidNewsTxt/responses/{file_name} |' 
        mapper_cmd = f'python3 mapper_responses.py {year} | sort -nk 1 |'
        combiner_cmd = f'python3 combiner_responses.py  &'

        cmd += cat_cmd + mapper_cmd + combiner_cmd
    
    cmd = cmd[:-1]

    cmd = cmd + ')'
    
    cmd = cmd + f' |sort -t - -k 3,3n -k 2,2n -k 1,1n |python3 reducer_responses.py {start_date} {end_date}'

    print(cmd)
    print()

    subprocess.run(cmd, shell=True)

def run_map_reduce1(start_date, end_date):
    #Extracting start date and end date in month year formate Eg.01-05-2020 -> 05_2020
    s_m_year_temp = start_date[3:]
    s_m_year =  s_m_year_temp.replace('-', '_')

    e_m_year_temp = end_date[3:]
    e_m_year = e_m_year_temp.replace('-', '_')

    print(s_m_year)
    print(e_m_year)

    valid_files = [] #Stores all files between start and end date

    print(f'End year ----------- {e_m_year[3:]}')
    for root, dirs, files in os.walk('CovidNewsTxt/timelines'):
        for file_name in files:
            if len(file_name) == 11:
                end_year = e_m_year[3:]
                if end_year > '2019':
                    m_year = file_name[:-4]
                    # print(m_year)
                    if s_m_year <= m_year <= e_m_year:
                        valid_files.append(file_name)
            else:
                print(file_name)
                start_year = s_m_year[3:]
                end_year = e_m_year[3:]
                current_year = file_name[0:4]
                
                if start_year <= current_year <= end_year:
                    valid_files.append(file_name)
            

    print()
    print(valid_files)
    print()

    cmd = '('
    for file_name in valid_files:
        if len(file_name) == 11:
            year = file_name[3:7]
        else:
            year = file_name[0:4]
        cat_cmd = f'cat CovidNewsTxt/timelines/{file_name} |' 
        mapper_cmd = f'python3 mapper_timelines.py {year} | sort -nk 1 |'
        combiner_cmd = f'python3 combiner_timelines.py  &'

        cmd += cat_cmd + mapper_cmd + combiner_cmd
    
    cmd = cmd[:-1]

    cmd = cmd + ')'
    
    cmd = cmd + f' |sort -t - -k 3,3n -k 2,2n -k 1,1n |python3 reducer_timelines.py {start_date} {end_date}'

    print(cmd)

    subprocess.run(cmd, shell=True)

def get_month(month_name):
    month_dict = {
        'January': '01', 'February': '02', 'March': '03', 'April': '04',
        'May': '05', 'June': '06', 'July': '07', 'August': '08',
        'September': '09', 'October': '10', 'November': '11', 'December': '12'
    }

    
    month = month_dict[month_name]

    return month

run_map_reduce1('15-06-2019', '15-12-2021')


