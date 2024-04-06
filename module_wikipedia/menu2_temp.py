import time
import sys
import os
import subprocess
import locale
# import getWikiData
# from getData import main as getCountryData
import warnings
import datetime
import sys
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

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

    valid_files = [] #Stores all files between start and end date

    for root, dirs, files in os.walk('CovidNewsTxt/timelines'):
        for file_name in files:
            if len(file_name) == 11:
                end_year = e_m_year[3:]
                if end_year > '2019':
                    m_year = file_name[:-4]
                    if s_m_year <= m_year <= e_m_year:
                        valid_files.append(file_name)
            else:
                start_year = s_m_year[3:]
                end_year = e_m_year[3:]
                current_year = file_name[0:4]
                
                if start_year <= current_year <= end_year:
                    valid_files.append(file_name)
            
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
    
def run_map_reduce3(start_date, end_date, country_name):
    #Extracting start date and end date in month year formate Eg.01-05-2020 -> 05_2020
    s_m_year_temp = start_date[3:]
    s_m_year =  s_m_year_temp.replace('-', '_')
    start_year = s_m_year[3:]
    
    
    e_m_year_temp = end_date[3:]
    e_m_year = e_m_year_temp.replace('-', '_')
    end_year = e_m_year[3:]

    valid_files = [] #Stores all files between start and end date

    for root, dirs, files in os.walk('CovidNewsTxt/countries'):
        for file_name in files:
            if file_name.startswith(country_name):
                current_year = file_name[-8:-4]
                if start_year <= current_year <= end_year:
                    valid_files.append(file_name)

    valid_files = sorted(valid_files)
    
    cmd = '('
    for file_name in valid_files:
        year = file_name[-8:-4]
        cat_cmd = f'cat CovidNewsTxt/countries/{file_name} |' 
        mapper_cmd = f'python3 mapper_countries.py {year} | sort -nk 1 |'
        combiner_cmd = f'python3 combiner_countries.py  &'

        cmd += cat_cmd + mapper_cmd + combiner_cmd
    
    cmd = cmd[:-1]

    cmd = cmd + ')'
    
    cmd = cmd + f' |sort -t - -k 3,3n -k 2,2n -k 1,1n |python3 reducer_countries.py {start_date} {end_date}'
    
    subprocess.run(cmd, shell=True)
    
def run_map_reduce4(start_date, end_date, country_name):
    #Extracting start date and end date in month year formate Eg.01-05-2020 -> 05_2020
    s_m_year_temp = start_date[3:]
    s_m_year =  s_m_year_temp.replace('-', '_')
    start_year = s_m_year[3:]
    
    
    e_m_year_temp = end_date[3:]
    e_m_year = e_m_year_temp.replace('-', '_')
    end_year = e_m_year[3:]

    valid_files = [] #Stores all files between start and end date

    for root, dirs, files in os.walk('CovidNewsTxt/countries'):
        for file_name in files:
            if file_name.startswith(country_name):
                current_year = file_name[-8:-4]
                if start_year <= current_year <= end_year:
                    valid_files.append(file_name)

    valid_files = sorted(valid_files)
    
    cmd = '('
    for file_name in valid_files:
        year = file_name[-8:-4]
        cat_cmd = f'cat CovidNewsTxt/countries/{file_name} |' 
        mapper_cmd = f'python3 mapper_countries.py {year} | sort -nk 1 |'
        combiner_cmd = f'python3 combiner_countries.py  &'

        cmd += cat_cmd + mapper_cmd + combiner_cmd
    
    cmd = cmd[:-1]

    cmd = cmd + ')'
    
    cmd = cmd + f' |sort -t - -k 3,3n -k 2,2n -k 1,1n |python3 reducer_countries.py {start_date} {end_date} > {country_name}_result.txt'

    print(cmd)
    
    subprocess.run(cmd, shell=True)

def get_jaccard_similarity(file1, file2):

    # Read contents of files
    with open(file1, 'r') as f1:
        text1 = f1.read().lower()
    with open(file2, 'r') as f2:
        text2 = f2.read().lower()

    # Tokenize text and remove stopwords
    stop_words = set(stopwords.words('english'))
    words1 = [word for word in word_tokenize(text1) if word.isalnum() and word not in stop_words]
    words2 = [word for word in word_tokenize(text2) if word.isalnum() and word not in stop_words]

    # Calculate Jaccard similarity
    intersection = len(set(words1).intersection(set(words2)))
    union = len(set(words1).union(set(words2)))
    similarity = intersection / union if union != 0 else 0

    return similarity

def jaccard_similarity(start_date, end_date, current_country_name):
    # Read contents of files
    # List of countries
    start_year = start_date[-4:]
    end_year = end_date[-4:]

    countries = ['Australia', 'England', 'India', 'Malaysia', 'Singapore']

    for country in countries:
        run_map_reduce4(start_date, end_date, country)

    file1 = f'{current_country_name}_result.txt'

    similarity = dict()
    for country in countries:
        if country != current_country_name: #Check for all countries except current country
            if country == 'India' and start_year > 2021:
                continue
            else:
                file2 = f'{country}_result.txt'
                similarity[country] = get_jaccard_similarity(file1, file2)

    max_value = 0
    max_key = None
    for key, value in similarity.items():
        if value > max_value:
            max_value = value
            max_key = key
    
    print(f'{current_country_name} has highest Jaccard Similarity with {max_key}\nJaccard Similarity: {max_value}')


def is_valid_date(date_str):
    try:
        # Set the locale to ensure consistent interpretation of date format
        locale.setlocale(locale.LC_TIME, 'en_IN.UTF-8')  # Set to 'en_IN.UTF-8' for English, India
        
        # Attempt to parse the date string
        datetime.strptime(date_str, '%d-%m-%Y')
        return True
    except Exception as e:
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
            print("1. Wikipedia WCOVID-19 World News")
            print("2. Wikipedia COVID-19 World Responses")
            print("3. Wikipedia COVID-19 Country-wise News") #Check if country name exists
            print("4. Jaccard Similarity for Country")
            print("5. Menu")
            print("6. EXIT")
            user = int(input("\nEnter your choice: "))
            if(user == 6):
                exit = 1
                continue

            elif(user == 5):
                continue

            elif(user == 1):
                # if not check_last_updated("checkTimelinesCache.txt"):
                #     print('\nWait!! Downloading & Parsing Countries webpages...\n')
                #     getWikiData.run(1)

                start_date = input("Enter the start date[dd-mm-yyyy format]: ")
                end_date = input("Enter the end date[dd-mm-yyyy format]: ")

                if not is_valid_date(start_date):
                    print('Invalid Start Date')
                elif not is_valid_date(end_date):
                    print('Invalid End Date')
                else:
                    print('Inside user 1, starting condition passed')
                    start_year = start_date[-4:]
                    end_year = end_date[-4:]
                    
                    if start_year > '2024':
                        print('Start Date beyond scope')
                    elif end_year < '2019':
                        print('End Date beyond scope')
                    elif start_year > end_year:
                        print('Start Date greater than End Date')
                    else:
                        print('Reached to function')
                        run_map_reduce1(start_date, end_date)
                

                # run_map_reduce1("cache/world.txt",ip,country)

            elif(user == 2):
                # if not check_last_updated("checkResponsesCache.txt"):
                #     print('\nWait!! Downloading & Parsing Countries webpages...\n')
                #     getWikiData.run(2)

                start_date = input("Enter the start date[dd-mm-yyyy format]: ")
                end_date = input("Enter the end date[dd-mm-yyyy format]: ")

                if not is_valid_date(start_date):
                    print('Invalid Start Date')
                elif not is_valid_date(end_date):
                    print('Invalid End Date')
                
                else:
                    start_year = start_date[-4:]
                    end_year = end_date[-4:]

                    if start_year > '2022':
                        print('Start Date beyond scope')
                    elif end_year < '2020':
                        print('End Date beyond scope')
                    elif start_year > end_year:
                        print('Start Date greater than End Date')
                    else:
                        run_map_reduce2(start_date, end_date)

                # run_map_reduce2(start_date, end_date, ip, country)

            elif(user == 3):
                # if not check_last_updated("checkCountriesCache.txt"):
                #     print('\nWait!! Downloading & Parsing Countries webpages...\n')
                #     getWikiData.run(3)
                country = input("Enter name of the Country: ")

                countries = ['Australia', 'England', 'India', 'Malaysia', 'Singapore']

                if country not in countries:
                    print('Country Name not valid')
                
                else:
                    start_date = input("Enter the start date[dd-mm-yyyy format]: ")
                    end_date = input("Enter the end date[dd-mm-yyyy format]: ")

                    if not is_valid_date(start_date):
                        print('Invalid Start Date')
                    elif not is_valid_date(end_date):
                        print('Invalid End Date')
                    
                    else:
                        start_year = start_date[-4:]
                        end_year = end_date[-4:]

                        # if start_year > '2022':
                        #     print('Start Date beyond scope')
                        if end_year < '2020':
                            print('End Date beyond scope')
                        elif start_year > end_year:
                            print('Start Date greater than End Date')
                        else:
                            run_map_reduce3(start_date, end_date, country)

            elif(user == 4):
                # if not check_last_updated("checkCountriesCache.txt"):
                #     print('\nWait!! Downloading & Parsing Countries webpages...\n')
                #     getWikiData.run(3)
                country = input("Enter name of the Country: ")

                countries = ['Australia', 'England', 'India', 'Malaysia', 'Singapore']

                if country not in countries:
                    print('Country Name not valid')
                
                else:
                    start_date = input("Enter the start date[dd-mm-yyyy format]: ")
                    end_date = input("Enter the end date[dd-mm-yyyy format]: ")

                    if not is_valid_date(start_date):
                        print('Invalid Start Date')
                    elif not is_valid_date(end_date):
                        print('Invalid End Date')
                    
                    else:
                        start_year = start_date[-4:]
                        end_year = end_date[-4:]

                        # if start_year > '2022':
                        #     print('Start Date beyond scope')
                        if end_year < '2020':
                            print('End Date beyond scope')
                        elif start_year > end_year:
                            print('Start Date greater than End Date')
                        elif start_date > 2023:
                            print('Jaccard Score 0')
                        else:
                            jaccard_similarity(start_date, end_date, country) 
                


            else:
                print('Try Again! Enter the valid choice.')
    except:
        print('Error! Check Input!')
        pass
    pass


if __name__ == '__main__':
    main()

sys.stderr = sys.__stderr__
