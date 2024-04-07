import wom_downloader as wom
import warnings
import time
warnings.filterwarnings("ignore")
import sys
import os
import subprocess
import getWorld
from getData import main as getCountryData
sys.stderr = open(os.devnull,'w')

worldometers_countrylist = ('France', 'UK', 'Russia', 'Italy', 'Germany', 'Spain', 'Poland', 'Netherlands', 'Ukraine', 'Belgium', 'USA', 'Mexico', 'Canada', 'Cuba', 'Costa Rica', 'Panama', 'India', 'Turkey', 'Iran', 'Indonesia', 'Philippines', 'Japan', 'Israel', 'Malaysia', 'Thailand', 'Iraq', 'Bangladesh', 'Pakistan', 'Brazil', 'Argentina', 'Colombia', 'Peru', 'Chile', 'Bolivia', 'Uruguay', 'Paraguay', 'Venezuela', 'South Africa', 'Morocco', 'Tunisia', 'Ethiopia', 'Libya', 'Egypt', 'Kenya', 'Zambia', 'Algeria', 'Botswana', 'Nigeria', 'Zimbabwe', 'Australia', 'Fiji', 'Papua New Guinea', 'New Caledonia', 'New Zealand', 'Vietnam')
# worldometers_countrylist = ('Vietnam', 'France')

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


options = ['','Total Cases','Active Cases','Total Deaths','Total Recovered','Total Tests','Death/million','Tests/million','New Case','New Death','New Recovered']

def main():
    exit = 0
    while(exit==0):
        print()
        print("------------------------------------")
        print("       Welcome to Worldometer       ")
        print("------------------------------------")
        print("1. World Data and queries")
        print("2. Country Data and queries")
        print("3. MAIN MENU")
        user = int(input("Enter your choice : "))
        if(user == 3):
            exit = 1
            continue
        if(user == 1):
            print("\n-------------- MENU ----------------")
            print("1.  Total Cases")
            print("2.  Active Cases")
            print("3.  Total Deaths")
            print("4.  Total Recovered")
            print("5.  Total Tests")
            print("6.  Death/million")
            print("7.  Tests/million")
            print("8.  New Case")
            print("9.  New Death")
            print("10. New Recovered")
            print("11. GO BACK")
            print("12. MAIN MENU")
            ip = int(input("\nEnter your choice : "))
            # country = input("Enter name of the Country : ")
            if(ip==12):
                exit=1
                continue
            if(ip==11):
                continue
            if(ip >0 and ip<11):
                country = input("Enter name of the Country : ")
                if not check_last_updated("module_worldometer/lastUpdated.txt"):
                    print("\vWait!! Parsing required webpages...\n")
                    getWorld.main()
                run_map_reduce1("module_worldometer/cache/world.txt",ip,country)

        if(user==2):
            print("\n-------------- MENU ----------------")
            print("1.  Change in active cases in %")
            print("2.  Change in daily death in %")
            print("3.  Change in new recovered in %")
            print("4.  Change in new cases in %")
            print("5.  GO BACK")
            print("6.  MAIN MENU")

            #input
            ip = int(input("\nEnter your choice : "))
            # # country = "Bolivia"
            # # start_date = "08-04-2020"
            # # end_date = "12-04-2022"
            # country = input("Enter name of the Country '_' seprated e.g. South_Africa: ")
            # start_date = input("Enter the start date[dd-mm-yyyy format]: ")
            # end_date = input("Enter the end date[dd-mm-yyyy format]: ")
            if(ip==6):
                exit=1
                continue
            if(ip==5):
                continue
            if(ip >0 and ip<5):
                # country = "Bolivia"
                # start_date = "08-04-2020"
                # end_date = "12-04-2022"
                country = input("Enter name of the Country '_' seprated e.g. South_Africa: ")
                start_date = input("Enter the start date[dd-mm-yyyy format]: ")
                end_date = input("Enter the end date[dd-mm-yyyy format]: ")
                if not check_last_updated("module_worldometer/checkCountryCache.txt"):
                    print('\nDownloading Countries webpages...\n')
                    wom.downloader()
                    print('\nParsing Countries webpages...\n')
                    for i in worldometers_countrylist:
                        getCountryData(i)
                        print(f'Parsed Country: {i}')
                run_map_reduce2(start_date, end_date, ip, country)
    pass

def run_map_reduce1(file_name, option, country_name):
    country_name = country_name.replace(' ', '')
    mapper_cmd = f"python3 module_worldometer/utilities/package1/mapper1.py {option} {file_name}"
    combiner_cmd = f"python3 module_worldometer/utilities/package1/combiner1.py {country_name} "
    reducer_cmd =   f"python3 module_worldometer/utilities/package1/reducer1.py {country_name} {option}"

    # Constructing the full command
    full_cmd = f"{mapper_cmd} | {combiner_cmd} | {reducer_cmd}"
    # full_cmd = f"{mapper_cmd} | {combiner_cmd}"

    # Running the command
    subprocess.run(full_cmd, shell=True)
    pass

def change_format(date):
    months = {"01": "Jan","02": "Feb","03": "Mar","04": "Apr","05": "May","06": "Jun","07": "Jul","08": "Aug","09": "Sep","10": "Oct","11": "Nov","12": "Dec"}
    dd, mm, yyyy = date.split('-')
    mm = months[mm]
    date = f"'{mm} {dd}, {yyyy}'"
    return date

def run_map_reduce2(start_date, end_date, option, given_country):
    given_country = given_country.replace(' ', '_')
    reducer_cmd = f"python3 module_worldometer/utilities/package2/reducer2.py {option} {start_date} {end_date} '{given_country}'"

    # normalize date format
    start_date = change_format(start_date)
    end_date = change_format(end_date)

    # Constructing the full command
    temp_cmd = "("
    list_length = len(worldometers_countrylist)
    for index, country in enumerate(worldometers_countrylist):
        country = country.replace(' ', '_')
        ipfile = f"module_worldometer/cache/country/{country}.txt"
        mapper_cmd = f"python3 module_worldometer/utilities/package2/mapper2.py {ipfile} {option} {start_date} {end_date} '{country}' '{given_country}'"
        combiner_cmd = f"python3 module_worldometer/utilities/package2/combiner2.py {start_date} {end_date} '{country}' '{given_country}'"
        if index < (list_length-1):
            temp_cmd += f"{mapper_cmd} | {combiner_cmd} & "
        else:
            temp_cmd += f"{mapper_cmd} | {combiner_cmd})"
    
    full_cmd = f"{temp_cmd} | {reducer_cmd}"
    # print(full_cmd,"\n")

    # Running the command
    subprocess.run(full_cmd, shell=True)
    pass


if __name__ == '__main__':
    main()

sys.stderr = sys.__stderr__
