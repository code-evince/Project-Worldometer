import time
import sys
import os
import subprocess
import getWikiData
# from getData import main as getCountryData
import warnings
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
            return current_time - last_updated_timestamp < twenty_four_hours
        
        except Exception as e:
            print(f"An error occurred while parsing timestamps: {str(e)}")
            return False
    else:
        return False

def run_map_reduce1(file_name, option, country_name):
    # country_name = country_name.replace(' ', '')
    # mapper_cmd = f"python3 utilities/package1/mapper1.py {option} {file_name}"
    # combiner_cmd = f"python3 utilities/package1/combiner1.py {country_name} "
    # reducer_cmd =   f"python3 utilities/package1/reducer1.py {country_name} {option}"

    # # Constructing the full command
    # full_cmd = f"{mapper_cmd} | {combiner_cmd} | {reducer_cmd}"
    # # full_cmd = f"{mapper_cmd} | {combiner_cmd}"

    # # Running the command
    # subprocess.run(full_cmd, shell=True)
    pass

def run_map_reduce2(start_date, end_date, option, given_country):
    # given_country = given_country.replace(' ', '_')
    # reducer_cmd = f"python3 utilities/package2/reducer2.py {option} {start_date} {end_date} '{given_country}'"

    # # normalize date format
    # start_date = change_format(start_date)
    # end_date = change_format(end_date)

    # # Constructing the full command
    # temp_cmd = "("
    # list_length = len(worldometers_countrylist)
    # for index, country in enumerate(worldometers_countrylist):
    #     country = country.replace(' ', '_')
    #     ipfile = f"cache/country/{country}.txt"
    #     mapper_cmd = f"python3 utilities/package2/mapper2.py {ipfile} {option} {start_date} {end_date} '{country}' '{given_country}'"
    #     combiner_cmd = f"python3 utilities/package2/combiner2.py {start_date} {end_date} '{country}' '{given_country}'"
    #     if index < (list_length-1):
    #         temp_cmd += f"{mapper_cmd} | {combiner_cmd} & "
    #     else:
    #         temp_cmd += f"{mapper_cmd} | {combiner_cmd})"
    
    # full_cmd = f"{temp_cmd} | {reducer_cmd}"
    # # print(full_cmd,"\n")

    # # Running the command
    # subprocess.run(full_cmd, shell=True)
    pass

def run_map_reduce3(file_name, option, country_name):
    pass

def main():
    print("----------------------------------")
    print("        Welcome to Wikipedia")
    print("----------------------------------")
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
            # country = "Australia"
            # start_date = "08-04-2020"
            # end_date = "12-04-2022"
            # run_map_reduce3(start_date, end_date, ip, country)
        else:
            print('Try Again! Enter the valid choice.')
    
    pass


if __name__ == '__main__':
    main()

sys.stderr = sys.__stderr__
