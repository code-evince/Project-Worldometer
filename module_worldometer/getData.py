import graph_dailyDeaths
import graph_activeCases
import graph_recovered_newCases
import warnings
warnings.filterwarnings("ignore")
import sys
import os
import time
sys.stderr = open(os.devnull,'w')


def get_current_time():
    return time.strftime("%Y-%m-%d %H:%M:%S")

def write_last_updated_time(file_name):
    try:
        with open(file_name, 'w') as f:
            current_time = get_current_time()
            f.write(current_time)
    except Exception as e:
        print(f"An error occurred while writing last updated time: {str(e)}")

def main(country):

    # country = input("Enter the name of the country: ")
    active_cases = graph_activeCases.fetchActiveCases(country)
    dates,daily_deaths = graph_dailyDeaths.fetchDailyDeaths(country)
    new_recovery,new_cases = graph_recovered_newCases.fetchRecover_NewCases(country)

    # print('dates ',len(dates))
    # print('active cases',len(active_cases))
    # print('daily deaths',len(daily_deaths))
    # print('new recovery',len(new_recovery))
    # print('new cases',len(new_cases))
    zipped_arrays = zip(dates, active_cases, daily_deaths, new_recovery, new_cases)

    # Open the file in write mode
    with open(f"cache\country\{country}.txt", "w") as file:
        # Iterate over the zipped arrays
        for values in zipped_arrays:
            # Join the values with tabs and write to the file
            file.write("\t".join(map(str, values)) + "\n")


if __name__ == '__main__':
    main()

sys.stderr = sys.__stderr__