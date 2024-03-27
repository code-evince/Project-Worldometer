import worldometer
import warnings
import time
# warnings.filterwarnings("ignore")
import sys
import os
import subprocess
import getWorld
# sys.stderr = open(os.devnull,'w')

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
    print("-----------------------")
    print("Welcome to Worldometer")
    print("-----------------------")
    exit = 0
    while(exit==0):
        print("1. World Data and queries")
        print("2. Country Data and queries")
        print("3. EXIT")
        user = int(input("Your input : "))
        if(user == 3):
            exit = 1
            continue
        if(user == 1):
            print("MENU")
            print()
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
            print("11. Main Menu")
            print("12. EXIT")
            country = input("Enter name of the Country : ")
            ip = int(input("Your input : "))
            if(ip==12):
                exit=1
                continue
            if(ip==11):
                continue
            if(ip >0 and ip<11):
                if not check_last_updated("lastUpdated.txt"):
                    getWorld.main()
                run_map_reduce("cache/world.txt",ip,country)


            
        # if(user==2):





def run_map_reduce(file_name, option, country_name):
    mapper_cmd = f"python3 utilities/package1/mapper1.py {option} {file_name}"
    combiner_cmd = f"python3 utilities/package1/combiner1.py {country_name} "
    reducer_cmd =   f"python3 utilities/package1/reducer1.py {country_name} {option}"

    # Constructing the full command
    full_cmd = f"{mapper_cmd} | {combiner_cmd} | {reducer_cmd}"

    # Running the command
    subprocess.run(full_cmd, shell=True)







if __name__ == '__main__':
    main()

# sys.stderr = sys.__stderr__
    

