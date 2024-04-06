import os
import subprocess
import sys
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

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

def run_map_reduce3(start_date, end_date, country_name):
    #Extracting start date and end date in month year formate Eg.01-05-2020 -> 05_2020
    s_m_year_temp = start_date[3:]
    s_m_year =  s_m_year_temp.replace('-', '_')
    start_year = s_m_year[3:]
    
    
    e_m_year_temp = end_date[3:]
    e_m_year = e_m_year_temp.replace('-', '_')
    end_year = e_m_year[3:]

    print(f'Start year {start_year}')
    print(f'End year {end_year}')

    valid_files = [] #Stores all files between start and end date

    for root, dirs, files in os.walk('CovidNewsTxt/countries'):
        for file_name in files:
            if file_name.startswith(country_name):
                current_year = file_name[-8:-4]
                if start_year <= current_year <= end_year:
                    valid_files.append(file_name)

    valid_files = sorted(valid_files)
    
    print()
    print(valid_files)
    print()


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

    print(cmd)
    
    subprocess.run(cmd, shell=True)

def run_map_reduce4(start_date, end_date, country_name):
    #Extracting start date and end date in month year formate Eg.01-05-2020 -> 05_2020
    s_m_year_temp = start_date[3:]
    s_m_year =  s_m_year_temp.replace('-', '_')
    start_year = s_m_year[3:]
    
    
    e_m_year_temp = end_date[3:]
    e_m_year = e_m_year_temp.replace('-', '_')
    end_year = e_m_year[3:]

    print(f'Start year {start_year}')
    print(f'End year {end_year}')

    valid_files = [] #Stores all files between start and end date

    for root, dirs, files in os.walk('CovidNewsTxt/countries'):
        for file_name in files:
            if file_name.startswith(country_name):
                current_year = file_name[-8:-4]
                if start_year <= current_year <= end_year:
                    valid_files.append(file_name)

    valid_files = sorted(valid_files)
    
    print()
    print(valid_files)
    print()


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

    countries = ['Australia', 'England', 'India', 'Malaysia', 'Singapore']

    for country in countries:
        run_map_reduce4(start_date, end_date, country)

    file1 = f'{current_country_name}_result.txt'

    similarity = dict()
    for country in countries:
        if country != current_country_name: #Check for all countries except current country
            file2 = f'{country}_result.txt'
            similarity[country] = get_jaccard_similarity(file1, file2)
    
    print(similarity)

    max_value = 0
    max_key = None
    for key, value in similarity.items():
        if value > max_value:
            max_value = value
            max_key = key
    
    print(f'{current_country_name} has highest Jaccard Similarity with {max_key}\nJaccard Similarity: {max_value}')


        
jaccard_similarity('15-06-2020', '15-12-2021', 'Singapore')


