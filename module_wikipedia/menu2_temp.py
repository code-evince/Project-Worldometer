import time
import sys
import os
import subprocess
import getWikiData
# from getData import main as getCountryData
import warnings
import datetime
warnings.filterwarnings("ignore")
sys.stderr = open(os.devnull,'w')

def get_current_time():
    return time.time()

def read_last_updated_time(file_name):
    try:
        with open(file_name, 'r') as f:
            last_updated_time = f.read().strip()
        return last_updated_time
    except Exception as e:
        print(f"An error occurred while reading last updated time: {str(e)}")
        return None

def check_last_updated(file_name):
    last_updated_time = read_last_updated_time(file_name)
    if last_updated_time:
        try:
            last_updated_timestamp = time.mktime(time.strptime(last_updated_time, "%Y-%m-%d %H:%M:%S"))
            current_time = get_current_time()
            twenty_four_hours=  (24 * 3600)  # 24 hours in seconds
            # print(current_time)
            # print(last_updated_time)
            # print(twenty_four_hours)
            # print(current_time - last_updated_timestamp)
            return current_time - last_updated_timestamp < twenty_four_hours
        
        except Exception as e:
            print(f"An error occurred while parsing timestamps: {str(e)}")
            return False
    else:
        return False

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

def run_map_reduce2(start_date, end_date):
    #Extracting start date and end date in month year formate Eg.01-05-2020 -> 05_2020
    s_m_year_temp = start_date[3:]
    s_m_year =  s_m_year_temp.replace('-', '_')

    e_m_year_temp = end_date[3:]
    e_m_year = e_m_year_temp.replace('-', '_')

    valid_files = [] #Stores all files between start and end date

    for root, dirs, files in os.walk('CovidNewsTxt/responses'):
        for file_name in files:
            m_year = file_name[:-4]
            if s_m_year <= m_year <= e_m_year:
                valid_files.append(file_name)

    valid_files = sorted(valid_files)
    
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


    subprocess.run(cmd, shell=True)
    

    

def run_map_reduce3(file_name, option, country_name):
    pass

def is_valid_date(date_str):
    try:
        # Attempt to parse the date string
        datetime.strptime(date_str, '%d-%m-%Y')
        return True
    except ValueError:
        # If ValueError is raised, it means the date string is not valid
        return False
    
def main():
    print("----------------------------------")
    print("        Welcome to Wikipedia")
    print("----------------------------------")
    try:
        exit = 0
        while(exit==0):
            print("\n-------------- MENU --------------")
            print("1. COVID-19 World News")
            print("2. COVID-19 World Responses")
            print("3. COVID-19 Country-wise News")
            print("4. Menu")
            print("5. EXIT")
            user = int(input("\nEnter your choice: "))
            if(user == 5):
                exit = 1
                continue
            elif(user == 4):
                continue
            elif(user == 1):
                if not check_last_updated("checkTimelinesCache.txt"):
                    print('\nWait!! Downloading & Parsing Countries webpages...\n')
                    getWikiData.run(1)
                start_date = input("Enter the start date[dd-mm-yyyy format]: ")
                end_date = input("Enter the end date[dd-mm-yyyy format]: ")
                if not is_valid_date(start_date):
                    print('Invalid Start Date')
                if not is_valid_date(end_date):
                    print('Invalid End Date')
                # run_map_reduce1("cache/world.txt",ip,country)
            elif(user == 2):
                if not check_last_updated("checkResponsesCache.txt"):
                    print('\nWait!! Downloading & Parsing Countries webpages...\n')
                    getWikiData.run(2)
                start_date = input("Enter the start date[dd-mm-yyyy format]: ")
                end_date = input("Enter the end date[dd-mm-yyyy format]: ")
                # run_map_reduce2(start_date, end_date, ip, country)
            elif(user == 2):
                if not check_last_updated("checkCountriesCache.txt"):
                    print('\nWait!! Downloading & Parsing Countries webpages...\n')
                    getWikiData.run(3)
                country = input("Enter name of the Country: ")
                start_date = input("Enter the start date[dd-mm-yyyy format]: ")
                end_date = input("Enter the end date[dd-mm-yyyy format]: ")
                # country = "Bolivia"
                # start_date = "08-04-2020"
                # end_date = "12-04-2022"
                # run_map_reduce3(start_date, end_date, ip, country)
            else:
                print('Try Again! Enter the valid choice.')
    except:
        print('Error! Check Input!')
        pass
    pass


if __name__ == '__main__':
    main()

sys.stderr = sys.__stderr__
