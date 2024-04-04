import time
import sys
import os
import subprocess
import warnings
import wiki_parser
import wiki_parser_2019
import wiki_parser_2023_2024
import wiki_parser_country
warnings.filterwarnings("ignore")
sys.stderr = open(os.devnull,'w')

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

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
            for month in months:
                name = f'Webpages/timelines/{month}_{year}'
                url = f"https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic_in_{month}_{year}"
                covidnews = wiki_parser.runparser(name, url)
                #write to file
                fname = f'{month}_{year}'
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
            for month in months:
                if (year == 2022 and (month in ['November', 'December'])):
                    continue
                name = f'Webpages/responses/{month}_{year}'
                url = f"https://en.wikipedia.org/wiki/Responses_to_the_COVID-19_pandemic_in_{month}_{year}"
                covidnews = wiki_parser.runparser(name, url)
                #write to file
                fname = f'{month}_{year}'
                loc = f'CovidNewsTxt/responses'
                writefile(fname, loc, covidnews)

    elif ctrl == 3:     #get countries data
        # check cache for the COvid News data
        file_name = "checkCountriesCache.txt"
        write_last_updated_time(file_name) 

        with open('link_countries', 'r') as f:
            url = f.readline()

        pass

    elif ctrl == 4:     #get all countries data
        pass
    
    return


if __name__ == '__main__':
    run()
