import time
import sys
import os
import re
import subprocess
import warnings
import wiki_parser
import wiki_parser_2019
import wiki_parser_2023_2024
import wiki_parser_country
import wiki_parser_singapore_2022
# warnings.filterwarnings("ignore")
# sys.stderr = open(os.devnull,'w')

months = {'January': '01','February': '02','March': '03','April': '04','May': '05','June': '06','July': '07','August': '08','September': '09','October': '10','November': '11','December': '12'}

def get_current_time():
    return time.strftime("%Y-%m-%d %H:%M:%S")

def write_last_updated_time(file_name):
    try:
        with open(file_name, 'w') as f:
            current_time = get_current_time()
            f.write(current_time)
    except Exception as e:
        print(f"An error occurred while writing last updated time: {str(e)}")

def writefile(fname, loc, covidnews):
    with open(f'{loc}/{fname}.txt', 'w') as f:
        for news in covidnews:
            f.write(news)
    f.close()

def readCovidNews(c_name, c_year):
    # Open the text file in read mode
    with open(f"CovidNewsTxt/countries/temp/temp_{c_name}_{c_year}.txt", "r") as file:
        covidnews = []
        paragraph = ""
        
        for line in file:
            # If the line is not empty, append it to the current paragraph
            if line.strip():
                paragraph += line
            # If the line is empty and current paragraph is not empty, 
            # append the current paragraph to the list of covidnews
            elif paragraph:
                covidnews.append(paragraph.strip())
                paragraph = ""
        
        # Append the last paragraph if any
        if paragraph:
            covidnews.append(paragraph.strip())
    file.close()
    return covidnews

def fetch_data_date_wise1(c_name, c_year):
    # getting news
    covidnews = readCovidNews(c_name, c_year)

    # fetching daily news & write to file
    with open(f'CovidNewsTxt/countries/{c_name}_{c_year}.txt', 'w') as file:
        for month_data in covidnews:
            month_name, data = month_data.split("::")
            # print(f"\nMonth: {month_name}")
            # Use regular expression to find dates
            date_pattern = r"(On|By|From) (\d{1,2}) (\w+)"
            dates = re.findall(date_pattern, data)

            for date in dates:
                date_prefix, day, month = date
                month_num = months.get(month.capitalize(), None)
                if month_num:
                    date_str = f"{day} {month}"
                    # Find the data corresponding to the date
                    start_index = data.index(date_prefix + " " + date_str)
                    next_date_pattern = r"(On|By|From) (\d{1,2}) (\w+)"
                    next_date_match = re.search(next_date_pattern, data[start_index + 1:])
                    if next_date_match:
                        end_index = start_index + next_date_match.start()
                    else:
                        end_index = len(data)
                    date_data = data[start_index:end_index]

                    # Check for additional information after the first date
                    additional_info_start = date_data.find(". On")
                    if additional_info_start != -1:
                        additional_info = date_data[additional_info_start + 2:]
                        date_data = date_data[:additional_info_start + 2] + "" + additional_info

                    # Split the input into day and month
                    d, m = date_str.split()
                    # Convert the date into two-digit format
                    t = d.zfill(2)
                    formatted_date = f"{t} {m}"

                    file.write(f"{formatted_date}::{date_data}\n\n")
    file.close()
    return

def fetch_data_date_wise2(c_name, c_year):
    # getting news
    covidnews = readCovidNews(c_name, c_year)

    # fetching daily news & write to file
    with open(f'CovidNewsTxt/countries/{c_name}_{c_year}.txt', 'w') as file:
        # checking for month
        month_pattern = '|'.join(months.keys())

        if c_name == 'England':
            # Regular expression pattern to match dates in the format "DD Month – "
            date_pattern = rf"(\d+\s+({month_pattern}))\s+–\s*(.+?)\s*(?=\d+\s+\w+\s+–|$)"
        elif c_name == 'Singapore':
            # Regular expression pattern to match dates in the format "DD Month: "
            date_pattern = rf"(\d+\s+({month_pattern})):\s*(.+?)\s*(?=\d+\s+\w+:|$)"

        for item in covidnews:
            month, news_items = item.split("::", 1)
            for match in re.finditer(date_pattern, news_items):
                date = match.group(1)
                news = match.group(3)
                # news_by_date.append(f"{date}::{news}")

                # Split the input into day and month
                d, m = date.split()
                # Convert the date into two-digit format
                t = d.zfill(2)
                formatted_date = f"{t} {m}"
                file.write(f"{formatted_date}::{news}\n\n")
    file.close()
    return

def run(ctrl):
    if ctrl == 1:   #get timelines data
        # check cache for the COvid News data
        file_name = "checkTimelinesCache.txt"
        write_last_updated_time(file_name) 

        # handle year 2019      
        name = f'Webpages/timelines/2019'
        url = f"https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_2019"
        covidnews = wiki_parser_2019.runparser(name, url)
        fname = '2019'   #write to file
        loc = f'CovidNewsTxt/timelines'
        writefile(fname, loc, covidnews)
                                     
        # handle year 2020-2022                                   
        for year in [2020, 2021, 2022]:
            for month, num in months.items():
                name = f'Webpages/timelines/{month}_{year}'
                url = f"https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_{month}_{year}"
                covidnews = wiki_parser.runparser(name, url)
                #write to file
                fname = f'{num}_{year}'
                loc = f'CovidNewsTxt/timelines'
                writefile(fname, loc, covidnews)

        # handle year 2023 & 2024 
        for year in [2023, 2024]:
            name = f'Webpages/timelines/{year}'
            url = f"https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_{year}"
            covidnews = wiki_parser_2023_2024.runparser(name, url)
            fname = f'{year}'
            loc = f'CovidNewsTxt/timelines'
            writefile(fname, loc, covidnews)    

    elif ctrl == 2:     #get reponses data
        # check cache for the COvid News data
        file_name = "checkResponsesCache.txt"
        write_last_updated_time(file_name) 

        for year in [2020, 2021, 2022]:
            for month, num in months.items():
                if (year == 2022 and (month in ['November', 'December'])):
                    continue
                name = f'Webpages/responses/{month}_{year}'
                url = f"https://en.wikipedia.org/wiki/Responses_to_the_COVID-19_pandemic_in_{month}_{year}"
                covidnews = wiki_parser.runparser(name, url)
                #write to file
                fname = f'{num}_{year}'
                loc = f'CovidNewsTxt/responses'
                writefile(fname, loc, covidnews)

    elif ctrl == 3:     #get countries data
        # check cache for the COvid News data
        file_name = "checkCountriesCache.txt"
        write_last_updated_time(file_name) 

        with open('link_countries.txt', 'r') as file:
            for line in file:
                if line == '\n':
                    continue
                url = line.strip()
                country = url.split('_')
                c_name = country[6]
                c_year = country[7][1:-1]
                if len(country[7]) != 6:
                    temp = country[7].split('%')
                    m1 = temp[0]
                    m1 = m1[1:]
                    m2 = temp[3]
                    m2 = m2[2:]
                    c_year = f'{m1}_to_{m2}_{country[8][:-1]}'
                # print(f'+{c_name},{c_year},{len(c_year)}+')###########################
                name = f'Webpages/countries/{c_name}_{c_year}'
                if c_name == 'Australia':
                    covidnews = wiki_parser_2019.runparser(name, url)
                elif c_name == 'India':
                    covidnews = wiki_parser.runparser(name, url)
                elif c_name == 'Malaysia':
                    covidnews = wiki_parser_country.runparser(name, url)
                elif c_name == 'England':
                    covidnews = wiki_parser_country.runparser(name, url)
                elif c_name == 'Singapore':
                    if c_year == '2022':
                        covidnews = wiki_parser_singapore_2022.runparser(name, url)
                    else:
                        covidnews = wiki_parser_country.runparser(name, url)

                #write to temp files
                if c_name == 'Australia' or c_name == 'Malaysia':
                    fname = f'temp_{c_name}_{c_year}'
                    loc = f'CovidNewsTxt/countries/temp'
                    writefile(fname, loc, covidnews)
                    fetch_data_date_wise1(c_name, c_year)
                elif c_name == 'India':
                    fname = f'{c_name}_{c_year}'
                    loc = f'CovidNewsTxt/countries'
                    writefile(fname, loc, covidnews)
                elif c_name == 'England' or c_name == 'Singapore':
                    fname = f'temp_{c_name}_{c_year}'
                    loc = f'CovidNewsTxt/countries/temp'
                    writefile(fname, loc, covidnews)
                    fetch_data_date_wise2(c_name, c_year)
        file.close()
        pass

    elif ctrl == 4:     #get all countries data
        # check cache for the COvid News data
        file_name = "checkCountriesCache.txt"
        write_last_updated_time(file_name) 
        pass
    
    return


if __name__ == '__main__':
    run()
